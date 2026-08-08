#!/usr/bin/env python3
"""Power budget simulation for eLV-500 Launch Vehicle Avionics."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "GR712RC GNC processor": 3.2,
    "Artix-7 sequencing FPGA": 1.8,
    "AFTS processor pair": 1.2,
    "ADIS16505 IMU triad": 0.63,
    "ZED-F9P GNSS x2": 0.27,
    "S-band telemetry transmitter": 12.0,
    "Pyro isolation drivers": 0.8,
    "Telemetry and housekeeping": 0.45,
}
BUS_V = 28
DCDC_EFFICIENCY = 0.85

total = sum(loads.values())
print("=" * 62)
print("eLV-500 Launch Vehicle Avionics — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
