#!/usr/bin/env python3
"""Reference designator expansion, package geometry, and board placement.

Three jobs that have to agree with one another:

**Designator expansion.** A BOM line reading ``C1`` with quantity 180 cannot be
built. A board needs 180 distinct designators. This module allocates sequential
designators per prefix across a whole BOM, so ``C1`` qty 180 becomes ``C1-C180``
on the bill of materials and ``C1`` through ``C180`` on the board and netlist.
Without this the BOM, the netlist and the board can never be reconciled.

**Package geometry.** Body and courtyard dimensions are needed to answer whether
a board is physically large enough for the parts assigned to it. Chip passives
use their exact standard land patterns; everything else is estimated from the
package family and pin count.

**Placement.** A shelf-packing pass positions every part inside the board
outline. It is not an optimised layout — it exists to establish area
feasibility and to give the board file real, non-overlapping footprints.

Accuracy limits
---------------
Estimated package bodies are dimensionally plausible, not manufacturer-verified.
Only the chip-passive entries in ``EXACT_PACKAGES`` correspond to published land
patterns. Nothing here is an IPC-7351 land pattern, and pad geometry is
deliberately not emitted: a footprint with invented pads would look fabricable
and would not be. Use these for placement, area and clearance reasoning only.
"""

from __future__ import annotations

import re

# Chip passives and a few small packages whose dimensions are standard and
# known. Values are (body_x, body_y, courtyard_x, courtyard_y) in mm.
EXACT_PACKAGES = {
    "0201": (0.60, 0.30, 1.00, 0.60),
    "0402": (1.00, 0.50, 1.50, 0.90),
    "0805": (2.00, 1.25, 2.60, 1.70),
    "1210": (3.20, 2.50, 3.90, 3.00),
    "1812": (4.50, 3.20, 5.20, 3.80),
    "3921": (10.00, 5.30, 10.70, 6.00),
    "2016": (2.00, 1.60, 2.60, 2.20),
    "SMB": (4.57, 3.94, 5.30, 4.60),
    "SOIC8": (4.90, 3.90, 6.60, 5.40),
    "SOIC16": (9.90, 3.90, 11.60, 5.40),
    "SOIC20W": (12.80, 7.50, 14.50, 10.60),
    "SOT23-8": (2.90, 1.60, 4.20, 3.10),
    "TSSOP24": (7.80, 4.40, 9.20, 6.40),
    "TSSOP28": (9.70, 4.40, 11.10, 6.40),
    "VSSOP8": (3.00, 3.00, 4.20, 4.60),
    "VSSOP10": (3.00, 3.00, 4.20, 4.60),
    "WSON6": (2.00, 2.00, 2.60, 2.60),
    "WSON8": (6.00, 5.00, 6.60, 5.60),
    "UDFN8": (2.00, 3.00, 2.60, 3.60),
    "USON10": (2.00, 3.00, 2.60, 3.60),
    "DFN4": (1.50, 1.50, 2.10, 2.10),
    "DFN6": (2.00, 2.00, 2.60, 2.60),
    "TO-247": (16.00, 21.00, 17.00, 22.00),
    "TO-247-4": (16.00, 21.00, 17.00, 22.00),
    "TO-39": (9.40, 9.40, 10.20, 10.20),
    "TO-46": (5.40, 5.40, 6.20, 6.20),
}

# Typical lead pitch by package family, used to estimate a body from pin count.
FAMILY_PITCH = {
    "qfp": 0.50,
    "qfn": 0.50,
    "bga": 1.00,
    "lga": 0.80,
    "plcc": 1.27,
    "cqfp": 0.64,
    "lcc": 1.00,
}

# Fallbacks for packages with no pin count and no standard size, in mm.
GENERIC_PACKAGES = {
    "module": (25.0, 20.0),
    "custom": (20.0, 15.0),
    "so-dimm": (69.6, 30.0),
    "m.2": (22.0, 42.0),
    "butterfly": (20.0, 12.5),
    "vpx": (16.0, 10.0),
    "rack": (60.0, 40.0),
    "circular": (25.0, 25.0),
    "m12": (18.0, 18.0),
    "edge mount": (9.0, 6.5),
    "press-fit": (14.0, 9.5),
    "smt": (9.0, 7.5),
    "tht": (16.0, 16.0),
    "radial": (10.0, 10.0),
    "coin 20mm": (20.0, 20.0),
    "18650": (18.6, 65.2),
    "a-size": (17.0, 50.0),
    "pouch": (40.0, 30.0),
    "socket": (12.0, 12.0),
    "patch 25mm": (25.0, 25.0),
    "flex": (30.0, 10.0),
    "sma": (9.0, 6.5),
    "din 35": (45.0, 75.0),
    "9x7mm": (9.0, 7.0),
    "5.3x5.3mm": (5.3, 5.3),
    "40mm": (40.0, 40.0),
}

COURTYARD_MARGIN = 0.25  # per side, mm


def package_model(footprint: str) -> dict:
    """Return body and courtyard dimensions for a footprint name.

    Chip passives resolve to their standard land pattern. Other packages are
    estimated from family and pin count. The returned ``exact`` flag says which
    happened, so a caller can report estimated geometry honestly.

    Args:
        footprint: The footprint string from the component library.

    Returns:
        A dict with ``body_x``, ``body_y``, ``court_x``, ``court_y``, ``pins``
        and ``exact``.

    Example:
        >>> package_model("0402")["exact"]
        True
        >>> package_model("LQFP144")["body_x"] > 15
        True
    """
    raw = (footprint or "").strip()
    key = raw.upper()

    if key in EXACT_PACKAGES:
        bx, by, cx, cy = EXACT_PACKAGES[key]
        return {"body_x": bx, "body_y": by, "court_x": cx, "court_y": cy,
                "pins": 0, "exact": True}

    pin_match = re.search(r"(\d{2,4})\s*$", key)
    pins = int(pin_match.group(1)) if pin_match else 0
    lowered = key.lower()

    family = None
    for name in ("cqfp", "plcc", "qfp", "qfn", "bga", "lga", "lcc"):
        if name in lowered:
            family = name
            break

    if family and pins >= 8:
        pitch = FAMILY_PITCH[family]
        if family in ("bga",):
            side = int(pins ** 0.5 + 0.999)
            body = (side - 1) * pitch + 3.0
            bx = by = round(body, 2)
        else:
            per_side = max(pins / 4.0, 2)
            body = (per_side - 1) * pitch + 2.5
            bx = by = round(body, 2)
    else:
        bx = by = None
        for token, (gx, gy) in GENERIC_PACKAGES.items():
            if token in lowered:
                bx, by = gx, gy
                break
        if bx is None:
            # Unrecognised package: assume a modest QFN-like body rather than
            # zero, and let the caller see exact=False.
            bx = by = 8.0

    return {
        "body_x": bx,
        "body_y": by,
        "court_x": round(bx + COURTYARD_MARGIN * 2, 2),
        "court_y": round(by + COURTYARD_MARGIN * 2, 2),
        "pins": pins,
        "exact": False,
    }


def _prefix(reference: str) -> str:
    """Return the alphabetic prefix of a reference designator.

    Args:
        reference: A designator such as ``C1`` or ``PCB1``.

    Returns:
        The leading letters, uppercased. Falls back to ``X`` when absent.

    Example:
        >>> _prefix("PCB1")
        'PCB'
        >>> _prefix("C12")
        'C'
    """
    match = re.match(r"([A-Za-z_]+)", reference.strip())
    return match.group(1).upper() if match else "X"


def expand_references(product: dict) -> list[dict]:
    """Allocate individual designators for every part in a product's BOM.

    Designators are numbered sequentially per prefix in BOM order, so a line
    with quantity N consumes N numbers. This is what makes the BOM, the netlist
    and the board reconcilable: all three derive from this one allocation.

    Args:
        product: A catalog product record with a ``bom`` list.

    Returns:
        One dict per BOM line, carrying ``part``, ``qty``, ``designators``
        (the individual names) and ``display`` (the range shown on the BOM).

    Raises:
        ValueError: If a quantity is not a positive integer.

    Example:
        >>> lines = expand_references({"bom": [
        ...     {"ref": "C1", "part": "c", "qty": 3},
        ...     {"ref": "U1", "part": "u", "qty": 1}]})
        >>> lines[0]["display"], lines[0]["designators"]
        ('C1-C3', ['C1', 'C2', 'C3'])
        >>> lines[1]["display"]
        'U1'
    """
    counters: dict[str, int] = {}
    lines = []
    for entry in product.get("bom", []):
        qty = entry.get("qty", 1)
        if not isinstance(qty, int) or qty <= 0:
            raise ValueError(f"quantity {qty!r} is not a positive integer")
        prefix = _prefix(str(entry["ref"]))
        start = counters.get(prefix, 0) + 1
        counters[prefix] = start + qty - 1
        designators = [f"{prefix}{start + i}" for i in range(qty)]
        display = designators[0] if qty == 1 else f"{designators[0]}-{designators[-1]}"
        lines.append({**entry, "qty": qty, "designators": designators, "display": display})
    return lines


def expand_display_reference(display: str) -> list[str]:
    """Expand a BOM display reference back into individual designators.

    Args:
        display: A designator or range such as ``C1`` or ``C1-C180``.

    Returns:
        The individual designators the range covers.

    Example:
        >>> expand_display_reference("C1-C4")
        ['C1', 'C2', 'C3', 'C4']
        >>> expand_display_reference("U7")
        ['U7']
    """
    text = display.strip()
    match = re.fullmatch(r"([A-Za-z_]+)(\d+)\s*-\s*([A-Za-z_]+)(\d+)", text)
    if not match:
        return [text] if text else []
    prefix, first, prefix2, last = match.groups()
    if prefix.upper() != prefix2.upper():
        return [text]
    return [f"{prefix}{n}" for n in range(int(first), int(last) + 1)]


def place_components(lines: list[dict], library: dict, geometry: dict) -> dict:
    """Position every component inside the board outline by shelf packing.

    Parts are sorted tallest-first and packed into rows, which is a reasonable
    area-feasibility test rather than an optimised layout. The usable area
    excludes a keep-out margin from the board edge.

    Args:
        lines: Output of expand_references().
        library: The component library.
        geometry: Board geometry from cad_render.board_geometry().

    Returns:
        A dict with ``placements`` (designator, x, y, courtyard size),
        ``placed``, ``overflow`` (parts that did not fit), ``used_area_mm2``,
        ``usable_area_mm2`` and ``utilisation``.

    Example:
        >>> lib = {"c": {"footprint": "0402"}}
        >>> g = {"shape": "rect", "width": 50.0, "height": 40.0}
        >>> r = place_components([{ "part": "c", "qty": 2,
        ...     "designators": ["C1", "C2"]}], lib, g)
        >>> r["placed"], r["overflow"]
        (2, [])
    """
    margin = 2.0
    if geometry["shape"] == "rect":
        usable_w = geometry["width"] - margin * 2
        usable_h = geometry["height"] - margin * 2
        origin_x = origin_y = margin
        usable_area = usable_w * usable_h
    else:
        # Treat a circular board as its inscribed square for packing purposes.
        side = (geometry["diameter"] - margin * 2) / (2 ** 0.5)
        usable_w = usable_h = side
        origin_x = origin_y = geometry["diameter"] / 2 - side / 2
        usable_area = 3.14159265 * (geometry["diameter"] / 2 - margin) ** 2

    items = []
    excluded = 0
    for line in lines:
        component = library[line["part"]]
        # Enclosures, battery packs, solar panels and the bare board itself are
        # part of the product but are not mounted on the PCB. Placing them would
        # make the area check meaningless -- most obviously the PCB, which would
        # otherwise be placed on top of itself.
        if component.get("assembly"):
            excluded += len(line["designators"])
            continue
        model = package_model(component["footprint"])
        for designator in line["designators"]:
            items.append((designator, model["court_x"], model["court_y"], model["exact"]))

    # Tallest first keeps shelves compact.
    items.sort(key=lambda item: (-item[2], -item[1]))

    placements = []
    overflow = []
    used_area = 0.0
    cursor_x, cursor_y, shelf_h = origin_x, origin_y, 0.0

    for designator, cx, cy, exact in items:
        if cx > usable_w or cy > usable_h:
            overflow.append(designator)
            continue
        if cursor_x + cx > origin_x + usable_w:
            cursor_x = origin_x
            cursor_y += shelf_h
            shelf_h = 0.0
        if cursor_y + cy > origin_y + usable_h:
            overflow.append(designator)
            continue
        placements.append(
            {"designator": designator, "x": round(cursor_x + cx / 2, 3),
             "y": round(cursor_y + cy / 2, 3), "court_x": cx, "court_y": cy,
             "exact": exact}
        )
        used_area += cx * cy
        cursor_x += cx
        shelf_h = max(shelf_h, cy)

    return {
        "placements": placements,
        "placed": len(placements),
        "excluded_assembly": excluded,
        "overflow": overflow,
        "used_area_mm2": round(used_area, 2),
        "usable_area_mm2": round(usable_area, 2),
        "utilisation": round(used_area / usable_area, 4) if usable_area else 0.0,
    }
