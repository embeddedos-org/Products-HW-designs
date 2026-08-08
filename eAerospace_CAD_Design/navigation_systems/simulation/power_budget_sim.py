#!/usr/bin/env python3
"""Power budget simulation for eINS-900 Inertial Navigation System."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "ADIS16505 IMU triad": 0.63,
    "Artix-7 IMU sampling FPGA": 0.95,
    "STM32H743 Kalman processor x2": 1.2,
    "ZED-F9P GNSS aiding": 0.135,
    "Barometer and magnetometer aiding": 0.06,
    "ARINC-429 / 1553B interfaces": 0.72,
    "Ethernet PHY and serial": 0.38,
    "Thermal control and housekeeping": 1.4,
}
BUS_V = 28
DCDC_EFFICIENCY = 0.86

total = sum(loads.values())
print("=" * 62)
print("eINS-900 Inertial Navigation System — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
