# eRadar360 — Legal and Policy Package
**Document:** EOS-RADAR-LEGAL-001 | **Revision:** 1.0 | **Date:** 2026-06-03
**Note:** All documents in this package are drafts requiring review by qualified legal counsel before publication.

---

## Section 1: Terms of Service

**Last Updated:** 2026-06-03 | **Effective Date:** Upon product launch

### 1.1 Acceptance of Terms

By purchasing, installing, or using the eRadar360 device or its companion mobile application ("Service"), you agree to be bound by these Terms of Service ("Terms"). If you do not agree to these Terms, do not use the Service.

### 1.2 Legal Use Only

The eRadar360 is a driver information and alert system. You are solely responsible for ensuring that your use of the eRadar360 complies with all applicable federal, state, provincial, and local laws. **Radar detectors are illegal in Virginia, Washington DC, and all Canadian provinces.** EmbeddedOS Inc. expressly disclaims all liability for any fines, penalties, or legal consequences arising from use of the eRadar360 in jurisdictions where such devices are prohibited.

### 1.3 Driver Responsibility

The eRadar360 is a supplementary information tool only. It does not control your vehicle, does not replace attentive driving, and does not guarantee detection of all speed enforcement or safety threats. You remain solely responsible for operating your vehicle safely and in compliance with all traffic laws at all times. EmbeddedOS Inc. is not liable for any accident, injury, citation, or loss arising from reliance on eRadar360 alerts or the absence thereof.

### 1.4 Limitation of Liability

TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW, EMBEDDEDOS INC. AND ITS AFFILIATES SHALL NOT BE LIABLE FOR ANY INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL, OR PUNITIVE DAMAGES, INCLUDING BUT NOT LIMITED TO LOSS OF LIFE, PERSONAL INJURY, PROPERTY DAMAGE, TRAFFIC CITATIONS, OR LOSS OF REVENUE, ARISING OUT OF OR IN CONNECTION WITH THE USE OR INABILITY TO USE THE ERADAR360 OR ITS COMPANION APPLICATION, EVEN IF EMBEDDEDOS INC. HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. IN NO EVENT SHALL EMBEDDEDOS INC.'S TOTAL LIABILITY EXCEED THE PURCHASE PRICE OF THE DEVICE.

### 1.5 OTA Updates

EmbeddedOS Inc. may deliver over-the-air (OTA) firmware updates to the eRadar360. Updates are delivered via cryptographically signed packages and may add, modify, or remove features. You consent to the automatic installation of security updates. Feature updates may be deferred via the mobile application settings.

### 1.6 Governing Law

These Terms are governed by the laws of the State of Delaware, USA, without regard to conflict of law principles.

---

## Section 2: Privacy Policy

**Last Updated:** 2026-06-03

### 2.1 Data Collected

EmbeddedOS Inc. collects the following data through the eRadar360 device and companion application:

| Data Type | Purpose | Retention | Shared With |
|-----------|---------|-----------|------------|
| GPS location (real-time) | Alert generation, threat database updates | Session only (not stored) | Not shared |
| GPS location (aggregated, anonymized) | Speed camera database crowdsourcing | 90 days | Not shared externally |
| OBD-II vehicle speed | Alert calibration, trip logging | 30 days (local device only) | Not shared |
| Device diagnostics | Crash reporting, firmware updates | 90 days | Crash reporting service |
| App usage analytics | Product improvement | 12 months | Analytics provider (anonymized) |
| Account information (email, name) | Account management | Until account deletion | Not shared |

### 2.2 Data Not Collected

EmbeddedOS Inc. does **not** collect: precise real-time location stored on servers, vehicle identification number (VIN), driver identity linked to location, health or biometric data, or financial information.

### 2.3 V2X Data

V2X messages (BSM, TIM, SPaT) transmitted by the eRadar360 use a rotating pseudonymous identifier per IEEE 1609.2. No personally identifiable information is included in V2X transmissions. V2X messages received from other vehicles are processed locally and not transmitted to EmbeddedOS servers.

### 2.4 GDPR Rights (EU Users)

EU users have the right to access, rectify, erase, restrict processing of, and port their personal data. To exercise these rights, contact privacy@embeddedos.com. EmbeddedOS Inc. will respond within 30 days.

### 2.5 CCPA Rights (California Users)

California residents have the right to know what personal information is collected, to delete personal information, and to opt out of the sale of personal information. EmbeddedOS Inc. does not sell personal information.

---

## Section 3: End User License Agreement (EULA)

**Last Updated:** 2026-06-03

### 3.1 License Grant

Subject to the terms of this EULA, EmbeddedOS Inc. grants you a limited, non-exclusive, non-transferable license to use the eRadar360 firmware and companion application for personal, non-commercial use.

### 3.2 Restrictions

You may not: reverse engineer, decompile, or disassemble the firmware or application; modify, adapt, or create derivative works; distribute, sell, or sublicense the software; use the software for any unlawful purpose; or attempt to circumvent any security or authentication mechanism.

### 3.3 Intellectual Property

The eRadar360 firmware, AI models, radar signature database, and companion application are proprietary to EmbeddedOS Inc. and protected by US and international intellectual property laws. All rights not expressly granted are reserved.

### 3.4 Warranty Disclaimer

THE ERADAR360 FIRMWARE AND APPLICATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND. EMBEDDEDOS INC. DOES NOT WARRANT THAT THE SOFTWARE WILL BE ERROR-FREE, THAT ALERTS WILL BE GENERATED FOR ALL THREATS, OR THAT THE DEVICE WILL OPERATE WITHOUT INTERRUPTION.

---

## Section 4: FTC Marketing Claims Policy

All public-facing marketing claims for the eRadar360 must be substantiated with the following evidence before publication:

| Claim | Required Evidence | Evidence Status |
|-------|------------------|----------------|
| "97% false alert suppression" | Controlled test: ≥1,000 non-threat events, ≥97% correctly suppressed | Simulation: ✅ | Physical test: Pending |
| "<50ms laser alert latency" | Bench test: ≥100 laser pulses, P95 latency <50ms | Simulation: ✅ | Physical test: Pending |
| "1km V2X range" | Field test: ≥50 BSM exchanges at 1km LOS | Simulation: ✅ | Field test: Pending |
| "360° laser coverage" | Bench test: laser gun at 72° intervals, all 5 sensors detect | Simulation: ✅ | Physical test: Pending |
| "Detects all radar bands (Ka/K/X)" | Bench test with calibrated signal generator at each band | Simulation: ✅ | Physical test: Pending |

All claims must include the following disclaimer: *"Performance may vary based on environmental conditions, vehicle type, and local regulations. Results from controlled testing. Individual results may vary."*

---

*EmbeddedOS eCAD-Hardware-Products | eRadar360_CAD_Design | Document EOS-RADAR-LEGAL-001*
