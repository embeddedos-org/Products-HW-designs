# HEALTH-BAND Neuro: Standalone Hardware Architecture

**Document Version:** 1.0
**Date:** May 2026
**Author:** Srikanth Patchava, Embedded Operating Systems Research Foundation (EoS)

---

## 1. System Overview

The HEALTH-BAND Neuro is a standalone wearable health tracker utilizing a flexible wristband form factor. It is distinct from the HEALTH-KEY ecosystem, operating independently with its own display, storage, and processing capabilities. The core design philosophy centers on the **Zero-Hole Architecture**, utilizing dual-purpose USB-C ports for all physical interfacing.

## 2. Core Processing and Connectivity

*   **Microcontroller (MCU):** Nordic Semiconductor nRF52840
    *   **Core:** ARM Cortex-M4F at 64MHz
    *   **Wireless:** Bluetooth Low Energy (BLE) 5.3
    *   **Wired:** USB 2.0 Full Speed (FS) Device Controller
    *   **Role:** Acts as the central hub, managing all sensor data acquisition, display rendering, local storage I/O, and BLE communications.

## 3. Power Management and Clasp Architecture

The physical clasp of the band is functional, forming the basis of the power and data routing system.

*   **Left End (Female):** USB-C Female Receptacle.
    *   Functions as the primary charging input.
    *   The physical housing around this port includes the micro-perforated grille for breath analysis.
*   **Right End (Male):** USB-C Male Plug.
    *   Inserts into the female receptacle to secure the band.
    *   Functions as a data output (USB MSC) when connected to a PC.
    *   Functions as a power output for pass-through charging.
*   **Battery:** 200mAh Lithium-Polymer (Li-Po) cell, embedded within the flexible band structure.
*   **PMIC:** Texas Instruments BQ25185 (or similar highly integrated wearable PMIC).
    *   Manages battery charging from the USB-C female port.
    *   Handles power routing for pass-through charging when the band acts as an inline cable.

## 4. User Interface

### 4.1 V1 Hardware: Micro OLED

*   **Display Panel:** 0.49-inch monochrome Micro OLED (e.g., Sony SSD1306 controller).
*   **Resolution:** 128 x 64 pixels.
*   **Integration:** Flush-mounted into the outer carbon fiber surface, protected by a scratch-resistant sapphire or hardened glass window perfectly leveled with the band.
*   **Functionality:** Displays real-time metrics (Time, HR, SpO2, BAC, Steps, BLE Status).

### 4.2 Future Hardware (CIP Claim): Holographic Micro-LED

*   **Concept:** A flexible micro-LED array positioned behind a holographic diffuser film.
*   **Visual Effect:** Iridescent, floating text appearing directly on the band surface without a defined screen bezel.

## 5. Local Storage

*   **Memory:** Winbond W25N512GV (64GB NAND Flash).
*   **Interface:** SPI/QSPI to the nRF52840.
*   **Functionality:** Stores encrypted health logs, raw ECG data, and BAC history.
*   **Access:** When the USB-C male plug is connected to a computer, the nRF52840 enumerates as a USB Mass Storage Class (MSC) device, allowing direct file access.

## 6. Sensor Subsystems

### 6.1 Optical and Biometric (Inner Surface)
*   **MAX30101:** Integrated pulse oximetry and heart rate monitor module. Also serves as a multi-color status LED visible through the inner surface when unclasped.
*   **OPA391 (ECG):** High-precision operational amplifier forming the analog front-end for electrocardiogram readings.
*   **TI AS6221:** High-accuracy digital skin temperature sensor.

### 6.2 Neuromuscular Interface (Inner Surface)
*   **Electrodes:** Six platinum dots flush with the inner strap.
*   **sEMG (Input):** Analog front-end to detect surface electromyography signals for gesture recognition.
*   **TENS (Output):** Integrated boost converter and H-bridge to deliver Transcutaneous Electrical Nerve Stimulation pulses through the same electrodes.

### 6.3 Breath Analysis (Left Port Housing)
*   **Dart EC4-10-100:** Electrochemical fuel cell for highly accurate Blood Alcohol Content (BAC) measurement.
*   **Sensirion SGP40:** MOx sensor for Volatile Organic Compounds (VOC) and ketosis tracking.
*   **Integration:** Housed behind a hexagonal titanium grille and PTFE hydrophobic membrane surrounding the USB-C female port.

### 6.4 Environmental and Motion
*   **Bosch BMI270:** 6-axis Inertial Measurement Unit (IMU) for step tracking, sleep staging, and tremor detection.
*   **Vishay VEML6075:** UV A/B light sensor mounted on the outer surface.
