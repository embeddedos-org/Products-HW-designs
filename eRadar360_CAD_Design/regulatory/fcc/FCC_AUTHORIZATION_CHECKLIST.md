# eRadar360 — FCC Authorization Checklist
**Document:** EOS-RADAR-FCC-001 | **Revision:** 1.0 | **Date:** 2026-06-03
**Applicant:** EmbeddedOS Inc. | **Product:** eRadar360 / Aegis One

---

## Overview

The eRadar360 contains three radio subsystems, each requiring separate FCC authorization:

| Subsystem | Chipset | Frequency | FCC Rule | Authorization Type |
|-----------|---------|-----------|----------|-------------------|
| 77 GHz FMCW Radar (×2) | TI AWR2944 | 76–81 GHz | 47 CFR §15.253 | Verification (self-declaration) |
| Wi-Fi 6 + Bluetooth 5.3 | Qualcomm QCA6174A-5 | 2.4/5 GHz + 2.4 GHz | 47 CFR §15.247 | Certification (TCB) |
| V2X DSRC | Autotalks TEKTON3 | 5.855–5.925 GHz | 47 CFR Part 90 Subpart M | Certification (FCC) |
| V2X C-V2X | Autotalks TEKTON3 | Band 47 (5.9 GHz) | 47 CFR Part 90 Subpart M | Certification (FCC) |
| Unintentional radiator | Full device | Broadband | 47 CFR Part 15B | Verification (self-declaration) |

---

## Part 1: 77 GHz Radar — 47 CFR §15.253

### Regulatory Basis

Under 47 CFR §15.253, vehicular radar systems operating in the 76–77 GHz band are permitted as unlicensed devices subject to the following limits:

| Parameter | Limit | AWR2944 Spec | Status |
|-----------|-------|-------------|--------|
| Peak EIRP | 50 dBm | 40 dBm (estimated) | ✅ Compliant |
| Average EIRP | 23.5 dBm | 18 dBm (estimated) | ✅ Compliant |
| Frequency range | 76–77 GHz | 76–81 GHz | ⚠️ See note |
| Emission bandwidth | 1 GHz max | 4 GHz (chirp) | ⚠️ See note |

> **Note on 76–81 GHz operation:** The AWR2944 operates across 76–81 GHz. The 77–81 GHz portion falls under §15.255 (automotive radar, 77–81 GHz), which permits higher EIRP (50 dBm peak, 40 dBm average) and wider bandwidth. The device will be tested and declared under both §15.253 and §15.255 as applicable.

### Checklist — §15.253 / §15.255

- [ ] Obtain AWR2944 FCC grant from TI (FCC ID: existing module grant)
- [ ] Confirm integration does not invalidate module grant (antenna gain, enclosure)
- [ ] Measure conducted output power at SPI/antenna interface
- [ ] Measure EIRP with production antenna array (8×8 SIW front, 4×4 SIW rear)
- [ ] Verify spurious emissions below −13 dBm average EIRP outside 76–81 GHz
- [ ] Prepare Verification declaration (no TCB required for §15.253)
- [ ] Label device with FCC ID of radar module or self-verification statement
- [ ] File FCC Form 731 (if self-verification) or obtain TCB certification

### Test Laboratory Requirements

- **Accreditation:** A2LA or NVLAP accredited, millimeter-wave capability
- **Recommended labs:** NTS (Fremont CA), Element Materials Technology, SGS
- **Test standard:** ANSI C63.26 (radiated emissions, 77 GHz)
- **Estimated cost:** $18,000–$35,000 per configuration
- **Lead time:** 8–12 weeks

---

## Part 2: Wi-Fi 6 + Bluetooth — 47 CFR §15.247

### Regulatory Basis

The Qualcomm QCA6174A-5 module operates under §15.247 (spread spectrum and digitally modulated intentional radiators, 2.4 GHz and 5 GHz ISM bands).

| Parameter | Limit | QCA6174A-5 Spec | Status |
|-----------|-------|----------------|--------|
| Max conducted output (2.4 GHz) | 30 dBm | 20 dBm | ✅ Compliant |
| Max conducted output (5 GHz) | 30 dBm | 23 dBm | ✅ Compliant |
| Frequency hopping (BT) | ≥75 hop channels | 79 channels | ✅ Compliant |
| Antenna gain | ≤6 dBi (fixed) | PCB trace ~2 dBi | ✅ Compliant |

### Checklist — §15.247

- [ ] Confirm QCA6174A-5 has existing FCC grant (FCC ID: PPD-AR5BXB112A or equivalent)
- [ ] Verify integration rules: antenna type, gain, host device enclosure
- [ ] If antenna gain exceeds module grant, obtain new certification via TCB
- [ ] Conduct co-location RF exposure evaluation (SAR or MPE) for BT + Wi-Fi simultaneous
- [ ] Prepare Class II Permissive Change application if modifying antenna
- [ ] Verify 5 GHz DFS (Dynamic Frequency Selection) compliance for channels 52–144
- [ ] Label with FCC ID of module (QCA6174A-5 grant)

---

## Part 3: V2X DSRC + C-V2X — 47 CFR Part 90 Subpart M

### Regulatory Basis

The Dedicated Short-Range Communications (DSRC) service at 5.850–5.925 GHz is governed by 47 CFR Part 90 Subpart M. C-V2X (PC5 sidelink) in Band 47 (5.855–5.925 GHz) is also authorized under Part 90 following the FCC's November 2020 Report and Order.

| Parameter | Limit | TEKTON3 Spec | Status |
|-----------|-------|-------------|--------|
| Max EIRP (DSRC) | 33 dBm | 23 dBm | ✅ Compliant |
| Frequency range | 5.850–5.925 GHz | 5.855–5.925 GHz | ✅ Compliant |
| Channel bandwidth | 10 MHz (DSRC) | 10 MHz | ✅ Compliant |
| Modulation (DSRC) | OFDM per IEEE 802.11p | OFDM | ✅ Compliant |
| Modulation (C-V2X) | SC-FDM per 3GPP | SC-FDM | ✅ Compliant |

### Checklist — Part 90 Subpart M

- [ ] Obtain TEKTON3 FCC grant from Autotalks (confirm existing FCC ID)
- [ ] Verify integration: antenna gain, cable loss, enclosure shielding
- [ ] Confirm dual-mode (DSRC + C-V2X) simultaneous operation is within grant
- [ ] Conduct antenna VSWR and gain measurement for 5.9 GHz SMA port (J5)
- [ ] Verify out-of-band emissions: −43 dBc at ±15 MHz from channel edge
- [ ] Prepare FCC Form 601 (Part 90 license application) if required for V2X RSU operation
- [ ] Note: OBU (On-Board Unit) operation in vehicles does not require individual license

---

## Part 4: Part 15B — Unintentional Radiator (Full Device)

### Regulatory Basis

The complete eRadar360 device (including all digital circuitry: RK3588S, STM32H7B3, DDR4, NOR Flash) must comply with Part 15B Class B limits as a consumer device.

| Frequency | Class B Limit (QP) | Measurement Distance |
|-----------|-------------------|---------------------|
| 30–88 MHz | 100 µV/m | 3 m |
| 88–216 MHz | 150 µV/m | 3 m |
| 216–960 MHz | 200 µV/m | 3 m |
| >960 MHz | 500 µV/m | 3 m |

### Checklist — Part 15B

- [ ] Conduct pre-compliance radiated emissions scan (30 MHz–1 GHz) at in-house or pre-comp lab
- [ ] Identify and mitigate any emissions from RK3588S clock harmonics (24 MHz, 76.8 MHz, 40 MHz)
- [ ] Verify DDR4 differential pair routing and termination (common source of 1–3 GHz emissions)
- [ ] Verify PCB ground plane continuity and chassis bonding
- [ ] Conduct full compliance radiated emissions test at accredited lab
- [ ] Conduct conducted emissions test (CISPR 32 / ANSI C63.4)
- [ ] Prepare Supplier's Declaration of Conformity (SDoC) for Part 15B
- [ ] Include FCC Part 15B statement in user manual and labeling

---

## Part 5: FCC Labeling Requirements

### Required Label Elements (47 CFR §15.19)

The device label must include:

```
FCC ID: [ASSIGNED ID]
This device complies with Part 15 of the FCC Rules.
Operation is subject to the following two conditions:
(1) This device may not cause harmful interference, and
(2) this device must accept any interference received,
including interference that may cause undesired operation.
```

For devices with multiple radio modules, each FCC ID must appear on the label or in the electronic labeling (e-label) system.

### E-Label Option (47 CFR §15.19(a)(10))

For devices where physical labeling space is constrained, FCC permits electronic labeling. The AMOLED display on eRadar360 qualifies. The e-label must be accessible within 3 menu steps from the home screen.

- [ ] Implement e-label screen in firmware (Settings → Device Info → Regulatory)
- [ ] Display: FCC ID, IC ID (Canada), CE mark (EU), all radio module IDs
- [ ] Physical label on device: "FCC ID: [ID] — See display for full regulatory information"

---

## Part 6: FCC Filing Timeline and Costs

| Activity | Timeline | Estimated Cost |
|----------|----------|----------------|
| Pre-compliance emissions scan | Month 1–2 | $3,000–$8,000 |
| 77 GHz radar verification testing | Month 3–5 | $18,000–$35,000 |
| Wi-Fi 6 / BT integration testing | Month 3–5 | $12,000–$22,000 |
| V2X DSRC/C-V2X certification | Month 4–6 | $15,000–$28,000 |
| Part 15B full compliance testing | Month 5–7 | $8,000–$15,000 |
| FCC filing fees (per application) | — | $1,085 (FCC fee) |
| TCB fees (Wi-Fi, V2X) | — | $3,000–$6,000 |
| **Total** | **7 months** | **$60,000–$115,000** |

---

## Part 7: Canada ISED / IC Requirements

The eRadar360 will also require Industry Canada (ISED) certification for Canadian market entry:

| Subsystem | Canadian Standard | IC Authorization |
|-----------|------------------|-----------------|
| 77 GHz radar | RSS-Gen + RSS-210 | RSS-210 Issue 10 |
| Wi-Fi 6 / BT | RSS-247 | IC ID required |
| V2X DSRC | RSS-252 | IC ID required |
| Part 15B equivalent | ICES-003 Class B | SDoC |

Canadian certification can typically be obtained simultaneously with FCC testing at minimal additional cost ($5,000–$12,000).

---

*EmbeddedOS eCAD-Hardware-Products | eRadar360_CAD_Design | Document EOS-RADAR-FCC-001*
