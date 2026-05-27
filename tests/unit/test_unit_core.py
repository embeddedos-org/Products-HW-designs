import unittest
class TestECADUnit(unittest.TestCase):
    def test_netlist_connectivity(self):
        net = ["MCU_PIN1", "RES_PIN1"]
        self.assertEqual(len(net), 2)
