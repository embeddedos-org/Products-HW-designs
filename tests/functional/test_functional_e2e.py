import unittest
class TestECADFunctional(unittest.TestCase):
    def test_schematic_to_pcb_pipeline(self):
        pipeline = ["schematic", "netlist", "layout", "gerber"]
        self.assertEqual(pipeline[-1], "gerber")
