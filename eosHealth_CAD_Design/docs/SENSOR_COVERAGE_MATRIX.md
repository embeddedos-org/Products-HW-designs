# EoS Health — Sensor Coverage Matrix
> All health metrics monitored across the four-device ecosystem

| Health Metric | HEALTH-KEY ULTRA | HEALTH-BAND Neuro | HEALTH-RING | HEALTH-LAB | Method |
|--------------|:---:|:---:|:---:|:---:|--------|
| **Cardiovascular** | | | | | |
| Heart rate | ✅ | ✅ | ✅ | — | Optical PPG |
| Heart rate variability (HRV) | ✅ | ✅ | ✅ | — | PPG inter-beat interval |
| SpO₂ (blood oxygen) | ✅ | ✅ | ✅ | — | Red/IR PPG ratio |
| Blood pressure (cNIBP) | ✅ | — | ✅ | — | PTT from PPG |
| ECG (1-lead) | — | ✅ | — | — | ADS1293 |
| ECG (3-lead) | — | ✅ | — | — | ADS1293 Lead I/II/III |
| Atrial fibrillation detection | — | ✅ | ✅ | — | ECG + PPG algorithm |
| **Metabolic** | | | | | |
| Blood glucose trend (HbA1c proxy) | — | — | ✅ | — | NIR spectral ratio |
| Continuous glucose (CGM) | — | — | — | ✅ | GOx electrochemical |
| Lactate (exercise) | — | — | — | ✅ | LOx electrochemical |
| Cortisol (stress hormone) | — | — | — | ✅ | MIP electrochemical |
| **Hydration & Chemistry** | | | | | |
| Hydration (bioimpedance) | ✅ | — | — | ✅ | AD5940 bioZ |
| Sodium (Na⁺) | — | — | — | ✅ | ISE electrode |
| Potassium (K⁺) | — | — | — | ✅ | ISE electrode |
| Skin pH | — | — | — | ✅ | PANI electrode |
| **Neurological** | | | | | |
| EEG (4-channel) | — | ✅ | — | — | ADS1299 |
| Surface EMG (sEMG) | — | ✅ | — | — | AD8232 |
| Gesture recognition | — | ✅ | — | — | sEMG + TFLite |
| Stress score | ✅ | ✅ | ✅ | ✅ | HRV + EDA + cortisol |
| **Physical** | | | | | |
| Body temperature | ✅ | — | ✅ | — | Thermistor / MAX30208 |
| Steps / activity | ✅ | ✅ | ✅ | — | IMU (BMI270 / BMA456) |
| Sleep staging (NREM/REM) | — | — | ✅ | — | PPG + accel algorithm |
| Fall detection | ✅ | ✅ | — | — | IMU threshold |
| GPS location | — | ✅ | — | — | u-blox M10 |
| **Therapeutic** | | | | | |
| TENS therapy output | — | ✅ | — | — | IEC 60601-2-10 |
| **Security** | | | | | |
| Cryptographic health key | ✅ | — | — | — | ATECC608B ECDSA |

**Total unique metrics: 32**
**Metrics covered by 2+ devices (redundancy): 12**
