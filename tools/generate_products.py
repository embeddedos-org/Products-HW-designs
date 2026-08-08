#!/usr/bin/env python3
"""Render eCAD product directories from the reviewable catalog under tools/catalog.

Why a generator
---------------
The product portfolio spans hundreds of designs. Hand-authoring a datasheet, a
costed bill of materials, and a power simulation for each one produces two
failure modes that are hard to see in review: filler that looks like data, and
arithmetic that drifts. This tool removes both.

Component facts live once, in ``tools/catalog/components.json``. A product
selects parts from that library by key, so the same component carries the same
manufacturer, part number, package, and unit cost everywhere it appears. Costs
are computed, never typed, which makes ``Extended = Quantity x Unit`` and the
BOM total correct by construction rather than by proofreading.

The generated tree is committed, so the repository keeps its existing shape: a
reader browses ``product_datasheet.md`` and ``bom.csv`` exactly as before. The
catalog is what a reviewer reads to check the engineering.

Independent verification
------------------------
``tools/validate_products.py`` re-derives every arithmetic claim from the
generated CSV rather than trusting this generator. A defect here therefore
shows up as a validator failure instead of passing silently, which is the point
of keeping the two tools separate.

What this tool does NOT establish
---------------------------------
It guarantees internal consistency, not external truth. Whether a part number
names a real, in-production component and whether its unit cost resembles a
distributor quote today are claims this tool cannot check. They rest on the
authoring of ``components.json`` and remain unverified against any live source.

Usage
-----
Render every catalog::

    python3 tools/generate_products.py

Render one division and show what changed::

    python3 tools/generate_products.py --division eAerospace_CAD_Design

Check that the committed tree matches the catalog without writing anything::

    python3 tools/generate_products.py --check
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import sys

import cad_geometry
import cad_render

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG_DIR = os.path.join(REPO_ROOT, "tools", "catalog")
COMPONENTS_PATH = os.path.join(CATALOG_DIR, "components.json")
DIVISIONS_DIR = os.path.join(CATALOG_DIR, "divisions")

BOM_HEADER = (
    "Reference,Quantity,Value,Footprint,Manufacturer,MPN,Description,"
    "Unit Cost USD,Extended Cost USD,Source"
)


class CatalogError(Exception):
    """Raised when the catalog is internally inconsistent.

    Carrying a dedicated type keeps a data mistake distinguishable from a bug in
    the renderer, so the message can name the offending product instead of
    surfacing as a KeyError from somewhere deep in a template.
    """


def load_components(path: str = COMPONENTS_PATH) -> dict[str, dict]:
    """Load the curated component library.

    Args:
        path: Location of components.json.

    Returns:
        Mapping of component key to its record. Each record carries
        ``manufacturer``, ``mpn``, ``value``, ``footprint``, ``description``,
        ``cost`` and ``source``.

    Raises:
        CatalogError: If the file is missing, unparseable, or a record omits a
            required field.

    Example:
        >>> library = load_components()
        >>> library["stm32h7b3"]["manufacturer"]
        'STMicroelectronics'
    """
    if not os.path.isfile(path):
        raise CatalogError(f"component library not found at {path}")
    try:
        with open(path, encoding="utf-8") as handle:
            raw = json.load(handle)
    except json.JSONDecodeError as exc:
        raise CatalogError(f"{path} is not valid JSON: {exc}") from exc

    required = ("manufacturer", "mpn", "value", "footprint", "description", "cost", "source")
    library = raw.get("components", {})
    for key, record in library.items():
        missing = [field for field in required if field not in record]
        if missing:
            raise CatalogError(f"component {key!r} is missing {missing}")
        if not isinstance(record["cost"], (int, float)) or record["cost"] < 0:
            raise CatalogError(f"component {key!r} has a non-numeric or negative cost")
    return library


def _escape_csv(text: str) -> str:
    """Quote a CSV field when it contains a comma, quote, or newline.

    A raw newline inside an unquoted field silently splits one row into two,
    which is exactly the corruption this repository already carried once. This
    keeps generated output immune to it.

    Args:
        text: The field value.

    Returns:
        The field, quoted and escaped if required.

    Example:
        >>> _escape_csv("Crypto co-processor")
        'Crypto co-processor'
        >>> _escape_csv('a,b')
        '"a,b"'
    """
    text = str(text).replace("\r", " ").replace("\n", " ")
    if any(ch in text for ch in (",", '"')):
        return '"' + text.replace('"', '""') + '"'
    return text


def render_bom(product: dict, library: dict[str, dict]) -> str:
    """Render a product's bill of materials as canonical CSV text.

    Extended costs and the total are computed from the library, so the
    arithmetic cannot disagree with itself.

    Args:
        product: A product record carrying a ``bom`` list of
            ``{"ref", "part", "qty"}`` entries, optionally overriding
            ``description`` or ``value``.
        library: The component library from load_components().

    Returns:
        The complete CSV text, newline-terminated.

    Raises:
        CatalogError: If a referenced part is unknown, a quantity is not a
            positive integer, or a reference designator repeats.

    Example:
        >>> lib = {"x": {"manufacturer": "M", "mpn": "P", "value": "V",
        ...              "footprint": "F", "description": "D", "cost": 2.0,
        ...              "source": "Mouser"}}
        >>> print(render_bom({"slug": "s", "bom": [{"ref": "U1", "part": "x",
        ...                                         "qty": 3}]}, lib))
        ... # doctest: +ELLIPSIS
        Reference,Quantity,...
        U1-U3,3,V,F,M,P,D,2.00,6.00,Mouser
        TOTAL,,,,,,,6.00,,Approximate BOM cost
        <BLANKLINE>
    """
    slug = product.get("slug", "<unnamed>")
    lines = [BOM_HEADER]
    total = 0.0
    seen: set[str] = set()

    try:
        expanded = cad_geometry.expand_references(product)
    except ValueError as exc:
        raise CatalogError(f"{slug}: {exc}") from exc

    for entry in expanded:
        # The displayed reference is the allocated range (C1-C180), not the
        # catalog's prefix hint, so the BOM names every part the board carries.
        ref = entry["display"]
        if ref in seen:
            raise CatalogError(f"{slug}: duplicate reference designator {ref!r}")
        seen.add(ref)

        key = entry["part"]
        if key not in library:
            raise CatalogError(f"{slug}: BOM entry {ref} names unknown component {key!r}")
        part = library[key]
        qty = entry["qty"]

        unit = float(part["cost"])
        extended = round(unit * qty, 2)
        total += extended

        lines.append(
            ",".join(
                _escape_csv(cell)
                for cell in (
                    ref,
                    qty,
                    entry.get("value", part["value"]),
                    entry.get("footprint", part["footprint"]),
                    part["manufacturer"],
                    part["mpn"],
                    entry.get("description", part["description"]),
                    f"{unit:.2f}",
                    f"{extended:.2f}",
                    part["source"],
                )
            )
        )

    if not seen:
        raise CatalogError(f"{slug}: BOM has no line items")

    lines.append(f"TOTAL,,,,,,,{total:.2f},,Approximate BOM cost")
    return "\n".join(lines) + "\n"


def render_datasheet(product: dict) -> str:
    """Render a product datasheet in the repository's established format.

    Args:
        product: A product record.

    Returns:
        Markdown text for product_datasheet.md.

    Raises:
        CatalogError: If a required field is absent.

    Example:
        >>> text = render_datasheet({
        ...     "title": "T", "part": "eX-1", "revision": "v1.0",
        ...     "date": "2026-08-08", "status": "Design Phase",
        ...     "overview": "o", "specs": [["A", "B"]],
        ...     "pcb": [["Layers", "4"]]})
        >>> text.splitlines()[0]
        '# T — Product Datasheet'
    """
    for field in ("title", "part", "revision", "overview", "specs", "pcb"):
        if field not in product:
            raise CatalogError(f"{product.get('slug', '<unnamed>')}: datasheet needs {field!r}")

    out = [
        f"# {product['title']} — Product Datasheet",
        f"> **Revision:** {product['revision']} | **Date:** {product.get('date', '2026-08-08')}"
        f" | **Status:** {product.get('status', 'Design Phase')}",
        "",
        "## Product Overview",
        product["overview"],
        "",
    ]

    family = product.get("family")
    if family:
        out += ["## Product Family", "", "| Unit | Function | Form Factor |", "|---|---|---|"]
        out += [f"| {u} | {f} | {ff} |" for u, f, ff in family]
        out.append("")

    out += [
        f"## Electrical Specifications — {product['part']}",
        "| Parameter | Specification |",
        "|---|---|",
    ]
    out += [f"| **{name}** | {value} |" for name, value in product["specs"]]
    out.append("")

    out += ["## PCB Specifications", "| Parameter | Value |", "|---|---|"]
    out += [f"| **{name}** | {value} |" for name, value in product["pcb"]]
    out.append("")

    compliance = product.get("compliance")
    if compliance:
        out += ["## Compliance Targets", "| Standard | Scope |", "|---|---|"]
        out += [f"| {std} | {scope} |" for std, scope in compliance]
        out.append("")

    return "\n".join(out)


def render_power_sim(product: dict) -> str:
    """Render a runnable power simulation for a product.

    Two shapes are supported, matching what the repository already uses. A
    ``budget`` simulation sums continuous loads and reports bus current; a
    ``duty`` simulation weights per-mode currents by duty cycle and reports
    average draw and battery life.

    Args:
        product: A product record carrying a ``power`` block.

    Returns:
        Python source for simulation/power_budget_sim.py.

    Raises:
        CatalogError: If the power block is absent or its kind is unknown.

    Example:
        >>> src = render_power_sim({"slug": "s", "power": {
        ...     "kind": "budget", "label": "L", "bus_v": 28,
        ...     "loads": [["SoC", 8.0]]}})
        >>> "TOTAL" in src
        True
    """
    slug = product.get("slug", "<unnamed>")
    power = product.get("power")
    if not power:
        raise CatalogError(f"{slug}: product has no 'power' block")
    kind = power.get("kind")
    label = power["label"]

    if kind == "budget":
        bus_v = power.get("bus_v", 12)
        efficiency = power.get("efficiency", 0.85)
        loads = "\n".join(f'    "{n}": {w},' for n, w in power["loads"])
        return f'''#!/usr/bin/env python3
"""Power budget simulation for {label}."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {{
{loads}
}}
BUS_V = {bus_v}
DCDC_EFFICIENCY = {efficiency}

total = sum(loads.values())
print("=" * 62)
print("{label} — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{{name:<44}} {{watts:>7.3f}} W")
print("-" * 62)
print(f"{{'TOTAL':<44}} {{total:>7.3f}} W")
print(f"{{BUS_V}}V bus current: {{total / BUS_V * 1000:.0f}} mA")
print(f"Input power at {{DCDC_EFFICIENCY:.0%}} DC-DC efficiency: {{total / DCDC_EFFICIENCY:.2f}} W")
'''

    if kind == "duty":
        modes = "\n".join(f'    "{n}": ({a}, {d}),' for n, a, d in power["modes"])
        battery_mah = power["battery_mah"]
        battery_desc = power.get("battery_desc", f"{battery_mah}mAh")
        return f'''#!/usr/bin/env python3
"""Duty-cycled power simulation for {label}."""
# Per-mode current draw in amps, paired with the fraction of time spent there.
# Duty cycles are expected to sum to 1.0 across a full operating period.
modes = {{
{modes}
}}
BATTERY_MAH = {battery_mah}

print("=" * 62)
print("{label} — Power by Mode")
print("=" * 62)
for name, (amps, duty) in modes.items():
    print(f"{{name:<38}} {{amps * 1000:>10.3f}} mA  @ {{duty:>6.2%}}")

duty_total = sum(duty for _, duty in modes.values())
if abs(duty_total - 1.0) > 0.001:
    print(f"\\nWARNING: duty cycles sum to {{duty_total:.3f}}, not 1.000")

average_a = sum(amps * duty for amps, duty in modes.values())
runtime_h = BATTERY_MAH / (average_a * 1000)
print("-" * 62)
print(f"{{'AVERAGE CURRENT':<38}} {{average_a * 1000:>10.3f}} mA")
print(f"Battery life ({battery_desc}): {{runtime_h:,.0f}} h "
      f"({{runtime_h / 24:.1f}} days / {{runtime_h / 8766:.2f}} years)")
'''

    raise CatalogError(f"{slug}: unknown power simulation kind {kind!r}")


def write_if_changed(path: str, content: str, check: bool) -> bool:
    """Write ``content`` to ``path`` unless it already matches.

    Args:
        path: Destination file path.
        content: Desired file content.
        check: When True, report the difference without writing.

    Returns:
        True when the file differed from ``content``.

    Example:
        >>> import tempfile, os
        >>> d = tempfile.mkdtemp()
        >>> write_if_changed(os.path.join(d, "a.txt"), "x", check=False)
        True
        >>> write_if_changed(os.path.join(d, "a.txt"), "x", check=False)
        False
    """
    if os.path.isfile(path):
        with open(path, encoding="utf-8") as handle:
            if handle.read() == content:
                return False
    if not check:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(content)
    return True


def generate_product(division: str, product: dict, library: dict, check: bool) -> list[str]:
    """Generate every file for one product directory.

    Args:
        division: Division directory name.
        product: The product record.
        library: The component library.
        check: Report differences without writing.

    Returns:
        Repository-relative paths that differed from the catalog.

    Example:
        >>> generate_product("d", {"slug": "s"}, {}, check=True)  # doctest: +SKIP
    """
    root = os.path.join(REPO_ROOT, division, product["slug"])
    changed = []

    slug = product["slug"]
    try:
        geometry = cad_render.board_geometry(product)
    except cad_render.CadError as exc:
        raise CatalogError(str(exc)) from exc

    try:
        placement = cad_geometry.place_components(
            cad_geometry.expand_references(product), library, geometry
        )
    except (ValueError, KeyError) as exc:
        raise CatalogError(f"{slug}: placement failed: {exc}") from exc

    files = {
        "product_datasheet.md": render_datasheet(product),
        "bom.csv": render_bom(product, library),
        os.path.join("simulation", "power_budget_sim.py"): render_power_sim(product),
        # CAD artefacts, all derived from the same catalog entry as the
        # datasheet and BOM so the three can never describe different boards.
        os.path.join("hardware", "pcb", f"{slug}.kicad_pcb"): cad_render.render_kicad_pcb(
            product, geometry, placement, library
        ),
        os.path.join("hardware", "pcb", "placement_report.md"): (
            cad_render.render_placement_report(product, geometry, placement)
        ),
        os.path.join("hardware", "pcb", f"{slug}.net"): cad_render.render_netlist(
            product, library
        ),
        os.path.join("hardware", "pcb", "stackup.md"): cad_render.render_stackup(
            product, geometry
        ),
        os.path.join("hardware", "pcb", "fabrication_notes.md"): (
            cad_render.render_fabrication_notes(product, geometry)
        ),
        os.path.join("hardware", "cad", f"{slug}_board_outline.dxf"): (
            cad_render.render_dxf_outline(product, geometry)
        ),
        os.path.join("hardware", "cad", f"{slug}_enclosure.scad"): (
            cad_render.render_enclosure_scad(product, geometry)
        ),
    }
    for relative, content in files.items():
        path = os.path.join(root, relative)
        if write_if_changed(path, content, check):
            changed.append(os.path.relpath(path, REPO_ROOT))
    return changed


def report_coverage() -> int:
    """Print how much of the product taxonomy currently has data on disk.

    Status is derived from the filesystem rather than recorded anywhere, so the
    report cannot drift out of step with reality. A name counts as covered when
    its target directory holds a bom.csv.

    Returns:
        ``0`` always; this is a report, not a gate. Coverage being incomplete is
        a statement of remaining work, not a failure.

    Example:
        >>> report_coverage()  # doctest: +SKIP
        0
    """
    path = os.path.join(CATALOG_DIR, "taxonomy.json")
    if not os.path.isfile(path):
        print(f"error: taxonomy manifest not found at {path}", file=sys.stderr)
        return 1
    with open(path, encoding="utf-8") as handle:
        categories = json.load(handle)["categories"]

    total = covered = 0
    pending_by_division: dict[str, set] = {}
    print(f"{'Category':<38} {'Covered':>9} {'Total':>7}")
    print("-" * 56)

    for category, entries in categories.items():
        cat_total = cat_covered = 0
        for name, division, slug in entries:
            cat_total += 1
            target = os.path.join(REPO_ROOT, division, slug) if slug else os.path.join(REPO_ROOT, division)
            marker = os.path.join(target, "bom.csv") if slug else target
            if os.path.exists(marker):
                cat_covered += 1
            elif slug:
                pending_by_division.setdefault(division, set()).add(slug)
        total += cat_total
        covered += cat_covered
        flag = "" if cat_covered == cat_total else "  <-- incomplete"
        print(f"{category:<38} {cat_covered:>9} {cat_total:>7}{flag}")

    print("-" * 56)
    print(f"{'TOTAL':<38} {covered:>9} {total:>7}   ({covered / total:.0%})")

    if pending_by_division:
        pending_total = sum(len(s) for s in pending_by_division.values())
        print(f"\n{pending_total} product director(ies) still to author, by division:")
        for division in sorted(pending_by_division):
            slugs = sorted(pending_by_division[division])
            print(f"\n  {division}  ({len(slugs)})")
            for slug in slugs:
                print(f"    - {slug}")
    return 0


def generate_division_docs(catalog: dict, check: bool) -> list[str]:
    """Create the four division-level documents for a new division.

    Only runs when the catalog carries a ``division_docs`` block, and never
    overwrites a document that already exists: the sixteen divisions that
    predate this catalog keep their hand-authored README, business plan and
    regulatory path exactly as written.

    Args:
        catalog: A division catalog record.
        check: Report the change without writing.

    Returns:
        Repository-relative paths of the documents created.

    Example:
        >>> generate_division_docs({"division": "x"}, check=True)
        []
    """
    docs = catalog.get("division_docs")
    if not docs:
        return []

    division = catalog["division"]
    root = os.path.join(REPO_ROOT, division)
    products = catalog.get("products", [])
    created = []

    readme = [
        f"# {docs['title']}",
        "",
        f"> {docs['blurb']}",
        "",
        "## Product Lines",
        "",
        "| Product | Category | Key Standard | Status |",
        "|---|---|---|---|",
    ]
    readme += [
        f"| {p['slug']} | {p.get('readme', {}).get('category', '—')} "
        f"| {p.get('readme', {}).get('standard', '—')} | Design |"
        for p in products
    ]
    readme += [
        "",
        "## Directory Structure",
        "",
        "```",
        f"{division}/",
        "├── README.md",
    ]
    readme += [f"├── {p['slug']}/" for p in products]
    readme += [
        "├── docs/",
        "│   ├── business_plan.md",
        "│   └── regulatory_path.md",
        "└── ebuild_simulation/",
        "    └── README.md",
        "```",
        "",
        "Each product directory carries a datasheet, a costed bill of materials, a",
        "runnable power simulation, and trees for CAD and PCB artefacts. The data is",
        "generated from `tools/catalog/` and checked by `tools/validate_products.py`.",
        "",
    ]

    business = [
        f"# {docs['title']} — Business Plan",
        "",
        "## Market Overview",
        docs["market"],
        "",
        "## Target Segments",
        "",
        "| Segment | TAM 2030 | EOS Target Share |",
        "|---|---|---|",
    ]
    business += [f"| {s} | {t} | {share} |" for s, t, share in docs["segments"]]
    business += [
        "",
        "## Revenue Model",
        "",
    ]
    business += [f"- {line}" for line in docs["revenue"]]
    business.append("")

    regulatory = [
        f"# {docs['title']} — Regulatory Path",
        "",
        "## Certifications Required",
        "",
        "| Product | Standard | Authority | Timeline |",
        "|---|---|---|---|",
    ]
    regulatory += [
        f"| {product} | {standard} | {authority} | {timeline} |"
        for product, standard, authority, timeline in docs["certifications"]
    ]
    regulatory += ["", "## Key Standards", ""]
    regulatory += [f"- **{name}**: {scope}" for name, scope in docs["standards"]]
    regulatory.append("")

    ebuild = [
        f"# {docs['title']} — eBuild Simulation",
        "",
        "## Overview",
        "The eBuild simulation framework exercises these CAD designs against the eOS",
        "embedded stack before any physical prototype is committed.",
        "",
        "## Simulation Targets",
        "",
        "| Product | Simulation Type | eOS Module |",
        "|---|---|---|",
    ]
    ebuild += [
        f"| {p['slug']} | {p.get('readme', {}).get('sim', 'Power budget')} "
        f"| {p.get('readme', {}).get('eos', 'eOS HAL')} |"
        for p in products
    ]
    ebuild += [
        "",
        "## Running Simulations",
        "",
        "```bash",
        f"python3 {division}/<product>/simulation/power_budget_sim.py",
        "```",
        "",
        "Every simulation in this division is executed by the repository gate:",
        "",
        "```bash",
        f"python3 tools/validate_products.py --run {division}",
        "```",
        "",
    ]

    for relative, body in (
        ("README.md", readme),
        (os.path.join("docs", "business_plan.md"), business),
        (os.path.join("docs", "regulatory_path.md"), regulatory),
        (os.path.join("ebuild_simulation", "README.md"), ebuild),
    ):
        path = os.path.join(root, relative)
        if os.path.isfile(path):
            continue
        if write_if_changed(path, "\n".join(body), check):
            created.append(os.path.relpath(path, REPO_ROOT))
    return created


def _readme_cell(header: str, product: dict) -> str:
    """Choose the value for one README product-table column.

    Division READMEs were hand-authored and their tables do not share a column
    set, so rows are built by matching the header text rather than by position.
    An unrecognised column yields an em dash instead of silently shifting every
    later cell into the wrong column.

    Args:
        header: The column heading text, as written in the README.
        product: The product record.

    Returns:
        The cell text for that column.

    Example:
        >>> _readme_cell("Product", {"slug": "avionics"})
        'avionics'
        >>> _readme_cell("Nonsense", {"slug": "x"})
        '—'
    """
    readme = product.get("readme", {})
    key = header.strip().lower()
    if key == "product":
        return product["slug"]
    if key in ("category", "segment"):
        return readme.get("category", "—")
    if key in ("key standard", "standard", "standards", "key standards"):
        return readme.get("standard", "—")
    if key in ("key ics", "ics", "key components"):
        return readme.get("ics", "—")
    if key in ("ipc class", "ipc"):
        return readme.get("ipc", "Class 3")
    if key == "status":
        return product.get("status", "Design").replace(" Phase", "")
    return "—"


def update_division_readme(division: str, products: list[dict], check: bool) -> list[str]:
    """Append rows to a division README's product table for any missing product.

    Existing rows are never rewritten, so hand-authored descriptions survive.
    Only products absent from the table are added, which keeps this safe to run
    repeatedly.

    Args:
        division: Division directory name.
        products: The catalog's product records for that division.
        check: Report the change without writing.

    Returns:
        A single-element list naming the README when it changed, else empty.

    Example:
        >>> update_division_readme("eAerospace_CAD_Design", [], check=True)
        []
    """
    path = os.path.join(REPO_ROOT, division, "README.md")
    if not os.path.isfile(path):
        return []
    with open(path, encoding="utf-8") as handle:
        lines = handle.read().splitlines()

    # Locate the product table: the header row and its delimiter, following the
    # first "## Product Lines" heading.
    start = next(
        (i for i, line in enumerate(lines) if line.strip().lower() == "## product lines"),
        None,
    )
    if start is None:
        return []
    header_index = next(
        (i for i in range(start + 1, min(start + 6, len(lines))) if lines[i].startswith("|")),
        None,
    )
    if header_index is None or header_index + 1 >= len(lines):
        return []

    headers = [cell.strip() for cell in lines[header_index].strip("|").split("|")]
    end = header_index + 2
    while end < len(lines) and lines[end].startswith("|"):
        end += 1

    existing = "\n".join(lines[header_index:end])
    additions = [
        "| " + " | ".join(_readme_cell(h, product) for h in headers) + " |"
        for product in products
        if f"| {product['slug']} " not in existing
    ]
    if not additions:
        return []

    updated = "\n".join(lines[:end] + additions + lines[end:]) + "\n"
    if write_if_changed(path, updated, check):
        return [os.path.relpath(path, REPO_ROOT)]
    return []


def load_division_catalogs(only: str | None = None) -> list[dict]:
    """Load every division catalog, or just one.

    Args:
        only: Division directory name to restrict to.

    Returns:
        The parsed catalog records, sorted by division name.

    Raises:
        CatalogError: If a catalog file is unparseable or names no division.

    Example:
        >>> isinstance(load_division_catalogs(), list)
        True
    """
    catalogs = []
    for path in sorted(glob.glob(os.path.join(DIVISIONS_DIR, "*.json"))):
        try:
            with open(path, encoding="utf-8") as handle:
                record = json.load(handle)
        except json.JSONDecodeError as exc:
            raise CatalogError(f"{path} is not valid JSON: {exc}") from exc
        if "division" not in record:
            raise CatalogError(f"{path} does not name a division")
        if only and record["division"] != only:
            continue
        record["_path"] = path
        catalogs.append(record)
    return catalogs


def main(argv: list[str] | None = None) -> int:
    """Render the catalog and report what changed.

    Args:
        argv: Command-line arguments. Defaults to ``sys.argv[1:]``.

    Returns:
        ``0`` on success. With ``--check``, ``1`` when the tree is stale.

    Example:
        >>> main(["--check"])  # doctest: +SKIP
        0
    """
    parser = argparse.ArgumentParser(
        description="Render eCAD product directories from tools/catalog."
    )
    parser.add_argument("--division", help="Render only this division directory.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Report files that would change without writing them.",
    )
    parser.add_argument("--quiet", action="store_true", help="Print only the summary.")
    parser.add_argument(
        "--coverage",
        action="store_true",
        help="Report taxonomy coverage instead of generating anything.",
    )
    args = parser.parse_args(argv)

    if args.coverage:
        return report_coverage()

    try:
        library = load_components()
        catalogs = load_division_catalogs(args.division)
    except CatalogError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if not catalogs:
        target = args.division or DIVISIONS_DIR
        print(f"error: no catalog found for {target}", file=sys.stderr)
        return 1

    changed: list[str] = []
    product_count = 0
    try:
        for catalog in catalogs:
            products = catalog.get("products", [])
            changed.extend(generate_division_docs(catalog, args.check))
            for product in products:
                product_count += 1
                changed.extend(
                    generate_product(catalog["division"], product, library, args.check)
                )
            changed.extend(
                update_division_readme(catalog["division"], products, args.check)
            )
    except CatalogError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if changed and not args.quiet:
        verb = "would change" if args.check else "wrote"
        for path in changed:
            print(f"  {verb}: {path}")

    print(
        f"\n{product_count} product(s) across {len(catalogs)} division(s); "
        f"{len(changed)} file(s) {'stale' if args.check else 'written'}."
    )
    if args.check and changed:
        print("Generated tree is out of date. Run: python3 tools/generate_products.py")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
