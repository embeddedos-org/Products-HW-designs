# E-Government Terminals — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Citizen service terminal handling identity document verification, biometric capture and secure form submission for government services. Biometric templates are matched on the terminal's secure element and never stored locally, which keeps the deployment out of the highest-risk data categories.

## Electrical Specifications — eGOV-500
| Parameter | Specification |
|---|---|
| **Processor** | TI AM6254 quad Cortex-A53 |
| **Document reading** | ICAO 9303 MRZ, contactless chip, UV and IR inspection |
| **Biometrics** | Fingerprint and facial capture, ISO/IEC 19794 templates |
| **Template handling** | Matched in the secure element, never persisted on disk |
| **Signature** | eIDAS-compliant qualified electronic signature support |
| **Printing** | Integrated receipt and document printer interface |
| **Accessibility** | EN 301 549 conformant interaction |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 10 |
| **Dimensions** | 200mm x 150mm |
| **IPC Class** | Class 2 |
| **Finish** | ENIG |
| **Security** | Tamper switch on enclosure wired to zeroise |

## Compliance Targets
| Standard | Scope |
|---|---|
| ICAO Doc 9303 | Machine readable travel documents |
| eIDAS Regulation 910/2014 | Electronic identification and trust services |
| EN 301 549 | Accessibility requirements for ICT products |
