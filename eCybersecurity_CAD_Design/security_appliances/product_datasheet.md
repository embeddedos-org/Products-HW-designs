# Security Appliances — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-06-03 | **Status:** Design Phase

## Product Family

| Model | Type | Standard |
|---|---|---|
| eHSM-Pro | Hardware security module | FIPS 140-3 Level 3 |
| eFirewall-10G | 10GbE hardware firewall | Common Criteria EAL4+ |
| eEncrypt-Module | AES-256/RSA-4096 encryption module | FIPS 140-3 Level 2 |
| eSecComm | Secure communication device | NSA Suite B |
| eIDVerify | Identity verification terminal | FIPS 201-3 |

## Electrical Specifications — eHSM-Pro
| Parameter | Specification |
|---|---|
| **CPU** | NXP LS1046A (quad Cortex-A72, security extensions) |
| **Crypto engine** | Dedicated AES/RSA/ECC hardware accelerator |
| **Key storage** | Tamper-evident battery-backed SRAM |
| **RNG** | True hardware RNG (NIST SP 800-90B) |
| **Tamper response** | Zeroize keys in <1ms on tamper |
| **Interfaces** | PCIe ×4, USB 3.0, Ethernet ×2 |
| **FIPS** | FIPS 140-3 Level 3 |
