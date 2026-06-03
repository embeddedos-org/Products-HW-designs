# eRadar360 — Antenna Design Guide

## 1. Why SIW Phased Array?

Standard microstrip patch arrays (used in Valentine R8, Escort Redline 360c) are **fixed-beam** — the antenna always points straight ahead with no ability to focus. The SIW (Substrate Integrated Waveguide) phased array electronically steers the beam up to **±45°** without moving any parts.

**Practical impact:** When the AI detects a signal at 20° left, firmware steers the beam toward it for 3–4 dB extra gain. That's detecting a gun at **2 miles vs 1 mile**.

### Comparison Table

| Antenna Type | Gain | Steering | Complexity | Cost | eRadar360 Use |
|-------------|------|----------|-----------|------|---------------|
| Horn antenna | 20–25 dBi | Fixed | Low | $$ | ❌ Too large |
| Microstrip patch array | 15–20 dBi | Fixed | Low | $ | ❌ No steering |
| Lens antenna | 25–30 dBi | Fixed | Medium | $$$ | ❌ Too expensive |
| **SIW phased array** | **18–24 dBi** | **±45°** | **High** | **$$** | **✅ Selected** |
| AESA (active phased array) | 25–35 dBi | ±60° | Very high | $$$$ | ❌ Overkill |

---

## 2. Material Selection: Rogers RO4003C

**This is the single most critical material decision in the entire design.**

At Ka-band (34 GHz), standard FR4 laminate has a loss tangent (tanδ) of ~0.020, which causes **~4 dB of front-end signal loss** before the signal reaches the LNA. Rogers RO4003C has tanδ = 0.0027 — an order of magnitude better.

| Property | FR4 | Rogers RO4003C | Impact |
|----------|-----|----------------|--------|
| Dielectric constant (εr) | 4.4 | 3.38 | Wider traces, easier fabrication |
| Loss tangent (tanδ) @ 10 GHz | 0.020 | 0.0027 | **7× lower loss** |
| Insertion loss @ 34 GHz | ~1.2 dB/cm | ~0.17 dB/cm | **4 dB saved over 3cm path** |
| CTE (ppm/°C) | 14–17 | 11 | Better dimensional stability |
| Tg (°C) | 130–140 | 280 | Survives car dashboard temps |
| Cost multiplier | 1× | 3–4× | Worth it for RF layers only |

**Decision:** Use Rogers RO4003C for PCB layers 1-2 (RF section only). Layers 3-10 remain Isola 370HR FR4 to control cost.

---

## 3. Front Array: 8×8 SIW Patch Elements

### 3.1 Specifications

| Parameter | Value |
|-----------|-------|
| Elements | 8 × 8 = 64 |
| Frequency | 33.4–36.0 GHz (Ka-band) |
| Gain | 24 dBi peak |
| 3 dB beamwidth | 8° × 8° (boresight) |
| Beam steering | ±45° azimuth, ±30° elevation |
| Polarization | Linear (vertical) |
| VSWR | < 1.5:1 across band |
| Array size | 40mm × 40mm |

### 3.2 Element Spacing Calculation

For maximum scan angle without grating lobes:

```
d ≤ λ₀ / (1 + sin θ_max)

Where:
  λ₀ = c / f = 3×10⁸ / 35×10⁹ = 8.57 mm  (at 35 GHz center freq)
  θ_max = 45°

  d ≤ 8.57 / (1 + sin 45°)
  d ≤ 8.57 / 1.707
  d ≤ 5.02 mm

Selected: d = 4.8 mm (0.56 λ₀) — provides margin against grating lobes
```

### 3.3 Patch Element Geometry

Each element is a rectangular microstrip patch on Rogers RO4003C:

```
Patch width:  W = c / (2f √((εr+1)/2))
              W = 3×10⁸ / (2 × 35×10⁹ × √((3.38+1)/2))
              W = 3×10⁸ / (70×10⁹ × 1.48)
              W = 2.90 mm

Patch length: L ≈ c / (2f √εr) - 2ΔL
              L ≈ 3×10⁸ / (2 × 35×10⁹ × √3.38) - 2(0.05)
              L ≈ 2.33 - 0.10
              L ≈ 2.23 mm

Feed offset: x_f = L / (2π) × arccos(√(Z_in/R_edge))
             ≈ 0.55 mm from center (for 50Ω match)
```

### 3.4 SIW Waveguide Structure

The SIW is formed by two rows of plated vias connecting the top copper (Layer 1) to the ground plane (Layer 2):

```
Via diameter:       d_via = 0.30 mm
Via pitch:          p = 0.50 mm  (= λg/20, preventing leakage)
SIW width:          a_siw = λg/2 + d_via = 4.28 + 0.30 = 4.58 mm
Effective width:    a_eff = a_siw - d_via²/(0.95 × p) = 4.39 mm

Guide wavelength:   λg = λ₀ / √(1 - (λ₀/2a_eff)²)
                    λg = 8.57 / √(1 - (8.57/8.78)²)
                    λg = 8.57 / 0.219
                    λg ≈ 10.0 mm  (approximate — iterate for exact)
```

### 3.5 Phase Shifter Design

4-bit digital phase shifters using PIN diode MEMS switches:

| Bit | Phase Shift | Resolution |
|-----|-------------|-----------|
| 0 | 22.5° | LSB |
| 1 | 45° | — |
| 2 | 90° | — |
| 3 | 180° | MSB |

Total: 16 phase states, 22.5° resolution. Sufficient for ±45° steering with 8 elements.

---

## 4. Rear Array: 4×4 SIW Patch Elements

| Parameter | Value |
|-----------|-------|
| Elements | 4 × 4 = 16 |
| Gain | 18 dBi peak |
| 3 dB beamwidth | 16° × 16° |
| Beam steering | ±30° azimuth |
| Array size | 22mm × 22mm |

Same element geometry and SIW structure as front array. Reduced element count trades gain for cost and space.

---

## 5. Multi-Band Coverage

The SIW arrays handle Ka-band (primary threat band). K-band and X-band are received by separate smaller antennas:

| Band | Frequency | Antenna Type | Gain | Size |
|------|-----------|-------------|------|------|
| Ka | 33.4–36.0 GHz | SIW phased array (above) | 24/18 dBi | 40×40 / 22×22 mm |
| K | 24.05–24.25 GHz | 2×2 microstrip patch | 12 dBi | 15×15 mm |
| Ku | 13.45–13.50 GHz | Single patch + LNA | 8 dBi | 12×12 mm |
| X | 10.5–10.55 GHz | Single patch + LNA | 7 dBi | 15×15 mm |

K/Ku/X-band patches are on the same Rogers 4003C substrate, sharing the RF ground plane.

---

## 6. Feed Network

### 6.1 Corporate Feed (Power Divider Tree)

The 8×8 array uses a **3-stage Wilkinson power divider** tree:
- Stage 1: 1→2 split (row/column)
- Stage 2: 1→4 split per row
- Stage 3: 1→8 split per column
- Total: 1→64 with equal amplitude

Each split includes a 4-bit phase shifter for beam steering.

### 6.2 Feed Loss Budget

| Stage | Loss | Cumulative |
|-------|------|-----------|
| SMA → SIW transition | 0.3 dB | 0.3 dB |
| Stage 1 divider | 0.2 dB | 0.5 dB |
| Stage 2 divider | 0.3 dB | 0.8 dB |
| Stage 3 divider | 0.3 dB | 1.1 dB |
| Phase shifter (4-bit) | 1.5 dB | 2.6 dB |
| SIW-to-patch transition | 0.2 dB | 2.8 dB |
| **Total feed loss** | **2.8 dB** | — |

**Net antenna gain = 24 dBi (element) - 2.8 dB (feed) = 21.2 dBi effective**

---

## 7. Thermal Considerations

At maximum scan (±45°), the phase shifter PIN diodes dissipate ~50 mW per element:
- Front array: 64 × 50 mW = 3.2 W
- Rear array: 16 × 50 mW = 0.8 W
- Total: 4.0 W in the RF section

The RF shield can (SHIELD1) acts as a heatsink. Thermal vias under the phase shifter ICs connect to the ground plane for heat spreading. Operating range: -20°C to +85°C (automotive).
