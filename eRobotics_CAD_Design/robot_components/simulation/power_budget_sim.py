#!/usr/bin/env python3
"""Power budget simulation for eServo-200 EtherCAT Servo Drive."""
components = {
    "STM32G474 MCU (FOC)": 0.08,
    "Lattice ECP5 FPGA": 0.5,
    "MOSFET gate driver": 0.02,
    "Current sense amp": 0.001,
    "GbE PHY (EtherCAT)": 0.18,
    "LDO regulator": 0.01,
}
total_electronics = sum(components.values())
motor_power_W = 200  # rated
efficiency = 0.95
input_power = motor_power_W / efficiency
print("=" * 55)
print("eServo-200 EtherCAT Servo Drive — Power Budget")
print("=" * 55)
for name, w in components.items():
    print(f"{name:<40} {w:>6.3f} W")
print("-" * 55)
print(f"{'TOTAL (electronics)':<40} {total_electronics:>6.3f} W")
print(f"Motor rated power: {motor_power_W} W")
print(f"Input power @ {efficiency*100:.0f}% efficiency: {input_power:.1f} W")
print(f"48V bus current @ rated: {input_power/48*1000:.0f} mA")
