"""
tests/unit/test_unit_core.py — Comprehensive eCAD unit tests
SPDX-License-Identifier: MIT  Copyright (c) 2026 EmbeddedOS Foundation
"""
import math
import unittest


# ---------------------------------------------------------------------------
# Netlist & Connectivity
# ---------------------------------------------------------------------------
class Netlist:
    def __init__(self):
        self._nets = {}  # net_name -> list of pins

    def add_net(self, name, pins):
        self._nets[name] = list(pins)

    def get_pins(self, name):
        return self._nets.get(name, [])

    def is_connected(self, pin1, pin2):
        for pins in self._nets.values():
            if pin1 in pins and pin2 in pins:
                return True
        return False

    def net_count(self):
        return len(self._nets)

    def dangling_nets(self):
        return [n for n, pins in self._nets.items() if len(pins) < 2]


class TestNetlist(unittest.TestCase):
    def setUp(self):
        self.nl = Netlist()
        self.nl.add_net("VCC", ["U1.VCC", "C1.P", "C2.P"])
        self.nl.add_net("GND", ["U1.GND", "C1.N", "C2.N", "R1.2"])
        self.nl.add_net("SDA", ["U1.PA0", "J1.2"])
        self.nl.add_net("FLOATING", ["U2.NC"])

    def test_netlist_connectivity(self):
        self.assertTrue(self.nl.is_connected("U1.VCC", "C1.P"))

    def test_not_connected_across_nets(self):
        self.assertFalse(self.nl.is_connected("U1.VCC", "U1.GND"))

    def test_net_count(self):
        self.assertEqual(self.nl.net_count(), 4)

    def test_dangling_net(self):
        dangling = self.nl.dangling_nets()
        self.assertIn("FLOATING", dangling)

    def test_gnd_pins(self):
        pins = self.nl.get_pins("GND")
        self.assertIn("U1.GND", pins)
        self.assertEqual(len(pins), 4)


# ---------------------------------------------------------------------------
# PCB Design Rule Check (DRC)
# ---------------------------------------------------------------------------
class DRCChecker:
    MIN_TRACE_WIDTH_MM = 0.2
    MIN_CLEARANCE_MM = 0.15
    MIN_VIA_DRILL_MM = 0.3

    def check_trace_width(self, width_mm):
        return width_mm >= self.MIN_TRACE_WIDTH_MM

    def check_clearance(self, gap_mm):
        return gap_mm >= self.MIN_CLEARANCE_MM

    def check_via_drill(self, drill_mm):
        return drill_mm >= self.MIN_VIA_DRILL_MM

    def check_all(self, trace_w, clearance, via_drill):
        return (
            self.check_trace_width(trace_w)
            and self.check_clearance(clearance)
            and self.check_via_drill(via_drill)
        )


class TestDRC(unittest.TestCase):
    def setUp(self):
        self.drc = DRCChecker()

    def test_trace_width_pass(self):
        self.assertTrue(self.drc.check_trace_width(0.25))

    def test_trace_width_fail(self):
        self.assertFalse(self.drc.check_trace_width(0.1))

    def test_clearance_pass(self):
        self.assertTrue(self.drc.check_clearance(0.2))

    def test_clearance_fail(self):
        self.assertFalse(self.drc.check_clearance(0.1))

    def test_via_drill_pass(self):
        self.assertTrue(self.drc.check_via_drill(0.4))

    def test_via_drill_fail(self):
        self.assertFalse(self.drc.check_via_drill(0.2))

    def test_check_all_pass(self):
        self.assertTrue(self.drc.check_all(0.3, 0.2, 0.4))

    def test_check_all_fail_one(self):
        self.assertFalse(self.drc.check_all(0.1, 0.2, 0.4))


# ---------------------------------------------------------------------------
# Bill of Materials (BOM)
# ---------------------------------------------------------------------------
class BOM:
    def __init__(self):
        self._items = []

    def add(self, ref, value, footprint, qty=1):
        self._items.append({"ref": ref, "value": value, "footprint": footprint, "qty": qty})

    def total_components(self):
        return sum(i["qty"] for i in self._items)

    def by_value(self, value):
        return [i for i in self._items if i["value"] == value]

    def unique_footprints(self):
        return set(i["footprint"] for i in self._items)


class TestBOM(unittest.TestCase):
    def setUp(self):
        self.bom = BOM()
        self.bom.add("R1", "10k", "0402", 1)
        self.bom.add("R2", "10k", "0402", 1)
        self.bom.add("C1", "100nF", "0402", 2)
        self.bom.add("U1", "STM32F4", "LQFP64", 1)

    def test_total_components(self):
        self.assertEqual(self.bom.total_components(), 5)

    def test_by_value(self):
        resistors = self.bom.by_value("10k")
        self.assertEqual(len(resistors), 2)

    def test_unique_footprints(self):
        fps = self.bom.unique_footprints()
        self.assertIn("0402", fps)
        self.assertIn("LQFP64", fps)
        self.assertEqual(len(fps), 2)


# ---------------------------------------------------------------------------
# Impedance calculations
# ---------------------------------------------------------------------------
class TestImpedance(unittest.TestCase):
    def test_microstrip_impedance_approx(self):
        """Approximate microstrip impedance Z0 for 50-ohm target."""
        # Simplified formula: Z0 ≈ 87/sqrt(er+1.41) * ln(5.98*h/(0.8*w+t))
        er = 4.4  # FR4
        h = 1.6   # mm substrate height
        w = 3.0   # mm trace width
        t = 0.035 # mm copper thickness
        Z0 = (87 / math.sqrt(er + 1.41)) * math.log(5.98 * h / (0.8 * w + t))
        self.assertGreater(Z0, 30)
        self.assertLess(Z0, 120)

    def test_capacitor_reactance(self):
        """Xc = 1 / (2*pi*f*C)"""
        f = 1e6  # 1 MHz
        C = 100e-9  # 100 nF
        Xc = 1 / (2 * math.pi * f * C)
        self.assertAlmostEqual(Xc, 1.592, places=2)

    def test_inductor_reactance(self):
        """Xl = 2*pi*f*L"""
        f = 1e6
        L = 10e-6  # 10 uH
        Xl = 2 * math.pi * f * L
        self.assertAlmostEqual(Xl, 62.83, places=1)


if __name__ == "__main__":
    unittest.main()
