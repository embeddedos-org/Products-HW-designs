# eRadar360 — ISO 26262 Functional Safety and IEC 62443 Cybersecurity
**Document:** EOS-RADAR-SAFETY-001 | **Revision:** 1.0 | **Date:** 2026-06-03

---

## Part 1: ISO 26262 Functional Safety

### 1.1 Scope and Applicability

ISO 26262:2018 (Road vehicles — Functional safety) is the international standard for functional safety of electrical and electronic systems in road vehicles. While ISO 26262 is legally mandatory only for OEM vehicle systems in some jurisdictions, it is **strongly recommended** for aftermarket ADAS devices and is increasingly required by automotive OEM partners and fleet customers.

The eRadar360 is classified as an **aftermarket item** under ISO 26262 Part 8 §5.4.7 (items developed outside the vehicle development process). The applicable ASIL (Automotive Safety Integrity Level) is determined by hazard analysis.

### 1.2 Hazard Analysis and Risk Assessment (HARA)

Per ISO 26262 Part 3, the following hazards have been identified and assessed:

| Hazard ID | Hazard Description | Severity (S) | Exposure (E) | Controllability (C) | ASIL |
|-----------|-------------------|-------------|-------------|-------------------|------|
| H-001 | False collision warning causes driver to brake suddenly | S2 | E4 | C2 | ASIL-B |
| H-002 | Missed collision warning (no alert when threat present) | S3 | E3 | C2 | ASIL-B |
| H-003 | False laser alert causes driver distraction | S1 | E4 | C1 | QM |
| H-004 | OBD-II data corruption causes incorrect speed display | S1 | E3 | C1 | QM |
| H-005 | Device power loss during critical alert | S2 | E2 | C2 | ASIL-A |
| H-006 | Display failure obscures critical warning | S2 | E3 | C2 | ASIL-A |
| H-007 | Radar interference with vehicle's own radar systems | S2 | E3 | C2 | ASIL-A |
| H-008 | Windshield mount failure causes device to fall | S2 | E3 | C1 | ASIL-A |
| H-009 | V2X message spoofing causes false emergency alert | S2 | E2 | C2 | ASIL-A |
| H-010 | Overheating causes fire or smoke | S3 | E2 | C1 | ASIL-A |

**Maximum ASIL: ASIL-B** (H-001, H-002)

### 1.3 Safety Goals

| Safety Goal | ASIL | Derived From |
|-------------|------|-------------|
| SG-001: The eRadar360 shall not generate false collision warnings that cause abrupt driver braking more than once per 10,000 operating hours | ASIL-B | H-001 |
| SG-002: The eRadar360 shall detect and alert for imminent collision threats (TTC <1.5s) with a probability of detection ≥99.5% | ASIL-B | H-002 |
| SG-003: The eRadar360 shall maintain continuous operation during vehicle operation without unintended power loss | ASIL-A | H-005 |
| SG-004: The eRadar360 shall not generate electromagnetic interference that affects the host vehicle's safety systems | ASIL-A | H-007 |

### 1.4 Functional Safety Concept

The following safety mechanisms are implemented to achieve the safety goals:

| Safety Mechanism | Addresses | Implementation |
|-----------------|-----------|---------------|
| Dual-radar cross-validation | SG-001, SG-002 | Front and rear AWR2944 must agree on threat classification before P1 alert |
| AI confidence threshold | SG-001 | NPU classifier must exceed 95% confidence before generating collision alert |
| Watchdog timer (STM32H7B3) | SG-003 | 100ms hardware watchdog; resets system if main processor hangs |
| Power supply monitoring | SG-003 | TPS65219 PMIC monitors all rails; alerts on undervoltage |
| EMC shielding | SG-004 | Full metal enclosure, ferrite beads on all I/O lines |
| FMEA (see §1.5) | All | Systematic failure mode analysis for all safety-relevant components |

### 1.5 FMEA Summary (Safety-Relevant Components)

| Component | Failure Mode | Effect | Detection | Mitigation | ASIL |
|-----------|-------------|--------|-----------|-----------|------|
| AWR2944 (front) | No output | Missed collision warning | Watchdog + rear radar | Dual-radar cross-check | ASIL-B |
| AWR2944 (front) | Spurious output | False collision warning | AI confidence filter | 95% confidence threshold | ASIL-B |
| RK3588S | Hang/crash | No alerts generated | STM32 watchdog | Watchdog reset + alert | ASIL-A |
| TPS65219 | Undervoltage | System shutdown | PMIC interrupt | Graceful shutdown + alert | ASIL-A |
| AMOLED display | Blank/frozen | Missed visual alert | Display health monitor | Audio alert fallback | ASIL-A |
| Suction mount | Detachment | Device falls on driver | — | Mechanical design review | ASIL-A |
| TEKTON3 V2X | False BSM | False emergency alert | Message authentication | IEEE 1609.2 signature check | ASIL-A |

### 1.6 ISO 26262 Compliance Checklist

**Part 2 — Management of Functional Safety:**
- [ ] Appoint Safety Manager
- [ ] Establish Safety Culture training program
- [ ] Create Safety Plan (document EOS-RADAR-SAFETY-PLAN-001)
- [ ] Conduct Safety Audit at each development phase gate

**Part 3 — Concept Phase:**
- [ ] Complete HARA (this document §1.2)
- [ ] Define Safety Goals (this document §1.3)
- [ ] Define Functional Safety Concept (this document §1.4)
- [ ] Obtain HARA review sign-off from independent safety assessor

**Part 4 — Product Development (System Level):**
- [ ] Develop Technical Safety Concept from Functional Safety Concept
- [ ] Define hardware/software safety requirements allocation
- [ ] Conduct DFA (Dependent Failure Analysis) for ASIL-B items
- [ ] Conduct FTA (Fault Tree Analysis) for SG-001 and SG-002

**Part 5 — Product Development (Hardware):**
- [ ] Calculate PMHF (Probabilistic Metric for Hardware Failures) for ASIL-B items
- [ ] Verify PMHF ≤ 10 FIT (ASIL-B target)
- [ ] Conduct hardware design review per ISO 26262-5 §8
- [ ] Verify hardware safety requirements coverage

**Part 6 — Product Development (Software):**
- [ ] Classify software components by ASIL (alert generation = ASIL-B)
- [ ] Apply ASIL-B software development methods (MC/DC coverage, static analysis)
- [ ] Conduct software unit testing with ≥100% statement coverage for ASIL-B modules
- [ ] Conduct software integration testing

**Part 8 — Supporting Processes:**
- [ ] Conduct qualification of software tools (compilers, static analysis tools)
- [ ] Manage safety-relevant configuration items under version control
- [ ] Conduct change impact analysis for all safety-relevant changes

**Part 9 — ASIL-Oriented and Safety-Oriented Analyses:**
- [ ] Conduct FMEA for all safety-relevant hardware components (this document §1.5)
- [ ] Conduct FTA for top-level safety goals
- [ ] Conduct FMEDA (Failure Modes, Effects, and Diagnostic Analysis)

---

## Part 2: IEC 62443 Cybersecurity

### 2.1 Scope

IEC 62443 (Industrial Automation and Control Systems Security) provides a framework for cybersecurity of industrial and embedded systems. For the eRadar360, the relevant parts are:

- **IEC 62443-2-1:** Security Management System requirements
- **IEC 62443-3-3:** System security requirements and security levels
- **IEC 62443-4-2:** Technical security requirements for components

The eRadar360 targets **Security Level 2 (SL-2)**: protection against intentional violation using simple means with low resources.

### 2.2 Threat Model

| Threat Actor | Attack Vector | Asset Targeted | Likelihood | Impact |
|-------------|--------------|---------------|-----------|--------|
| Script kiddie | OBD-II port (physical) | Vehicle speed data | Medium | Low |
| Researcher | Wi-Fi / BT (wireless) | Device firmware | Medium | Medium |
| Malicious actor | V2X (wireless) | Alert system (spoofing) | Low | High |
| Supply chain | Firmware update | Device integrity | Low | High |
| Insider | Manufacturing | Device provisioning | Very Low | High |

### 2.3 Security Requirements (IEC 62443-4-2)

| Requirement ID | Requirement | Implementation | Status |
|---------------|-------------|---------------|--------|
| CR 1.1 | Human user identification and authentication | Device PIN + mobile app OAuth | ✅ |
| CR 1.2 | Software process and device identification | Device serial + ECDSA-P256 attestation | ✅ |
| CR 1.5 | Authenticator management | Secure element (ATECC608B equivalent) | ✅ |
| CR 2.1 | Authorization enforcement | Role-based access (user/admin/factory) | ✅ |
| CR 3.1 | Communication integrity | TLS 1.3 for cloud; IEEE 1609.2 for V2X | ✅ |
| CR 3.4 | Software and information integrity | ECDSA-P256 firmware signatures | ✅ |
| CR 3.5 | Input validation | All OBD-II and V2X inputs validated | ✅ |
| CR 4.1 | Information confidentiality | AES-256-GCM for stored data | ✅ |
| CR 4.3 | Use of cryptography | NIST-approved algorithms only | ✅ |
| CR 7.2 | Resource availability | Watchdog + rate limiting on V2X input | ✅ |
| CR 7.3 | Control system backup | Firmware rollback to last known good | ✅ |
| CR 7.6 | Network and security configuration settings | Hardened defaults, no open ports | ✅ |

### 2.4 UNECE WP.29 R155 / R156 (EU Market)

For EU market entry, the eRadar360 must comply with:

**R155 (Cybersecurity Management System):**
- [ ] Establish CSMS (Cybersecurity Management System) per R155 Annex 5
- [ ] Document cybersecurity risk assessment for the vehicle type
- [ ] Implement monitoring for new cyber threats post-launch
- [ ] Obtain CSMS certificate from Type Approval Authority

**R156 (Software Update Management System):**
- [ ] Establish SUMS (Software Update Management System) per R156 Annex 4
- [ ] Implement cryptographically signed OTA updates
- [ ] Implement rollback mechanism to previous software version
- [ ] Log all software updates with timestamp and version
- [ ] Obtain SUMS certificate from Type Approval Authority

### 2.5 OBD-II Security

The OBD-II connection presents a unique attack surface. The eRadar360 implements:

| Control | Implementation | Verification |
|---------|---------------|-------------|
| Read-only OBD-II | ELM327 configured for read-only mode (AT commands disabled) | Firmware test FT-OBD-001 |
| PID whitelist | Only approved PIDs (speed, RPM, fuel level) are processed | Code review |
| Input validation | All OBD-II responses validated against expected ranges | Unit test UT-OBD-001 |
| Rate limiting | Maximum 10 OBD-II queries per second | Firmware implementation |
| Anomaly detection | Alert if OBD-II returns implausible values | Algorithm test AT-OBD-001 |

---

## Part 3: Compliance Timeline and Costs

| Activity | Timeline | Estimated Cost |
|----------|----------|----------------|
| ISO 26262 HARA and Safety Concept | Month 1–3 | $20,000–$40,000 |
| ISO 26262 hardware FMEA/FTA | Month 3–5 | $15,000–$25,000 |
| ISO 26262 software safety analysis | Month 4–6 | $20,000–$35,000 |
| ISO 26262 independent safety assessment | Month 8–10 | $30,000–$60,000 |
| IEC 62443 gap assessment | Month 2–3 | $8,000–$15,000 |
| Penetration testing (IEC 62443 SL-2) | Month 6–8 | $20,000–$40,000 |
| UNECE WP.29 R155/R156 (EU) | Month 8–12 | $25,000–$50,000 |
| **Total** | **12 months** | **$138,000–$265,000** |

---

*EmbeddedOS eCAD-Hardware-Products | eRadar360_CAD_Design | Document EOS-RADAR-SAFETY-001*
