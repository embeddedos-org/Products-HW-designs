#!/usr/bin/env python3
"""Power budget simulation for eGNSS-400 RTK Receiver."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "ZED-F9P GNSS engine (RTK active)": 0.135,
    "ECP5 interference monitor": 0.42,
    "STM32H743 fusion processor": 0.6,
    "ADIS16470 IMU": 0.21,
    "AD9265 IF digitiser": 1.2,
    "Active antenna LNA bias": 0.09,
    "USB PHY and CAN transceiver": 0.14,
    "Reference oscillator": 0.03,
}
BUS_V = 5
DCDC_EFFICIENCY = 0.9

total = sum(loads.values())
print("=" * 62)
print("eGNSS-400 RTK Receiver — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
