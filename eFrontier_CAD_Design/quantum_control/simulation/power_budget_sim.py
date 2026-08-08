#!/usr/bin/env python3
"""Power budget simulation for eQC-1000 Quantum Control System."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "Zynq UltraScale+ sequencer": 18.0,
    "AD9265 readout digitiser x8": 9.6,
    "Arbitrary waveform output x16": 4.8,
    "HMC7044 clock tree x2": 2.2,
    "LMX2594 synthesiser x4": 2.8,
    "10MHz OCXO reference": 1.8,
    "LPDDR4 x4": 4.4,
    "Low-noise analogue supplies": 3.6,
}
BUS_V = 12
DCDC_EFFICIENCY = 0.88

total = sum(loads.values())
print("=" * 62)
print("eQC-1000 Quantum Control System — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
