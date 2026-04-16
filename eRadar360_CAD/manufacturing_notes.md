# eRadar360 — Manufacturing & Gerber Notes

## Gerber File Naming Convention

| File | Layer | Description |
|------|-------|-------------|
| `eradar360-F_Cu.gbr` | Layer 1 | Top copper (RF: SIW arrays, Ka-band traces) |
| `eradar360-In1_Cu.gbr` | Layer 2 | RF ground plane (SIW bottom wall) |
| `eradar360-In2_Cu.gbr` | Layer 3 | High-speed signal (DDR4, MIPI-DSI, SPI) |
| `eradar360-In3_Cu.gbr` | Layer 4 | Digital ground plane |
| `eradar360-In4_Cu.gbr` | Layer 5 | Power plane 1 (VCC_3V3, VCC_1V8, VCC_0V85) |
| `eradar360-In5_Cu.gbr` | Layer 6 | Power plane 2 (VCC_1V1, VCC_5V, VCC_OLED) |
| `eradar360-In6_Cu.gbr` | Layer 7 | Digital ground plane |
| `eradar360-In7_Cu.gbr` | Layer 8 | Low-speed signal (I2C, UART, CAN, GPIO) |
| `eradar360-In8_Cu.gbr` | Layer 9 | Bottom ground / thermal |
| `eradar360-B_Cu.gbr` | Layer 10 | Bottom copper (PMIC, passives, connectors) |
| `eradar360-F_Mask.gbr` | — | Top solder mask (matte black) |
| `eradar360-B_Mask.gbr` | — | Bottom solder mask (matte black) |
| `eradar360-F_Silkscreen.gbr` | — | Top silkscreen (white epoxy) |
| `eradar360-B_Silkscreen.gbr` | — | Bottom silkscreen (white epoxy) |
| `eradar360-F_Paste.gbr` | — | Top solder paste stencil |
| `eradar360-B_Paste.gbr` | — | Bottom solder paste stencil |
| `eradar360-Edge_Cuts.gbr` | — | Board outline (120mm × 85mm) |
| `eradar360.drl` | — | Drill file (Excellon format) |
| `eradar360-NPTH.drl` | — | Non-plated through holes |

---

## Fabrication Notes

### PCB Specifications

| Parameter | Value |
|-----------|-------|
| Board size | 120.0 × 85.0 mm |
| Layer count | 10 |
| Thickness | 1.6 mm ±10% |
| Min trace width | 0.10 mm (4 mil) |
| Min trace spacing | 0.10 mm (4 mil) |
| Min drill size | 0.10 mm (micro-via, layers 1-2) |
| Surface finish | ENIG (3-6 µin Au / 120-240 µin Ni) |
| Solder mask | Taiyo PSR-4000 AUS703, matte black, both sides |
| Silkscreen | White epoxy ink, both sides |
| Impedance control | Required (see pcb_stackup.txt) |
| IPC class | Class 2 (Automotive) |

### Material Requirements (CRITICAL)

| Layers | Material | Why |
|--------|----------|-----|
| 1–2 (RF) | **Rogers RO4003C** | εr=3.38, tanδ=0.0027 @ 10 GHz. FR4 causes 4 dB excess loss at Ka-band. |
| 3–10 (Digital) | Isola 370HR | εr=3.92, Tg≥180°C, automotive grade |
| PP 1-2 | Rogers 4450F | RF prepreg, εr=3.54 |
| PP 3-10 | Isola 370HR prepreg | Standard digital prepreg |

⚠ **DO NOT substitute FR4 for layers 1-2.** This will halve the Ka-band detection range.

### Special Processing

1. **SIW via fence** (layers 1-2): 0.3mm drill, 0.5mm pitch, continuous rows forming waveguide walls. Total ~800 vias in the RF section.
2. **Via-in-pad (VIPPO)**: Required for U1, U2 (AWR2944), U3 (RK3588S), U4 (TEKTON3), U11 (DDR4). Fill with conductive epoxy, plate over, ensure flat for BGA reflow.
3. **Micro-vias**: Layers 1↔2 (0.10mm drill, laser-drilled) for AWR2944 BGA escape routing.
4. **Buried vias**: Layers 3↔8 (0.15mm drill) for RK3588S DDR4 routing.
5. **Impedance test coupons**: Include on each panel — 50Ω, 100Ω, 120Ω.
6. **Edge plating**: Castellated pads on 2 edges for RF shield can attachment.
7. **Controlled depth routing**: Cutout for display FPC connector clearance.

### Panelization

| Parameter | Value |
|-----------|-------|
| Panel size | 280 × 200 mm |
| Boards per panel | 2 × 2 = 4 |
| Rail width | 10 mm |
| V-score | Between boards |
| Fiducials | 3× per panel + 2× per board (Top + Bottom) |
| Tooling holes | 4× per panel (3.2mm, non-plated) |

---

## Assembly Notes

### Reflow Profile (Lead-Free SAC305)

| Zone | Temperature | Duration |
|------|-------------|----------|
| Preheat | 150°C → 200°C | 60–120 s |
| Soak | 200°C ± 5°C | 60–90 s |
| Ramp to peak | 200°C → 245°C | 30–60 s |
| Peak | 245°C ± 5°C | 10–20 s |
| Cooling | 245°C → 200°C | < 4°C/s |

### Assembly Order

1. **Bottom side first** (reflow):
   - U8 (STM32H7B3 LQFP-176)
   - U10 (TPS65219 VQFN-24)
   - U12 (Flash SOP-8)
   - U13A-E (OPA857 WQFN-16 × 5)
   - U14 (QCA6174A BGA-120)
   - U15 (TPA2012D2 QFN-20)
   - U16 (TPS61046 SOT-563)
   - All bottom passives

2. **Top side second** (reflow):
   - U1 (AWR2944 BGA-232) — front radar
   - U2 (AWR2944 BGA-232) — rear radar
   - U3 (RK3588S FCBGA-775) — main CPU
   - U4 (TEKTON3 BGA-196) — V2X
   - U11 (DDR4 FBGA-96)
   - All top passives, crystals, ferrite beads

3. **Hand solder / manual placement**:
   - U5A-E (laser APD TO-46 × 5) — orientation critical
   - J1 (USB-C) — THT pins
   - J3 (OBD-II J1962) — THT connector
   - J5 (SMA) — THT
   - J6 (JTAG header) — THT
   - SW1-SW3 (tact switches)
   - SPK1 (speaker) — wire bond
   - ANT_GPS (ceramic patch) — adhesive + solder

4. **Post-assembly**:
   - Attach RF shield can (SHIELD1) — snap-fit + solder tabs
   - Apply thermal pad (HS1) between U3 and shield
   - Connect display FPC cable to J4
   - Connect GPS antenna to J7 (U.FL)

### X-Ray Inspection Required

- U1, U2 (AWR2944 BGA) — check for solder bridging, head-in-pillow
- U3 (RK3588S FCBGA-775) — check all 775 balls
- U4 (TEKTON3 BGA-196)
- U11 (DDR4 FBGA-96)
- U14 (QCA6174A BGA-120)
- All via-in-pad locations

### AOI Inspection

- All QFN/QFP packages (U8, U10, U15, U16)
- All 0402 passives (≥150 placements)
- Solder paste coverage on all BGA pads

---

## Test Points

| TP | Net | Location | Purpose |
|----|-----|----------|---------|
| TP1 | VCC_5V | Near J1 | Input voltage |
| TP2 | VCC_3V3 | Near U10 pin 7 | 3.3V rail |
| TP3 | VCC_1V8 | Near U10 pin 10 | 1.8V rail |
| TP4 | VCC_0V85 | Near U10 pin 13 | CPU core |
| TP5 | VCC_1V1 | Near U10 pin 16 | Radar core |
| TP6 | GND | Center board | Ground reference |
| TP7 | UART2_TX | Near U3 | Debug console TX |
| TP8 | UART2_RX | Near U3 | Debug console RX |
| TP9 | SPI0_CLK | Near U1 | Front radar SPI |
| TP10 | I2C0_SDA | Near U7 | I2C bus |
| TP11 | CANH | Near J3 | CAN bus high |
| TP12 | CANL | Near J3 | CAN bus low |

---

*Document: ERAD360-MFG-001 Rev A | Date: 2026-04-15 | embeddedOS.org*
