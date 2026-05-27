import unittest

class TesteCAD-Hardware-ProductsSimulation(unittest.TestCase):
    def test_thermal_dissipation_simulation(self):
        # Simulate thermal dissipation profile of a voltage regulator (LDO)
        ambient_temp = 25.0
        power_dissipated = 1.5 # Watts
        thermal_resistance = 40.0 # °C/W
        junction_temp = ambient_temp + (power_dissipated * thermal_resistance)
        assert junction_temp == 85.0, "Thermal dissipation simulation incorrect"
