# Diagnostic Equipment — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-06-03 | **Status:** Design Phase

## Product Overview
Medical-grade diagnostic equipment suite: 12-lead ECG, 32-channel EEG, portable ultrasound, multi-parameter patient monitor, and blood analyzer — all running eOS Medical.

## Product Family

| Model | Function | Channels | Connectivity |
|---|---|---|---|
| eECG-12 | 12-lead ECG | 12 | BLE 5.3, USB-C, Wi-Fi |
| eEEG-32 | 32-channel EEG | 32 | USB-C, BLE |
| eUS-Pro | Portable Ultrasound | — | Wi-Fi, USB-C |
| ePM-500 | Patient Monitor | 8 params | Ethernet, BLE, Wi-Fi |
| eBA-100 | Blood Analyzer | — | USB-C, LAN |

## Electrical Specifications — eECG-12
| Parameter | Specification |
|---|---|
| **MCU** | STM32H7B3ZIT6 ARM Cortex-M7 @ 280MHz |
| **AFE** | Texas Instruments ADS1298 (8-ch 24-bit ECG AFE) |
| **Display** | 7" TFT IPS 1024×600, capacitive touch |
| **Wireless** | BLE 5.3 (nRF5340), Wi-Fi 6 (ESP32-S3) |
| **Battery** | 7.4V LiPo 5000mAh, 8h operation |
| **Safety** | IEC 60601-1 Class II BF applied part |
| **CMRR** | >110 dB |
| **Input impedance** | >10 GΩ |
| **Resolution** | 24-bit, 0.5µV LSB |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 6 |
| **Dimensions** | 150mm × 100mm |
| **IPC Class** | Class 3 Medical |
| **Isolation** | 4kV patient isolation barrier |
