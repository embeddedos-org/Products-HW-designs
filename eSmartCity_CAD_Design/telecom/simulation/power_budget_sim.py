#!/usr/bin/env python3
"""Power budget simulation for eIoT-GW Multi-Protocol IoT Gateway."""
components = {
    "NXP i.MX 8M Plus SoC": 4.5,
    "LPDDR4X x2": 2 * 0.3,
    "eMMC": 0.2,
    "LoRaWAN SoC": 0.044,
    "BLE + Zigbee SoC": 0.018,
    "4G LTE module": 1.5,
    "GbE PHY x2": 2 * 0.18,
    "RS-485 transceiver": 0.01,
}
total = sum(components.values())
print("=" * 55)
print("eIoT-GW Multi-Protocol Gateway — Power Budget")
print("=" * 55)
for name, w in components.items():
    print(f"{name:<40} {w:>6.3f} W")
print("-" * 55)
print(f"{'TOTAL':<40} {total:>6.3f} W")
print(f"12V input current: {total/12*1000:.0f} mA")
