# eBuild Simulation — EoS Health Hardware Stack
> **Purpose:** Pre-silicon validation, EoS stack integration testing, and hardware-in-the-loop (HIL) simulation for all four EoS Health devices
> **Status:** Framework ready | Physical hardware integration: Q4 2026

---

## What is eBuild?

**eBuild** is the EmbeddedOS build and simulation framework that enables:

1. **Pre-silicon validation** — Test firmware algorithms against synthetic and clinical reference datasets before physical prototypes are manufactured
2. **EoS stack integration testing** — Validate the full stack: firmware → BLE → cloud API → mobile app → dashboard, all in a simulated environment
3. **Hardware-in-the-loop (HIL)** — Connect physical sensor boards to QEMU/Renode-emulated MCUs for mixed-signal testing
4. **Regression testing** — Run all 10 clinical validation study datasets against algorithm updates to catch regressions before deployment
5. **Cross-device protocol testing** — Simulate multi-device BLE mesh scenarios (all 4 EoS Health devices simultaneously)

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    eBuild Simulation Layer                   │
├──────────────┬──────────────┬──────────────┬────────────────┤
│  HEALTH-KEY  │  HEALTH-BAND │  HEALTH-RING │  HEALTH-LAB    │
│  ULTRA sim   │  Neuro sim   │  sim         │  sim           │
│  (QEMU nRF)  │  (QEMU nRF  │  (QEMU nRF)  │  (QEMU nRF)    │
│              │  + STM32)    │              │                │
├──────────────┴──────────────┴──────────────┴────────────────┤
│              Synthetic Sensor Data Generator                 │
│  (ECG, EEG, PPG, sEMG, GPS, bioimpedance, electrochemical)  │
├─────────────────────────────────────────────────────────────┤
│              BLE Mesh Simulator (Zephyr BT stack)            │
├─────────────────────────────────────────────────────────────┤
│              EoS Health Cloud API (local mock)               │
├─────────────────────────────────────────────────────────────┤
│              EoS Health Mobile App (React Native / Flutter)  │
└─────────────────────────────────────────────────────────────┘
```

---

## Quick Start

### Prerequisites

```bash
# Install eBuild dependencies
sudo apt-get install -y qemu-system-arm renode python3-pip cmake ninja-build

# Install Python simulation dependencies
pip3 install numpy scipy matplotlib pandas pyserial bleak

# Install Zephyr SDK (for firmware builds)
wget https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v0.16.8/zephyr-sdk-0.16.8_linux-x86_64.tar.xz
tar xf zephyr-sdk-0.16.8_linux-x86_64.tar.xz
cd zephyr-sdk-0.16.8 && ./setup.sh

# Clone eos-health firmware
git clone https://github.com/embeddedos-org/eos-health.git
cd eos-health && west init && west update
```

### Run the Full EoS Stack Simulation

```bash
# From eosHealth_CAD_Design/ebuild_simulation/
python3 eos_stack_sim.py --devices all --duration 3600 --output ./results/

# Run a single device
python3 eos_stack_sim.py --devices health-ring --duration 300

# Run with clinical reference dataset
python3 eos_stack_sim.py --devices health-lab --dataset clinical/glucose_study_EOS-CL-003.csv

# Run regression test suite
python3 eos_stack_sim.py --mode regression --dataset all
```

---

## Device Simulation Models

### HEALTH-KEY ULTRA (`device_models/health_key_ultra.py`)

Simulates:
- MAX86141 PPG sensor output (synthetic waveforms with configurable HR, SpO₂, motion artifacts)
- AD5940 bioimpedance measurements (hydration level simulation)
- MAX30208 temperature sensor (circadian rhythm model)
- BMI270 IMU (activity classification: sedentary, walking, running, cycling)
- ATECC608B crypto operations (health data signing simulation)
- BLE 5.3 advertisement and GATT profile

```python
from device_models.health_key_ultra import HealthKeyUltraSim

sim = HealthKeyUltraSim(
    heart_rate=72,          # bpm
    spo2=98,                # %
    temperature=36.8,       # °C
    activity="walking",     # sedentary | walking | running | cycling
    motion_artifact=0.1,    # 0.0 = clean, 1.0 = maximum artifact
)
data = sim.generate(duration_seconds=60, sample_rate=25)
```

### HEALTH-BAND Neuro (`device_models/health_band_neuro.py`)

Simulates:
- ADS1293 ECG (12 pre-loaded ECG morphologies: normal sinus, AFib, PVCs, ST elevation, LBBB, etc.)
- ADS1299 EEG (alpha, beta, theta, delta band synthesis; seizure simulation)
- AD8232 sEMG (12 gesture classes, fatigue model)
- u-blox M10 GPS (route playback from GPX files)
- TENS output waveform verification

```python
from device_models.health_band_neuro import HealthBandNeuroSim

sim = HealthBandNeuroSim(
    ecg_morphology="normal_sinus",   # normal_sinus | afib | pvc | st_elevation
    eeg_state="relaxed",             # relaxed | focused | drowsy | seizure
    gesture="fist",                  # open | fist | pinch | point | wave | rest
    gps_route="routes/boston_5k.gpx"
)
ecg_data = sim.ecg.generate(duration_seconds=30, sample_rate=500)
eeg_data = sim.eeg.generate(duration_seconds=30, sample_rate=250)
```

### HEALTH-RING (`device_models/health_ring.py`)

Simulates:
- AS7058 PPG (HR, SpO₂, HRV, cNIBP from PTT model)
- HbA1c proxy (spectral ratio model with configurable glycemic state)
- Sleep staging (NREM1/2/3, REM cycle simulation over 8 hours)
- BMA456 accelerometer (sleep movement, step counting)

```python
from device_models.health_ring import HealthRingSim

sim = HealthRingSim(
    glycemic_state="normal",    # normal | pre_diabetic | diabetic
    sleep_quality="good",       # good | poor | insomnia
    blood_pressure=(120, 80),   # systolic, diastolic mmHg
)
ppg_data = sim.ppg.generate(duration_seconds=300, sample_rate=25)
sleep_data = sim.sleep.simulate_night(total_hours=8)
```

### HEALTH-LAB (`device_models/health_lab.py`)

Simulates:
- Glucose sensor (CGM trace with configurable meal events, insulin response)
- Cortisol sensor (diurnal rhythm, stress event injection)
- Electrolytes (Na⁺, K⁺ during exercise and hydration)
- Lactate (exercise intensity model, lactate threshold detection)
- pH sensor (sweat pH during exercise)
- Bioimpedance (hydration state model)

```python
from device_models.health_lab import HealthLabSim

sim = HealthLabSim(
    baseline_glucose=95,        # mg/dL fasting
    stress_level=0.3,           # 0.0 = calm, 1.0 = peak stress
    exercise_intensity=0.6,     # 0.0 = rest, 1.0 = max effort
)
# Simulate a full day with meals and exercise
day_data = sim.simulate_day(
    meals=[{"time": "08:00", "carbs_g": 60}, {"time": "13:00", "carbs_g": 80}],
    exercise=[{"time": "17:00", "duration_min": 45, "intensity": 0.7}]
)
```

---

## EoS Stack Integration Test Scenarios

### Scenario 1: Multi-Device BLE Pairing
Tests that all 4 devices can simultaneously pair with the EoS Health app via BLE 5.3 without interference.

```bash
python3 eos_stack_sim.py --scenario multi_device_pairing --devices all
```

### Scenario 2: Clinical Alert Pipeline
Tests that a simulated AFib event on HEALTH-BAND Neuro triggers a push notification within <30 seconds.

```bash
python3 eos_stack_sim.py --scenario clinical_alert --device health-band-neuro --event afib
```

### Scenario 3: OTA Firmware Update
Tests the MCUboot + SUIT OTA pipeline across all 4 devices simultaneously.

```bash
python3 eos_stack_sim.py --scenario ota_update --firmware ./builds/eos_health_v2.2.0.bin
```

### Scenario 4: Algorithm Regression
Runs all 10 clinical validation datasets against the current algorithm library and reports accuracy metrics.

```bash
python3 eos_stack_sim.py --scenario regression --datasets ./clinical_datasets/ --report ./results/regression_report.html
```

### Scenario 5: Power Budget Validation
Simulates 7-day battery life for each device and validates against specifications.

```bash
python3 eos_stack_sim.py --scenario power_budget --devices all --duration 604800
```

---

## Hardware-in-the-Loop (HIL) Setup

When physical development boards are available, eBuild supports HIL testing:

```
Physical Sensor Board ──UART/SPI──► nRF5340 DK ──USB──► eBuild HIL Bridge ──► QEMU EoS Stack
```

### Supported HIL Boards (Q4 2026)

| Device | Development Board | Interface |
|--------|------------------|-----------|
| HEALTH-KEY ULTRA | nRF5340 DK + MAX86141 eval board | SPI + I²C |
| HEALTH-BAND Neuro | nRF5340 DK + ADS1293 eval + ADS1299 eval | SPI + I²C |
| HEALTH-RING | nRF5340 DK + AS7058 eval board | I²C |
| HEALTH-LAB | nRF5340 DK + LMP91000 eval board | I²C |

---

## Integration with CI/CD

Add to your `.github/workflows/ci.yml`:

```yaml
- name: Run eBuild EoS Stack Simulation
  run: |
    python3 eosHealth_CAD_Design/ebuild_simulation/eos_stack_sim.py \
      --mode ci \
      --devices all \
      --duration 300 \
      --report ./artifacts/simulation_report.html
      
- name: Upload Simulation Report
  uses: actions/upload-artifact@v4
  with:
    name: eos-simulation-report
    path: ./artifacts/simulation_report.html
```

---

## Roadmap

| Milestone | Target | Description |
|-----------|--------|-------------|
| v1.0 — Sensor models | Q3 2026 | All 4 device simulation models complete |
| v1.1 — BLE stack | Q3 2026 | Full BLE GATT profile simulation |
| v1.2 — Cloud integration | Q4 2026 | EoS Health cloud API mock |
| v2.0 — HIL support | Q4 2026 | Physical board integration |
| v2.1 — Clinical datasets | Q1 2027 | 10 clinical study datasets integrated |
| v3.0 — Full EoS stack | Q2 2027 | Firmware + BLE + cloud + app + dashboard |

---

## Contributing

See [eos-health/CONTRIBUTING.md](https://github.com/embeddedos-org/eos-health/blob/main/CONTRIBUTING.md) for contribution guidelines.

All simulation models must include:
- Unit tests with >90% coverage
- Validation against at least one published clinical reference dataset
- Documentation of physiological model assumptions and limitations
