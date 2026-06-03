#!/usr/bin/env python3
"""Power budget simulation for eSolarInv-10kW Solar Inverter."""
rated_power = 10000  # W
efficiency = 0.986
losses = rated_power * (1 - efficiency)
components = {
    "STM32H7B3 MCU x2": 2 * 0.12,
    "TMS320F28379D DSP": 0.5,
    "SiC MOSFET switching losses": losses * 0.4,
    "SiC MOSFET conduction losses": losses * 0.3,
    "Magnetics (inductor/transformer)": losses * 0.2,
    "Gate drivers x6": 6 * 0.05,
    "Current sensors x4": 4 * 0.01,
    "Wi-Fi module": 0.25,
    "4G LTE module": 1.5,
    "Cooling fan": 15.0,
}
total = sum(components.values())
print("=" * 55)
print(f"eSolarInv-10kW Solar Inverter — Power Loss Budget")
print("=" * 55)
for name, w in components.items():
    print(f"{name:<45} {w:>6.1f} W")
print("-" * 55)
print(f"{'TOTAL losses':<45} {total:>6.1f} W")
print(f"Efficiency: {(1 - total/rated_power)*100:.2f}%")
