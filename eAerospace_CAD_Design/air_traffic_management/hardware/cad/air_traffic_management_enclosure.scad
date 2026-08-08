// Air Traffic Management Systems — parametric enclosure
// Part: eATM-3000
//
// Generated from tools/catalog. Sized to the board outline in the datasheet.
// Connector and control cut-outs are NOT included: their positions depend on a
// placed layout, which does not exist yet. Add them once placement is fixed.
//
// Render:  openscad -o enclosure.stl air_traffic_management_enclosure.scad

/* [Enclosure] */
wall           = 2.4;   // wall thickness, mm
floor_t        = 2.0;   // floor thickness, mm
board_clear    = 1.5;   // clearance around the board edge, mm
standoff_h     = 6.0;   // board standoff height above the floor, mm
headroom       = 14.0;  // clear height above the board, mm
mount_inset    = 5.0;   // board mounting hole inset, mm
screw_d        = 2.6;   // self-tapping screw pilot diameter, mm
standoff_d     = 6.0;   // standoff outer diameter, mm
corner_r       = 3.0;   // external corner radius, mm
lid_lip        = 1.2;   // lid register lip depth, mm

$fn = 64;

board_w = 260.0;   // board width, mm
board_h = 180.0;   // board depth, mm

module board_footprint(inflate = 0) {
    square([board_w + inflate * 2, board_h + inflate * 2], center = true);
}

module standoff_positions() {
    for (sx = [-1, 1], sy = [-1, 1])
        translate([sx * (board_w / 2 - mount_inset),
                   sy * (board_h / 2 - mount_inset), 0]) children();
}

inner_h = standoff_h + headroom;

module shell() {
    difference() {
        // Outer body, offset out from the board footprint by clearance + wall.
        linear_extrude(height = floor_t + inner_h)
            offset(r = corner_r) offset(delta = -corner_r)
                offset(delta = board_clear + wall) board_footprint();

        // Internal cavity.
        translate([0, 0, floor_t])
            linear_extrude(height = inner_h + 1)
                offset(delta = board_clear) board_footprint();
    }
}

module standoffs() {
    standoff_positions()
        difference() {
            cylinder(d = standoff_d, h = floor_t + standoff_h);
            translate([0, 0, floor_t])
                cylinder(d = screw_d, h = standoff_h + 1);
        }
}

module base() {
    union() {
        shell();
        standoffs();
    }
}

module lid() {
    union() {
        // Lid plate.
        linear_extrude(height = wall)
            offset(r = corner_r) offset(delta = -corner_r)
                offset(delta = board_clear + wall) board_footprint();

        // Register lip that drops into the cavity.
        translate([0, 0, -lid_lip])
            linear_extrude(height = lid_lip)
                offset(delta = board_clear - 0.2) board_footprint();
    }
}

/* [Output] */
// Set to "base", "lid" or "both".
part = "both";

if (part == "base") base();
else if (part == "lid") lid();
else {
    base();
    translate([0, 0, floor_t + inner_h + 6]) lid();
}
