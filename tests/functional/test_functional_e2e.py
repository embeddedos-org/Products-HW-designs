import unittest

class TesteCAD-Hardware-ProductsFunctional(unittest.TestCase):
    def test_pcb_clearance_rule_check_pipeline(self):
        traces = [{"net": "3V3", "x": 10.0, "y": 10.0}, {"net": "GND", "x": 10.1, "y": 10.0}]
        # Clearance check (min 0.2mm required)
        import math
        dist = math.sqrt((traces[0]["x"] - traces[1]["x"])**2 + (traces[0]["y"] - traces[1]["y"])**2)
        clearance_violation = dist < 0.2
        assert clearance_violation, "PCB clearance check pipeline failed to flag 0.1mm violation"
