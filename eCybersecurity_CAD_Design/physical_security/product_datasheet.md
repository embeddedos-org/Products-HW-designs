# Physical Security — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-06-03 | **Status:** Design Phase

## Product Family

| Model | Type | Standard |
|---|---|---|
| eAccess-Pro | Smart access control panel | FIPS 201-3, OSDP v2 |
| eBioLock | Biometric smart lock | ISO/IEC 19794 |
| ePerim-Radar | Perimeter radar sensor | MIL-STD-810 |
| eSecurity-Cam | AI security camera | IEC 62676-1 |
| eIntruder-Det | Intrusion detection system | EN 50131-1 |

## Electrical Specifications — eAccess-Pro
| Parameter | Specification |
|---|---|
| **MCU** | STM32H7B3 |
| **Reader** | OSDP v2, Wiegand, RS-485 |
| **Credentials** | MIFARE DESFire EV3, HID iCLASS, BLE |
| **Connectivity** | Ethernet, RS-485, Wi-Fi |
| **Power** | PoE+ (802.3at), 12VDC |
| **Tamper** | Cover + wall tamper detection |
