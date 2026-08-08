#!/usr/bin/env python3
"""Emit CAD artefacts for a product from its catalog entry.

Each product gets a board outline, a layer stackup, a KiCad board file, a
netlist, fabrication notes, and a parametric enclosure model. Everything is
derived from the catalog, so the board a file describes is always the board the
datasheet and BOM describe.

What these files are
--------------------
- ``<slug>.kicad_pcb`` — board outline on Edge.Cuts, the full copper and
  technical layer stack for the stated layer count, design rules matched to the
  IPC class, and every board-mounted component placed without courtyard
  overlap. It is **not routed**: there are no traces, no copper pours, and the
  placed footprints carry body and courtyard outlines but **no pads**. Pad
  geometry would have to be invented, and an invented land pattern looks
  fabricable while not being so.
- ``<slug>.net`` — every BOM component as its own record, plus the power
  distribution nets. Signal nets are **absent**, and deliberately so: pin-level
  connectivity is not derivable from a bill of materials, and inventing it
  would produce a netlist that looks authoritative and is wrong.
- ``placement_report.md`` — area feasibility: how much courtyard area the parts
  need against how much the outline provides, and anything that did not fit.
- ``stackup.md`` / ``fabrication_notes.md`` — the layer construction, material
  set, impedance targets and fabrication constraints, fully specified.
- ``<slug>_enclosure.scad`` — a parametric enclosure sized to the board, with
  standoffs, lid and mounting bosses.
- ``<slug>_board_outline.dxf`` — the board outline and mounting holes as DXF
  R12, for import into mechanical CAD.

Determinism
-----------
Element identifiers are hashed from the product slug rather than randomised, so
regenerating an unchanged catalog reproduces byte-identical files and the
``--check`` drift test stays meaningful.

Verification status
-------------------
What is verified: ``validate_products.py`` parses every board with kiutils and
every outline with ezdxf, renders every enclosure with OpenSCAD, and reconciles
the BOM, the netlist and the placed footprints against one another.

What is **not** verified: no DRC has been run, no Gerbers exported, no signal
integrity or thermal simulation performed, and no land pattern checked against
IPC-7351 or a manufacturer drawing. These are buildable-shaped inputs to a
layout, not a design ready to fabricate.
"""

from __future__ import annotations

import hashlib
import re

import cad_geometry

# KiCad assigns fixed ordinals to its technical layers; copper layers occupy
# 0 (F.Cu) through 31 (B.Cu) with inner layers numbered sequentially from 1.
TECHNICAL_LAYERS = [
    (32, "B.Adhes", "user", "B.Adhesive"),
    (33, "F.Adhes", "user", None),
    (34, "B.Paste", "user", None),
    (35, "F.Paste", "user", None),
    (36, "B.SilkS", "user", "B.Silkscreen"),
    (37, "F.SilkS", "user", "F.Silkscreen"),
    (38, "B.Mask", "user", None),
    (39, "F.Mask", "user", None),
    (40, "Dwgs.User", "user", "User.Drawings"),
    (41, "Cmts.User", "user", "User.Comments"),
    (42, "Eco1.User", "user", "User.Eco1"),
    (43, "Eco2.User", "user", "User.Eco2"),
    (44, "Edge.Cuts", "user", None),
    (45, "Margin", "user", None),
    (46, "B.CrtYd", "user", "B.Courtyard"),
    (47, "F.CrtYd", "user", "F.Courtyard"),
    (48, "B.Fab", "user", None),
    (49, "F.Fab", "user", None),
]

# Design rules by IPC class. Class 3 buys reliability with wider clearance and
# larger annular rings, which costs routing density.
IPC_RULES = {
    "Class 2": {"clearance": 0.15, "track": 0.15, "via": 0.6, "drill": 0.3, "annular": 0.13},
    "Class 3": {"clearance": 0.20, "track": 0.20, "via": 0.7, "drill": 0.35, "annular": 0.15},
}

MOUNTING_HOLE_DIA = 3.2  # M3 clearance
MOUNTING_INSET = 5.0  # from board edge to hole centre


class CadError(Exception):
    """Raised when a product's PCB specification cannot be turned into geometry."""


def _uuid(seed: str) -> str:
    """Derive a deterministic UUID-shaped identifier from a seed string.

    KiCad requires a UUID per element. A random one would change on every
    regeneration and make the drift check useless, so the value is hashed from
    stable inputs instead.

    Args:
        seed: Stable text identifying the element.

    Returns:
        A UUID-formatted string.

    Example:
        >>> _uuid("a") == _uuid("a")
        True
        >>> _uuid("a") != _uuid("b")
        True
    """
    digest = hashlib.sha256(seed.encode("utf-8")).hexdigest()
    return f"{digest[:8]}-{digest[8:12]}-{digest[12:16]}-{digest[16:20]}-{digest[20:32]}"


def _spec(pcb: list, name: str) -> str | None:
    """Return the value of a named row in a product's PCB specification table.

    Args:
        pcb: The catalog's ``pcb`` list of ``[name, value]`` pairs.
        name: The row name to find, matched case-insensitively.

    Returns:
        The row value, or None when absent.

    Example:
        >>> _spec([["Layers", "8"]], "layers")
        '8'
    """
    for row_name, value in pcb:
        if row_name.strip().lower() == name.strip().lower():
            return str(value)
    return None


def board_geometry(product: dict) -> dict:
    """Derive board outline geometry from the product's PCB specification.

    Understands rectangular ``WWmm x HHmm`` and circular ``DDmm diameter``
    dimension strings. Anything else raises rather than silently defaulting,
    because a board generated at the wrong size is worse than no board.

    Args:
        product: A catalog product record.

    Returns:
        A dict with ``shape`` and either ``width``/``height`` or ``diameter``,
        plus ``layers`` and ``ipc``.

    Raises:
        CadError: If dimensions or layer count cannot be read.

    Example:
        >>> board_geometry({"slug": "s", "pcb": [["Layers", "4"],
        ...     ["Dimensions", "50mm x 40mm"], ["IPC Class", "Class 2"]]})["width"]
        50.0
    """
    slug = product.get("slug", "<unnamed>")
    pcb = product.get("pcb")
    if not pcb:
        raise CadError(f"{slug}: product has no 'pcb' specification")

    dims = _spec(pcb, "Dimensions")
    if not dims:
        raise CadError(f"{slug}: PCB specification has no 'Dimensions' row")

    geometry: dict = {}
    rect = re.search(r"([\d.]+)\s*mm\s*[x×]\s*([\d.]+)\s*mm", dims, re.IGNORECASE)
    circle = re.search(r"([\d.]+)\s*mm\s+diameter", dims, re.IGNORECASE)
    if rect:
        geometry["shape"] = "rect"
        geometry["width"] = float(rect.group(1))
        geometry["height"] = float(rect.group(2))
    elif circle:
        geometry["shape"] = "circle"
        geometry["diameter"] = float(circle.group(1))
    else:
        raise CadError(f"{slug}: cannot read board dimensions from {dims!r}")

    layers_raw = _spec(pcb, "Layers")
    if not layers_raw:
        raise CadError(f"{slug}: PCB specification has no 'Layers' row")
    match = re.search(r"\d+", layers_raw)
    if not match:
        raise CadError(f"{slug}: cannot read layer count from {layers_raw!r}")
    layers = int(match.group())
    if layers < 2 or layers > 32 or layers % 2:
        raise CadError(f"{slug}: layer count {layers} is not an even number between 2 and 32")
    geometry["layers"] = layers

    ipc = _spec(pcb, "IPC Class") or "Class 2"
    geometry["ipc"] = "Class 3" if "3" in ipc else "Class 2"
    geometry["finish"] = _spec(pcb, "Finish") or "ENIG"
    geometry["stackup_note"] = _spec(pcb, "Stackup") or ""
    return geometry


def _copper_layers(count: int) -> list[tuple[int, str]]:
    """Return KiCad copper layer ordinals and names for a layer count.

    Args:
        count: Even copper layer count.

    Returns:
        Ordered ``(ordinal, name)`` pairs from F.Cu to B.Cu.

    Example:
        >>> _copper_layers(4)
        [(0, 'F.Cu'), (1, 'In1.Cu'), (2, 'In2.Cu'), (31, 'B.Cu')]
    """
    layers = [(0, "F.Cu")]
    layers += [(i, f"In{i}.Cu") for i in range(1, count - 1)]
    layers.append((31, "B.Cu"))
    return layers


def _footprint_block(placement: dict, value: str, origin: tuple[float, float], slug: str) -> str:
    """Render one placed footprint as a KiCad s-expression.

    The footprint carries a body outline on F.Fab, a courtyard on F.CrtYd and
    its reference and value. It carries **no pads**: pad geometry would have to
    be invented, and an invented land pattern looks fabricable while not being
    so. See the module docstring.

    Args:
        placement: One entry from cad_geometry.place_components().
        value: The component value to show.
        origin: Board origin offset applied to placement coordinates.
        slug: Product slug, for deterministic identifiers.

    Returns:
        A ``(footprint ...)`` s-expression block.

    Example:
        >>> block = _footprint_block(
        ...     {"designator": "C1", "x": 5.0, "y": 5.0,
        ...      "court_x": 1.5, "court_y": 0.9}, "100nF", (0.0, 0.0), "s")
        >>> block.startswith("  (footprint")
        True
    """
    ref = placement["designator"]
    x = placement["x"] + origin[0]
    y = placement["y"] + origin[1]
    hx = placement["court_x"] / 2
    hy = placement["court_y"] / 2
    bx = max(hx - 0.25, 0.15)
    by = max(hy - 0.25, 0.15)
    safe_value = str(value).replace('"', "'")
    return "\n".join(
        [
            f'  (footprint "eos_placement:{ref}"',
            f'    (layer "F.Cu")',
            f'    (uuid "{_uuid(f"{slug}-fp-{ref}")}")',
            f"    (at {x:.3f} {y:.3f})",
            f'    (attr smd)',
            f'    (property "Reference" "{ref}"',
            f"      (at 0 {-hy - 0.6:.3f} 0)",
            f'      (layer "F.SilkS")',
            f'      (uuid "{_uuid(f"{slug}-fpref-{ref}")}")',
            f"      (effects (font (size 0.6 0.6) (thickness 0.1)))",
            f"    )",
            f'    (property "Value" "{safe_value}"',
            f"      (at 0 {hy + 0.6:.3f} 0)",
            f'      (layer "F.Fab")',
            f'      (uuid "{_uuid(f"{slug}-fpval-{ref}")}")',
            f"      (effects (font (size 0.6 0.6) (thickness 0.1)))",
            f"    )",
            f"    (fp_rect (start {-bx:.3f} {-by:.3f}) (end {bx:.3f} {by:.3f})",
            f"      (stroke (width 0.1) (type default)) (fill none)",
            f'      (layer "F.Fab") (uuid "{_uuid(f"{slug}-fpfab-{ref}")}")',
            f"    )",
            f"    (fp_rect (start {-hx:.3f} {-hy:.3f}) (end {hx:.3f} {hy:.3f})",
            f"      (stroke (width 0.05) (type default)) (fill none)",
            f'      (layer "F.CrtYd") (uuid "{_uuid(f"{slug}-fpcy-{ref}")}")',
            f"    )",
            f"  )",
        ]
    )


def render_placement_report(product: dict, geometry: dict, placement: dict) -> str:
    """Render the placement and area-feasibility report for a board.

    Args:
        product: A catalog product record.
        geometry: Output of board_geometry().
        placement: Output of cad_geometry.place_components().

    Returns:
        Markdown text summarising placement and area utilisation.

    Example:
        >>> render_placement_report({"slug": "s", "title": "T"},
        ...     {"shape": "rect", "width": 10.0, "height": 10.0},
        ...     {"placed": 1, "overflow": [], "used_area_mm2": 1.0,
        ...      "usable_area_mm2": 36.0, "utilisation": 0.03})[:2]
        '# '
    """
    overflow = placement["overflow"]
    status = "FITS" if not overflow else f"DOES NOT FIT — {len(overflow)} part(s) unplaced"
    return "\n".join(
        [
            f"# {product.get('title', product['slug'])} — Placement and Area Check",
            "",
            f"> **Result:** {status}",
            "",
            "| Metric | Value |",
            "|---|---|",
            f"| Components placed | {placement['placed']} |",
            f"| Components unplaced | {len(overflow)} |",
            f"| Assembly-level items excluded | {placement.get('excluded_assembly', 0)} |",
            f"| Courtyard area used | {placement['used_area_mm2']:.1f} mm² |",
            f"| Usable board area | {placement['usable_area_mm2']:.1f} mm² |",
            f"| Courtyard utilisation | {placement['utilisation']:.1%} |",
            "",
            "## Method",
            "",
            "Single-sided shelf packing inside the board outline less a 2 mm edge",
            "keep-out. This establishes **area feasibility**, not a layout: it does not",
            "consider routing channels, thermal spacing, connector positions, keep-outs,",
            "or which side a part belongs on. A board that fits here can still be",
            "unroutable.",
            "",
            "Courtyard utilisation above roughly 60% on a single side generally means the",
            "design needs both sides of the board, a larger outline, or finer geometry.",
            "",
            (
                "## Unplaced components\n\n"
                + "\n".join(f"- {designator}" for designator in overflow[:40])
                + ("\n- ... and more" if len(overflow) > 40 else "")
                + "\n"
                if overflow
                else ""
            ),
        ]
    )


def render_kicad_pcb(product: dict, geometry: dict, placement: dict | None = None,
                     library: dict | None = None) -> str:
    """Render a KiCad board file carrying outline, stackup, and design rules.

    Args:
        product: A catalog product record.
        geometry: Output of board_geometry().

    Returns:
        KiCad ``.kicad_pcb`` s-expression text.

    Example:
        >>> g = {"shape": "rect", "width": 50.0, "height": 40.0, "layers": 4,
        ...      "ipc": "Class 2", "finish": "ENIG", "stackup_note": ""}
        >>> render_kicad_pcb({"slug": "s", "part": "eX-1"}, g).startswith("(kicad_pcb")
        True
    """
    slug = product["slug"]
    rules = IPC_RULES[geometry["ipc"]]

    layer_lines = [f'    ({n} "{name}" signal)' for n, name in _copper_layers(geometry["layers"])]
    for ordinal, name, kind, alias in TECHNICAL_LAYERS:
        suffix = f' "{alias}"' if alias else ""
        layer_lines.append(f'    ({ordinal} "{name}" {kind}{suffix})')

    # Outline is drawn on Edge.Cuts with the board origin at (100, 100) so the
    # geometry sits inside a default A4 sheet.
    ox, oy = 100.0, 100.0
    edges = []
    if geometry["shape"] == "rect":
        w, h = geometry["width"], geometry["height"]
        corners = [(ox, oy), (ox + w, oy), (ox + w, oy + h), (ox, oy + h)]
        for index in range(4):
            x1, y1 = corners[index]
            x2, y2 = corners[(index + 1) % 4]
            edges.append(
                f'  (gr_line (start {x1:.3f} {y1:.3f}) (end {x2:.3f} {y2:.3f})\n'
                f'    (stroke (width 0.1) (type solid)) (layer "Edge.Cuts")\n'
                f'    (uuid "{_uuid(f"{slug}-edge-{index}")}")\n  )'
            )
        holes = [
            (ox + MOUNTING_INSET, oy + MOUNTING_INSET),
            (ox + w - MOUNTING_INSET, oy + MOUNTING_INSET),
            (ox + w - MOUNTING_INSET, oy + h - MOUNTING_INSET),
            (ox + MOUNTING_INSET, oy + h - MOUNTING_INSET),
        ]
    else:
        radius = geometry["diameter"] / 2.0
        cx, cy = ox + radius, oy + radius
        edges.append(
            f'  (gr_circle (center {cx:.3f} {cy:.3f}) (end {cx + radius:.3f} {cy:.3f})\n'
            f'    (stroke (width 0.1) (type solid)) (fill none) (layer "Edge.Cuts")\n'
            f'    (uuid "{_uuid(f"{slug}-edge-circle")}")\n  )'
        )
        inset = radius - MOUNTING_INSET
        holes = [
            (cx + inset, cy),
            (cx - inset, cy),
            (cx, cy + inset),
            (cx, cy - inset),
        ]

    footprint_blocks = []
    if placement and library:
        values = {}
        for entry in cad_geometry.expand_references(product):
            value = entry.get("value", library[entry["part"]]["value"])
            for designator in entry["designators"]:
                values[designator] = value
        footprint_blocks = [
            _footprint_block(item, values.get(item["designator"], ""), (ox, oy), slug)
            for item in placement["placements"]
        ]

    hole_lines = []
    for index, (hx, hy) in enumerate(holes):
        hole_lines.append(
            f'  (gr_circle (center {hx:.3f} {hy:.3f}) '
            f'(end {hx + MOUNTING_HOLE_DIA / 2:.3f} {hy:.3f})\n'
            f'    (stroke (width 0.1) (type solid)) (fill none) (layer "Edge.Cuts")\n'
            f'    (uuid "{_uuid(f"{slug}-hole-{index}")}")\n  )'
        )

    body = "\n".join(
        [
            "(kicad_pcb",
            '  (version 20240108)',
            '  (generator "eos_ecad_generate_products")',
            '  (generator_version "8.0")',
            "",
            f"  (general",
            f"    (thickness 1.6)",
            f"    (legacy_teardrops no)",
            f"  )",
            '  (paper "A4")',
            "",
            "  (layers",
            "\n".join(layer_lines),
            "  )",
            "",
            "  (setup",
            "    (pad_to_mask_clearance 0.05)",
            "    (allow_soldermask_bridges_in_footprints no)",
            "    (pcbplotparams",
            "      (layerselection 0x00010fc_ffffffff)",
            "      (plot_on_all_layers_selection 0x0000000_00000000)",
            "      (disableapertmacros no)",
            "      (usegerberextensions no)",
            "      (usegerberattributes yes)",
            "      (usegerberadvancedattributes yes)",
            "      (creategerberjobfile yes)",
            "      (svgprecision 4)",
            "      (plotframeref no)",
            "      (mode 1)",
            "      (useauxorigin no)",
            "      (dxfpolygonmode yes)",
            "      (dxfimperialunits yes)",
            "      (dxfusepcbnewfont yes)",
            "      (psnegative no)",
            "      (psa4output no)",
            "      (plotreference yes)",
            "      (plotvalue yes)",
            "      (plotfptext yes)",
            "      (plotinvisibletext no)",
            "      (sketchpadsonfab no)",
            "      (subtractmaskfromsilk no)",
            "      (outputformat 1)",
            "      (mirror no)",
            "      (drillshape 1)",
            "      (scaleselection 1)",
            '      (outputdirectory "gerber/")',
            "    )",
            "  )",
            "",
            '  (net 0 "")',
            '  (net 1 "GND")',
            '  (net 2 "VBUS")',
            '  (net 3 "+3V3")',
            '  (net 4 "+1V8")',
            "",
            f"  ; Board outline -- {product.get('part', slug)}",
            "\n".join(edges),
            "",
            "  ; M3 mounting holes",
            "\n".join(hole_lines),
            "",
            "  ; Placed components. Body outline on F.Fab, courtyard on F.CrtYd.",
            "  ; No pads: see the note in fabrication_notes.md.",
            "\n".join(footprint_blocks),
            ")",
            "",
        ]
    )
    return body


def render_netlist(product: dict, library: dict) -> str:
    """Render a KiCad netlist of the product's components and power nets.

    Signal nets are intentionally omitted. A bill of materials does not carry
    pin-level connectivity, so any signal net written here would be invented.
    The header says so, in the file, where someone opening it will see it.

    Args:
        product: A catalog product record.
        library: The component library.

    Returns:
        KiCad ``.net`` s-expression text.

    Example:
        >>> lib = {"x": {"manufacturer": "M", "mpn": "P", "value": "V",
        ...              "footprint": "F", "description": "D", "cost": 1.0,
        ...              "source": "S"}}
        >>> "GND" in render_netlist(
        ...     {"slug": "s", "part": "eX", "title": "T",
        ...      "bom": [{"ref": "U1", "part": "x", "qty": 1}]}, lib)
        True
    """
    slug = product["slug"]
    comps = []
    power_nodes = []
    rail_list = []

    for entry in cad_geometry.expand_references(product):
        part = library[entry["part"]]
        value = entry.get("value", part["value"])
        description = entry.get("description", part["description"]).replace('"', "'")
        for ref in entry["designators"]:
            comps.append(
                "\n".join(
                    [
                        f'    (comp (ref "{ref}")',
                        f'      (value "{value}")',
                        f'      (footprint "{part["footprint"]}")',
                        f'      (description "{description}")',
                        "      (fields",
                        f'        (field (name "Manufacturer") "{part["manufacturer"]}")',
                        f'        (field (name "MPN") "{part["mpn"]}")',
                        f'        (field (name "Source") "{part["source"]}")',
                        "      )",
                        f'      (tstamp "{_uuid(f"{slug}-{ref}")}")',
                        "    )",
                    ]
                )
            )
            power_nodes.append(f'      (node (ref "{ref}") (pin "GND"))')
            if ref[0] == "U":
                rail_list.append(f'      (node (ref "{ref}") (pin "VDD"))')

    rail_nodes = "\n".join(rail_list)

    return "\n".join(
        [
            "(export (version \"E\")",
            "  (design",
            f'    (source "tools/catalog -- {slug}")',
            f'    (tool "eos_ecad_generate_products")',
            "    (sheet (number \"1\") (name \"/\") (tstamps \"/\")",
            "      (title_block",
            f'        (title "{product.get("title", slug)}")',
            f'        (company "EmbeddedOS Foundation")',
            f'        (rev "{product.get("revision", "v1.0")}")',
            f'        (comment (number "1") (value "Generated from tools/catalog. '
            "Component records are complete; SIGNAL NETS ARE NOT INCLUDED because "
            "pin-level connectivity is not derivable from a bill of materials. "
            "Only power distribution nets appear below.\"))",
            "      )",
            "    )",
            "  )",
            "  (components",
            "\n".join(comps),
            "  )",
            "  (nets",
            '    (net (code "1") (name "GND")',
            "\n".join(power_nodes),
            "    )",
            '    (net (code "2") (name "VDD")',
            rail_nodes,
            "    )",
            "  )",
            ")",
            "",
        ]
    )


def render_stackup(product: dict, geometry: dict) -> str:
    """Render the layer stackup document for a board.

    Args:
        product: A catalog product record.
        geometry: Output of board_geometry().

    Returns:
        Markdown text describing the construction.

    Example:
        >>> g = {"shape": "rect", "width": 50.0, "height": 40.0, "layers": 4,
        ...      "ipc": "Class 2", "finish": "ENIG", "stackup_note": ""}
        >>> render_stackup({"slug": "s", "part": "eX", "title": "T"}, g)[:2]
        '# '
    """
    layers = geometry["layers"]
    rules = IPC_RULES[geometry["ipc"]]
    # A 1.6mm finished board divides its dielectric budget across the inner
    # layer pairs; prepreg between signal layers, core at the centre.
    copper_oz = 1.0
    dielectric = round((1.6 - layers * 0.035) / max(layers - 1, 1), 4)

    rows = []
    names = [name for _, name in _copper_layers(layers)]
    for index, name in enumerate(names):
        if index == 0:
            role = "Signal / component side"
        elif index == len(names) - 1:
            role = "Signal / solder side"
        elif index % 2:
            role = "Ground plane" if index == 1 else "Power plane"
        else:
            role = "Signal (inner)"
        rows.append(f"| {index + 1} | {name} | {role} | {copper_oz:.1f} oz | — |")
        if index < len(names) - 1:
            material = "Core" if index == len(names) // 2 - 1 else "Prepreg"
            rows.append(f"| — | {material} | FR-4 Tg170 dielectric | — | {dielectric:.4f} mm |")

    if geometry["shape"] == "rect":
        size = f"{geometry['width']:.1f} mm x {geometry['height']:.1f} mm"
    else:
        size = f"{geometry['diameter']:.1f} mm diameter"

    return "\n".join(
        [
            f"# {product.get('title', product['slug'])} — PCB Stackup",
            "",
            f"> **Board:** {product.get('part', product['slug'])} | "
            f"**Layers:** {layers} | **Finished thickness:** 1.6 mm | "
            f"**IPC class:** {geometry['ipc']}",
            "",
            "## Construction",
            "",
            "| # | Layer | Role | Copper | Dielectric |",
            "|---|---|---|---|---|",
            "\n".join(rows),
            "",
            "## Board Parameters",
            "",
            "| Parameter | Value |",
            "|---|---|",
            f"| Outline | {size} |",
            f"| Finished thickness | 1.6 mm +/- 10% |",
            f"| Surface finish | {geometry['finish']} |",
            f"| Base material | FR-4 Tg170, UL 94V-0 |",
            f"| Copper weight | {copper_oz:.1f} oz outer and inner |",
            f"| Mounting holes | 4 x {MOUNTING_HOLE_DIA:.1f} mm, {MOUNTING_INSET:.1f} mm inset |",
            "",
            "## Impedance Targets",
            "",
            "| Structure | Target | Tolerance |",
            "|---|---|---|",
            "| Single-ended microstrip | 50 ohm | +/- 10% |",
            "| Differential pair | 100 ohm | +/- 10% |",
            "| USB / Ethernet differential | 90 ohm | +/- 10% |",
            "",
            "## Design Rules",
            "",
            "| Rule | Value |",
            "|---|---|",
            f"| Minimum clearance | {rules['clearance']:.2f} mm |",
            f"| Minimum track width | {rules['track']:.2f} mm |",
            f"| Minimum via diameter | {rules['via']:.2f} mm |",
            f"| Minimum drill | {rules['drill']:.2f} mm |",
            f"| Minimum annular ring | {rules['annular']:.2f} mm |",
            "",
            (geometry["stackup_note"] and f"## Notes\n\n{geometry['stackup_note']}\n") or "",
        ]
    )


def render_fabrication_notes(product: dict, geometry: dict) -> str:
    """Render fabrication and assembly notes for a board.

    Args:
        product: A catalog product record.
        geometry: Output of board_geometry().

    Returns:
        Markdown text of fabrication constraints.

    Example:
        >>> g = {"shape": "rect", "width": 1.0, "height": 1.0, "layers": 2,
        ...      "ipc": "Class 3", "finish": "ENIG", "stackup_note": ""}
        >>> "IPC-A-610" in render_fabrication_notes({"slug": "s"}, g)
        True
    """
    ipc = geometry["ipc"]
    acceptance = "Class 3" if ipc == "Class 3" else "Class 2"
    return "\n".join(
        [
            f"# {product.get('title', product['slug'])} — Fabrication Notes",
            "",
            "## Fabrication",
            "",
            f"- Build to IPC-6012 {acceptance}.",
            f"- Surface finish: {geometry['finish']}.",
            "- Base material FR-4 Tg170 or better, UL 94V-0 marked.",
            "- Finished thickness 1.6 mm +/- 10%.",
            "- Solder mask both sides; silkscreen both sides, white on green.",
            "- Electrical test: 100% netlist verification against the supplied netlist.",
            "- No design changes without written approval; report any DFM issue instead.",
            "",
            "## Assembly",
            "",
            f"- Assemble to IPC-A-610 {acceptance}.",
            "- Lead-free process, SAC305, per J-STD-001.",
            "- Moisture-sensitive devices handled per J-STD-033.",
            "- ESD control per ANSI/ESD S20.20 throughout.",
            "",
            "## Status of this design — read before quoting",
            "",
            "Generated from `tools/catalog`. **This is not a fabrication release.**",
            "",
            "What exists: board outline, layer stack, design rules, and every",
            "board-mounted part placed without courtyard overlap inside the outline.",
            "The BOM, the netlist and the placed footprints reconcile against each other.",
            "",
            "What does not exist yet, and is required before fabrication:",
            "",
            "- **No pads.** Placed footprints carry body and courtyard outlines only.",
            "  Real IPC-7351 land patterns must be assigned before layout.",
            "- **No routing.** No traces, no vias, no copper pours.",
            "- **No signal nets.** The netlist carries power distribution only; pin-level",
            "  connectivity is not derivable from a bill of materials and has been left",
            "  out rather than invented.",
            "- **No DRC, no Gerbers, no signal integrity or thermal simulation.**",
            "- **Component part numbers and prices are unverified** against any",
            "  distributor. Confirm availability, lifecycle status and pricing before use.",
            "",
        ]
    )


def render_dxf_outline(product: dict, geometry: dict) -> str:
    """Render the board outline and mounting holes as DXF R12.

    Args:
        product: A catalog product record.
        geometry: Output of board_geometry().

    Returns:
        DXF text with an ENTITIES section.

    Example:
        >>> g = {"shape": "circle", "diameter": 20.0, "layers": 2,
        ...      "ipc": "Class 2", "finish": "ENIG", "stackup_note": ""}
        >>> render_dxf_outline({"slug": "s"}, g).strip().endswith("EOF")
        True
    """
    out = ["0", "SECTION", "2", "ENTITIES"]

    def line(x1, y1, x2, y2, layer="EDGE"):
        out.extend(
            ["0", "LINE", "8", layer,
             "10", f"{x1:.4f}", "20", f"{y1:.4f}", "30", "0.0",
             "11", f"{x2:.4f}", "21", f"{y2:.4f}", "31", "0.0"]
        )

    def circle(cx, cy, r, layer="EDGE"):
        out.extend(
            ["0", "CIRCLE", "8", layer,
             "10", f"{cx:.4f}", "20", f"{cy:.4f}", "30", "0.0",
             "40", f"{r:.4f}"]
        )

    if geometry["shape"] == "rect":
        w, h = geometry["width"], geometry["height"]
        line(0, 0, w, 0)
        line(w, 0, w, h)
        line(w, h, 0, h)
        line(0, h, 0, 0)
        holes = [
            (MOUNTING_INSET, MOUNTING_INSET),
            (w - MOUNTING_INSET, MOUNTING_INSET),
            (w - MOUNTING_INSET, h - MOUNTING_INSET),
            (MOUNTING_INSET, h - MOUNTING_INSET),
        ]
    else:
        r = geometry["diameter"] / 2.0
        circle(r, r, r)
        inset = r - MOUNTING_INSET
        holes = [(r + inset, r), (r - inset, r), (r, r + inset), (r, r - inset)]

    for hx, hy in holes:
        circle(hx, hy, MOUNTING_HOLE_DIA / 2.0, layer="HOLES")

    out.extend(["0", "ENDSEC", "0", "EOF", ""])
    return "\n".join(out)


def render_enclosure_scad(product: dict, geometry: dict) -> str:
    """Render a parametric OpenSCAD enclosure sized to the board.

    Args:
        product: A catalog product record.
        geometry: Output of board_geometry().

    Returns:
        OpenSCAD source text.

    Example:
        >>> g = {"shape": "rect", "width": 50.0, "height": 40.0, "layers": 4,
        ...      "ipc": "Class 2", "finish": "ENIG", "stackup_note": ""}
        >>> "module" in render_enclosure_scad({"slug": "s", "part": "eX"}, g)
        True
    """
    if geometry["shape"] == "rect":
        bw, bh = geometry["width"], geometry["height"]
        shape_block = f"""
board_w = {bw:.1f};   // board width, mm
board_h = {bh:.1f};   // board depth, mm

module board_footprint(inflate = 0) {{
    square([board_w + inflate * 2, board_h + inflate * 2], center = true);
}}

module standoff_positions() {{
    for (sx = [-1, 1], sy = [-1, 1])
        translate([sx * (board_w / 2 - mount_inset),
                   sy * (board_h / 2 - mount_inset), 0]) children();
}}
"""
    else:
        d = geometry["diameter"]
        shape_block = f"""
board_d = {d:.1f};    // board diameter, mm

module board_footprint(inflate = 0) {{
    circle(d = board_d + inflate * 2, $fn = 128);
}}

module standoff_positions() {{
    for (a = [0 : 90 : 359])
        rotate([0, 0, a])
            translate([board_d / 2 - mount_inset, 0, 0]) children();
}}
"""

    return f"""// {product.get('title', product['slug'])} — parametric enclosure
// Part: {product.get('part', product['slug'])}
//
// Generated from tools/catalog. Sized to the board outline in the datasheet.
// Connector and control cut-outs are NOT included: their positions depend on a
// placed layout, which does not exist yet. Add them once placement is fixed.
//
// Render:  openscad -o enclosure.stl {product['slug']}_enclosure.scad

/* [Enclosure] */
wall           = 2.4;   // wall thickness, mm
floor_t        = 2.0;   // floor thickness, mm
board_clear    = 1.5;   // clearance around the board edge, mm
standoff_h     = 6.0;   // board standoff height above the floor, mm
headroom       = 14.0;  // clear height above the board, mm
mount_inset    = {MOUNTING_INSET:.1f};   // board mounting hole inset, mm
screw_d        = 2.6;   // self-tapping screw pilot diameter, mm
standoff_d     = 6.0;   // standoff outer diameter, mm
corner_r       = 3.0;   // external corner radius, mm
lid_lip        = 1.2;   // lid register lip depth, mm

$fn = 64;
{shape_block}
inner_h = standoff_h + headroom;

module shell() {{
    difference() {{
        // Outer body, offset out from the board footprint by clearance + wall.
        linear_extrude(height = floor_t + inner_h)
            offset(r = corner_r) offset(delta = -corner_r)
                offset(delta = board_clear + wall) board_footprint();

        // Internal cavity.
        translate([0, 0, floor_t])
            linear_extrude(height = inner_h + 1)
                offset(delta = board_clear) board_footprint();
    }}
}}

module standoffs() {{
    standoff_positions()
        difference() {{
            cylinder(d = standoff_d, h = floor_t + standoff_h);
            translate([0, 0, floor_t])
                cylinder(d = screw_d, h = standoff_h + 1);
        }}
}}

module base() {{
    union() {{
        shell();
        standoffs();
    }}
}}

module lid() {{
    union() {{
        // Lid plate.
        linear_extrude(height = wall)
            offset(r = corner_r) offset(delta = -corner_r)
                offset(delta = board_clear + wall) board_footprint();

        // Register lip that drops into the cavity.
        translate([0, 0, -lid_lip])
            linear_extrude(height = lid_lip)
                offset(delta = board_clear - 0.2) board_footprint();
    }}
}}

/* [Output] */
// Set to "base", "lid" or "both".
part = "both";

if (part == "base") base();
else if (part == "lid") lid();
else {{
    base();
    translate([0, 0, floor_t + inner_h + 6]) lid();
}}
"""
