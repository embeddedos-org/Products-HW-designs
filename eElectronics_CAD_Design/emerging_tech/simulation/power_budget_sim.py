#!/usr/bin/env python3
"""Power budget simulation for eEdge-AI-Box."""
components = {
    "RK3588S SoC (AI workload)": 10.0,
    "LPDDR5 x4": 4 * 0.8,
    "NVMe SSD": 2.0,
    "2.5GbE controllers x2": 2 * 0.5,
    "USB-C PD controller": 0.05,
    "Board regulators": 0.5,
}
total = sum(components.values())
print("=" * 55)
print("eEdge-AI-Box — Power Budget")
print("=" * 55)
for name, w in components.items():
    print(f"{name:<40} {w:>6.3f} W")
print("-" * 55)
print(f"{'TOTAL':<40} {total:>6.3f} W")
print(f"12V input current: {total/12*1000:.0f} mA")
print(f"AI efficiency: {32/10:.1f} TOPS/W")
