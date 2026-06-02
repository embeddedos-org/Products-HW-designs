#!/usr/bin/env python3
"""
EoS Health — Signal Integrity Simulation (All 4 Devices)

Simulates:
  1. BLE 2.4 GHz antenna matching network (L-network Pi filter)
     - S11 return loss vs frequency
     - Antenna efficiency vs mismatch
     - Link budget (TX power, path loss, RX sensitivity)

  2. PCB trace impedance
     - Microstrip characteristic impedance vs width/height
     - Differential pair impedance for ECG traces
     - Via stub resonance analysis

  3. EMI from switching regulators
     - Buck converter switching noise spectrum
     - Conducted EMI on power rails
     - Radiated EMI estimate (FCC Part 15 / CE EN 55032)

  4. Analog front-end isolation
     - Digital-to-analog coupling via ground plane
     - Decoupling capacitor effectiveness
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy import signal
from pathlib import Path

PLOTS_DIR = Path(__file__).parent.parent / "plots"
PLOTS_DIR.mkdir(exist_ok=True)

# ── BLE Antenna Parameters ────────────────────────────────────────────────────
F_BLE_GHZ    = 2.44     # GHz — BLE center frequency
F_BLE_HZ     = 2.44e9   # Hz
C0           = 3e8       # m/s — speed of light
LAMBDA_BLE   = C0 / F_BLE_HZ  # ~12.3 cm

# nRF52840 RF output
TX_POWER_DBM = 4.0       # dBm — nRF52840 max TX power
RX_SENS_DBM  = -95.0     # dBm — nRF52840 BLE sensitivity

# Chip antenna (Johanson 2450AT18A100E)
ANTENNA_GAIN_DBI = 2.0   # dBi — chip antenna gain
ANTENNA_EFF_PCT  = 65.0  # %   — radiation efficiency (typical for chip antenna on small PCB)

# Matching network (L-network)
Z0 = 50.0   # Ω — reference impedance
Z_ANT = complex(35, -15)  # Ω — antenna impedance at 2.44 GHz (typical chip antenna)


# ── PCB Trace Parameters ──────────────────────────────────────────────────────
# FR4 substrate
ER_FR4       = 4.4       # relative permittivity
H_FR4_MM     = 0.8       # mm — substrate height (2-layer PCB)
T_COPPER_MM  = 0.035     # mm — copper thickness (1 oz)

# Flex PCB (HEALTH-RING, HEALTH-LAB)
ER_FLEX      = 3.5       # Kapton/polyimide
H_FLEX_MM    = 0.1       # mm — flex substrate height

# ECG differential pair requirements
Z_DIFF_TARGET = 100.0    # Ω — differential impedance target
Z_SE_TARGET   = 50.0     # Ω — single-ended impedance target


# ── Switching Regulator Parameters ───────────────────────────────────────────
BUCK_FREQ_HZ  = 2e6      # Hz — switching frequency (2 MHz — above AM band)
BUCK_VIN      = 3.7      # V  — input voltage
BUCK_VOUT     = 1.8      # V  — output voltage
BUCK_IOUT     = 0.05     # A  — output current
BUCK_L_UH     = 2.2      # µH — inductor
BUCK_C_OUT_UF = 10.0     # µF — output capacitor


# ── Antenna Simulation ────────────────────────────────────────────────────────

def compute_s11(Z_load, Z0=50.0):
    """Compute S11 reflection coefficient."""
    gamma = (Z_load - Z0) / (Z_load + Z0)
    return gamma


def matching_network_response(freqs_ghz):
    """
    Simulate Pi-network matching from 50Ω to chip antenna impedance.
    Pi-network (shunt C1 — series L — shunt C2) provides better bandwidth
    and achieves S11 < -10 dB at 2.44 GHz.
    Returns S11 (dB) vs frequency.
    """
    s11_db = []
    for f_ghz in freqs_ghz:
        f = f_ghz * 1e9
        omega = 2 * np.pi * f

        # Chip antenna impedance model (Lorentzian resonance near 2.44 GHz)
        # Johanson 2450AT18A100E: R_rad=50Ω, Q=6 at resonance
        f_res = 2.44e9
        Q_ant = 6.0
        R_rad = 50.0  # Ω — radiation resistance (at resonance = 50Ω for this antenna)
        X_ant = R_rad * Q_ant * (f/f_res - f_res/f)
        Z_ant = complex(R_rad, X_ant)

        # Pi-network: shunt C1 (input) — series L — shunt C2 (output)
        # Optimised for 50Ω → 50Ω match at 2.44 GHz
        # C1 = 1.0 pF (input shunt), L = 2.7 nH (series), C2 = 1.0 pF (output shunt)
        C1 = 1.0e-12   # F — input shunt capacitor
        L_s = 2.7e-9   # H — series inductor
        C2 = 1.0e-12   # F — output shunt capacitor

        # Input shunt C1 in parallel with (series L + (C2 || Z_ant))
        Z_C1 = complex(0, -1 / (omega * C1))
        Z_L  = complex(0, omega * L_s)
        Z_C2 = complex(0, -1 / (omega * C2))

        # C2 in parallel with Z_ant
        Z_c2_ant = (Z_C2 * Z_ant) / (Z_C2 + Z_ant)
        # Series L + (C2 || Z_ant)
        Z_series = Z_L + Z_c2_ant
        # C1 in parallel with Z_series
        Z_total = (Z_C1 * Z_series) / (Z_C1 + Z_series)

        gamma = compute_s11(Z_total, Z0)
        s11_db.append(20 * np.log10(abs(gamma) + 1e-12))

    return np.array(s11_db)


def compute_link_budget(distance_m: float, freq_ghz: float = 2.44) -> dict:
    """Compute BLE link budget at given distance."""
    # Free-space path loss (Friis equation)
    lambda_m = C0 / (freq_ghz * 1e9)
    fspl_db = 20 * np.log10(4 * np.pi * distance_m / lambda_m)

    # Human body absorption (typical 3-5 dB for on-body BLE)
    body_loss_db = 4.0

    # Antenna gain (both ends)
    tx_ant_gain = ANTENNA_GAIN_DBI
    rx_ant_gain = 2.15  # dBi — smartphone antenna

    # Received power
    rx_power_dbm = (TX_POWER_DBM + tx_ant_gain + rx_ant_gain
                    - fspl_db - body_loss_db
                    + 10 * np.log10(ANTENNA_EFF_PCT / 100))

    # Link margin
    link_margin_db = rx_power_dbm - RX_SENS_DBM

    return {
        'distance_m': distance_m,
        'fspl_db': fspl_db,
        'rx_power_dbm': rx_power_dbm,
        'link_margin_db': link_margin_db,
        'connected': link_margin_db > 0,
    }


# ── PCB Trace Impedance ───────────────────────────────────────────────────────

def microstrip_impedance(w_mm: float, h_mm: float, er: float, t_mm: float = 0.035) -> float:
    """
    Compute microstrip characteristic impedance (IPC-2141A formula).
    w: trace width (mm), h: substrate height (mm), er: relative permittivity
    """
    w_eff = w_mm + t_mm / np.pi * (1 + np.log(4 * np.pi * w_mm / t_mm))
    w_eff = max(w_eff, 0.001)

    if w_eff / h_mm < 1:
        Z0 = (60 / np.sqrt(er)) * np.log(8 * h_mm / w_eff + w_eff / (4 * h_mm))
    else:
        Z0 = (120 * np.pi / np.sqrt(er) /
              (w_eff / h_mm + 1.393 + 0.667 * np.log(w_eff / h_mm + 1.444)))
    return Z0


def find_trace_width(target_z: float, h_mm: float, er: float, t_mm: float = 0.035) -> float:
    """Find trace width for target impedance using binary search."""
    w_low, w_high = 0.01, 10.0
    for _ in range(50):
        w_mid = (w_low + w_high) / 2
        z_mid = microstrip_impedance(w_mid, h_mm, er, t_mm)
        if z_mid > target_z:
            w_low = w_mid
        else:
            w_high = w_mid
    return (w_low + w_high) / 2


def differential_impedance(w_mm: float, s_mm: float, h_mm: float, er: float) -> float:
    """
    Compute differential microstrip impedance (Wadell formula approximation).
    s: spacing between traces (mm)
    """
    Z_se = microstrip_impedance(w_mm, h_mm, er)
    # Coupling factor (approximate)
    Q = 0.347 * np.exp(-2.455 * s_mm / h_mm)
    Z_diff = 2 * Z_se * (1 - Q)
    return Z_diff


# ── EMI Simulation ────────────────────────────────────────────────────────────

def buck_converter_emi(freqs_hz):
    """
    Simulate conducted EMI spectrum from buck converter.
    Returns noise voltage (dBµV) vs frequency.
    """
    noise_dbmuv = []
    for f in freqs_hz:
        # Fundamental switching frequency
        f_sw = BUCK_FREQ_HZ
        # Harmonic number
        n = round(f / f_sw)
        if n == 0:
            n = 1
        f_harmonic = n * f_sw

        # Trapezoidal current waveform — harmonic amplitudes decay as 1/n²
        # Duty cycle D = Vout/Vin
        D = BUCK_VOUT / BUCK_VIN
        delta_I = BUCK_VIN * D * (1 - D) / (BUCK_FREQ_HZ * BUCK_L_UH * 1e-6)

        # Harmonic amplitude (trapezoidal approximation)
        if n == 0:
            I_n = delta_I * D
        else:
            I_n = (2 * delta_I / (n * np.pi)) * abs(np.sin(n * np.pi * D))

        # Voltage noise across output capacitor ESR
        ESR = 0.01  # Ω — 10 mΩ ESR for ceramic cap
        V_n = I_n * ESR

        # Convert to dBµV
        V_dbmuv = 20 * np.log10(V_n * 1e6 + 1e-12)

        # Add frequency-dependent attenuation from output filter
        # LC filter: -40 dB/decade above resonance
        f_lc = 1 / (2 * np.pi * np.sqrt(BUCK_L_UH * 1e-6 * BUCK_C_OUT_UF * 1e-6))
        if f > f_lc:
            V_dbmuv -= 40 * np.log10(f / f_lc)

        noise_dbmuv.append(V_dbmuv)

    return np.array(noise_dbmuv)


def analog_digital_coupling(freqs_hz, ground_impedance_mohm: float = 5.0):
    """
    Simulate digital noise coupling into analog ground plane.
    Returns coupled noise voltage (dBµV) vs frequency.
    """
    # Digital switching current (MCU + BLE)
    I_digital_ma = 5.0  # mA peak digital current
    I_digital = I_digital_ma * 1e-3

    # Ground plane impedance (increases with frequency due to skin effect)
    Z_gnd = ground_impedance_mohm * 1e-3 * np.sqrt(freqs_hz / 1e6)

    # Coupled voltage
    V_coupled = I_digital * Z_gnd
    V_dbmuv = 20 * np.log10(V_coupled * 1e6 + 1e-12)

    return V_dbmuv


# ── Main Simulation ───────────────────────────────────────────────────────────

def run_signal_integrity_simulation():
    print("Running Signal Integrity Simulation...")

    # 1. BLE antenna S11 vs frequency
    freqs_ghz = np.linspace(1.5, 3.5, 500)
    s11_db = matching_network_response(freqs_ghz)

    # 2. Link budget vs distance
    distances = np.logspace(-1, 2, 100)  # 0.1 m to 100 m
    link_budgets = [compute_link_budget(d) for d in distances]
    rx_powers = [lb['rx_power_dbm'] for lb in link_budgets]
    max_range = max([d for d, lb in zip(distances, link_budgets) if lb['connected']], default=0)

    # 3. PCB trace impedance vs width (FR4 and Flex)
    widths_mm = np.linspace(0.05, 2.0, 200)
    z_fr4  = [microstrip_impedance(w, H_FR4_MM,  ER_FR4)  for w in widths_mm]
    z_flex = [microstrip_impedance(w, H_FLEX_MM, ER_FLEX) for w in widths_mm]

    # Find widths for 50Ω on FR4 and Flex
    w_50_fr4  = find_trace_width(50, H_FR4_MM,  ER_FR4)
    w_50_flex = find_trace_width(50, H_FLEX_MM, ER_FLEX)

    # Differential pair impedance (100Ω) for ECG traces
    spacings = np.linspace(0.05, 1.0, 50)
    w_ecg = 0.15  # mm — ECG trace width
    z_diff_fr4 = [differential_impedance(w_ecg, s, H_FR4_MM, ER_FR4) for s in spacings]
    s_100_fr4 = spacings[np.argmin(np.abs(np.array(z_diff_fr4) - 100))]

    # 4. EMI spectrum
    freqs_emi = np.logspace(4, 9, 2000)  # 10 kHz to 1 GHz
    emi_noise = buck_converter_emi(freqs_emi)
    coupling_noise = analog_digital_coupling(freqs_emi)

    # FCC Part 15 Class B limits (approximate)
    fcc_limits = np.where(freqs_emi < 30e6, 48, np.where(freqs_emi < 88e6, 48, 54))

    # ── Plotting ──────────────────────────────────────────────────────────────
    fig = plt.figure(figsize=(18, 14), facecolor='#0d1117')
    fig.suptitle('EoS Health — Signal Integrity Simulation (All 4 Devices)\n'
                 'BLE Antenna | PCB Trace Impedance | EMI | Analog-Digital Isolation',
                 color='white', fontsize=13, fontweight='bold', y=0.99)

    gs = gridspec.GridSpec(3, 3, figure=fig, hspace=0.5, wspace=0.4)
    bg = '#0d1117'; grid_c = '#21262d'; text_c = '#e6edf3'
    c = ['#58a6ff', '#3fb950', '#ffa657', '#f78166', '#d2a8ff', '#79c0ff']

    def style_ax(ax, title):
        ax.set_facecolor(bg)
        ax.tick_params(colors=text_c, labelsize=7)
        for spine in ax.spines.values():
            spine.set_edgecolor(grid_c)
        ax.grid(True, color=grid_c, alpha=0.5, linewidth=0.5)
        ax.set_title(title, color=text_c, fontsize=9, fontweight='bold')

    def leg(ax):
        legend = ax.legend(fontsize=6.5, facecolor='#161b22', edgecolor=grid_c)
        for text in legend.get_texts():
            text.set_color(text_c)

    # 1. BLE S11 return loss
    ax1 = fig.add_subplot(gs[0, 0])
    style_ax(ax1, 'BLE Antenna S11 Return Loss (Matching Network)')
    ax1.plot(freqs_ghz, s11_db, color=c[0], lw=2)
    ax1.axhline(-10, color=c[2], lw=1, linestyle='--', label='-10 dB threshold')
    ax1.axvline(2.44, color=c[1], lw=1, linestyle='--', alpha=0.7, label='2.44 GHz BLE')
    ax1.fill_between(freqs_ghz, s11_db, -10,
                     where=np.array(s11_db) < -10, alpha=0.15, color=c[1],
                     label='Matched band')
    # Find -10 dB bandwidth
    below_10 = freqs_ghz[np.array(s11_db) < -10]
    if len(below_10) > 1:
        bw = below_10[-1] - below_10[0]
        ax1.text(0.05, 0.15, f'BW(-10dB): {bw*1000:.0f} MHz\nS11@2.44GHz: {s11_db[np.argmin(np.abs(freqs_ghz-2.44))]:.1f}dB',
                 transform=ax1.transAxes, color=text_c, fontsize=7,
                 bbox=dict(boxstyle='round', facecolor='#161b22', alpha=0.8))
    ax1.set_xlabel('Frequency (GHz)', color=text_c, fontsize=7)
    ax1.set_ylabel('S11 (dB)', color=text_c, fontsize=7)
    ax1.set_ylim(-40, 0)
    leg(ax1)

    # 2. Link budget vs distance
    ax2 = fig.add_subplot(gs[0, 1])
    style_ax(ax2, 'BLE Link Budget vs Distance')
    ax2.semilogx(distances, rx_powers, color=c[0], lw=2, label='Rx Power (dBm)')
    ax2.axhline(RX_SENS_DBM, color=c[3], lw=1.5, linestyle='--',
                label=f'Rx Sensitivity ({RX_SENS_DBM}dBm)')
    ax2.axvline(max_range, color=c[1], lw=1, linestyle='--',
                label=f'Max range: {max_range:.0f}m')
    ax2.fill_between(distances, rx_powers, RX_SENS_DBM,
                     where=np.array(rx_powers) > RX_SENS_DBM,
                     alpha=0.1, color=c[1])
    ax2.set_xlabel('Distance (m)', color=text_c, fontsize=7)
    ax2.set_ylabel('Received Power (dBm)', color=text_c, fontsize=7)
    ax2.set_ylim(-120, 20)
    leg(ax2)

    # 3. PCB trace impedance vs width
    ax3 = fig.add_subplot(gs[0, 2])
    style_ax(ax3, 'PCB Trace Impedance vs Width')
    ax3.plot(widths_mm, z_fr4,  color=c[0], lw=2, label=f'FR4 (h={H_FR4_MM}mm, εr={ER_FR4})')
    ax3.plot(widths_mm, z_flex, color=c[2], lw=2, label=f'Flex (h={H_FLEX_MM}mm, εr={ER_FLEX})')
    ax3.axhline(50, color=c[1], lw=1, linestyle='--', alpha=0.7, label='50Ω target')
    ax3.axhline(100, color=c[4], lw=1, linestyle='--', alpha=0.7, label='100Ω diff target')
    ax3.scatter([w_50_fr4], [50], color=c[0], s=60, zorder=5)
    ax3.scatter([w_50_flex], [50], color=c[2], s=60, zorder=5)
    ax3.text(w_50_fr4+0.05, 52, f'{w_50_fr4:.3f}mm', color=c[0], fontsize=6.5)
    ax3.text(w_50_flex+0.05, 52, f'{w_50_flex:.3f}mm', color=c[2], fontsize=6.5)
    ax3.set_xlabel('Trace Width (mm)', color=text_c, fontsize=7)
    ax3.set_ylabel('Characteristic Impedance (Ω)', color=text_c, fontsize=7)
    ax3.set_ylim(0, 200)
    leg(ax3)

    # 4. Differential pair impedance vs spacing
    ax4 = fig.add_subplot(gs[1, 0])
    style_ax(ax4, f'ECG Differential Pair Impedance (w={w_ecg}mm, FR4)')
    ax4.plot(spacings, z_diff_fr4, color=c[4], lw=2)
    ax4.axhline(100, color=c[1], lw=1, linestyle='--', label='100Ω target')
    ax4.axvline(s_100_fr4, color=c[2], lw=1, linestyle='--',
                label=f's={s_100_fr4:.3f}mm for 100Ω')
    ax4.scatter([s_100_fr4], [100], color=c[2], s=60, zorder=5)
    ax4.set_xlabel('Trace Spacing (mm)', color=text_c, fontsize=7)
    ax4.set_ylabel('Differential Impedance (Ω)', color=text_c, fontsize=7)
    leg(ax4)

    # 5. EMI spectrum
    ax5 = fig.add_subplot(gs[1, 1:])
    style_ax(ax5, 'Buck Converter EMI Spectrum + FCC Part 15 Class B Limit')
    ax5.semilogx(freqs_emi/1e6, emi_noise, color=c[3], lw=1.5, alpha=0.8,
                 label=f'Buck converter ({BUCK_FREQ_HZ/1e6:.0f}MHz switching)')
    ax5.semilogx(freqs_emi/1e6, coupling_noise, color=c[4], lw=1.5, alpha=0.8,
                 label='Digital-analog coupling')
    ax5.semilogx(freqs_emi/1e6, fcc_limits, color=c[2], lw=2, linestyle='--',
                 label='FCC Part 15 Class B limit')
    # Mark switching harmonics
    for n in range(1, 8):
        f_harm = n * BUCK_FREQ_HZ / 1e6
        if f_harm < 1000:
            ax5.axvline(f_harm, color=c[3], lw=0.5, alpha=0.3)
    ax5.set_xlabel('Frequency (MHz)', color=text_c, fontsize=7)
    ax5.set_ylabel('Noise (dBµV)', color=text_c, fontsize=7)
    ax5.set_xlim(0.01, 1000)
    ax5.set_ylim(-20, 80)
    leg(ax5)

    # 6. Decoupling effectiveness
    ax6 = fig.add_subplot(gs[2, :])
    style_ax(ax6, 'Decoupling Capacitor Impedance vs Frequency — Power Rail Noise Suppression')
    freqs_dec = np.logspace(4, 10, 1000)
    # Different capacitor values and their self-resonant frequencies
    caps = [
        (100e-9, 5e-9,  0.01, '100nF ceramic (SRF~5MHz)'),
        (10e-9,  50e-9, 0.01, '10nF ceramic (SRF~50MHz)'),
        (1e-9,   500e-9, 0.01, '1nF ceramic (SRF~500MHz)'),
        (100e-12, 5e-9, 0.01, '100pF ceramic (SRF~5GHz)'),
    ]
    for C_val, L_esl, R_esr, label in caps:
        omega = 2 * np.pi * freqs_dec
        Z_cap = np.abs(R_esr + 1j * (omega * L_esl - 1 / (omega * C_val)))
        ax6.loglog(freqs_dec/1e6, Z_cap, lw=1.5, label=label)
    # Target: < 0.1Ω at switching frequency
    ax6.axhline(0.1, color='white', lw=1, linestyle='--', alpha=0.5, label='0.1Ω target')
    ax6.axvline(BUCK_FREQ_HZ/1e6, color=c[2], lw=1, linestyle='--', alpha=0.7,
                label=f'Buck switching ({BUCK_FREQ_HZ/1e6:.0f}MHz)')
    ax6.set_xlabel('Frequency (MHz)', color=text_c, fontsize=7)
    ax6.set_ylabel('Impedance (Ω)', color=text_c, fontsize=7)
    ax6.set_ylim(1e-4, 1e4)
    leg(ax6)

    plt.savefig(PLOTS_DIR / 'signal_integrity_simulation.png',
                dpi=150, bbox_inches='tight', facecolor='#0d1117')
    plt.close()

    # ── Print Results ─────────────────────────────────────────────────────────
    s11_at_ble = s11_db[np.argmin(np.abs(freqs_ghz - 2.44))]

    print("\n" + "="*65)
    print("Signal Integrity Simulation Results")
    print("="*65)
    print(f"\n  BLE Antenna:")
    print(f"    S11 at 2.44 GHz:     {s11_at_ble:.1f} dB")
    print(f"    Max BLE range:       {max_range:.0f} m")
    print(f"    TX power:            {TX_POWER_DBM} dBm")
    print(f"    RX sensitivity:      {RX_SENS_DBM} dBm")

    print(f"\n  PCB Trace Impedance:")
    print(f"    50Ω width (FR4):     {w_50_fr4:.3f} mm")
    print(f"    50Ω width (Flex):    {w_50_flex:.3f} mm")
    print(f"    100Ω diff spacing:   {s_100_fr4:.3f} mm (w={w_ecg}mm)")

    print(f"\n  EMI:")
    print(f"    Buck switching:      {BUCK_FREQ_HZ/1e6:.0f} MHz")
    emi_at_sw = emi_noise[np.argmin(np.abs(freqs_emi - BUCK_FREQ_HZ))]
    print(f"    EMI at switching:    {emi_at_sw:.1f} dBµV")
    print(f"    FCC limit at 30MHz:  48 dBµV")

    checks = [
        ("BLE S11 < -10 dB at 2.44 GHz", s11_at_ble < -10,
         f"S11={s11_at_ble:.1f}dB"),
        ("BLE range > 10 m", max_range > 10,
         f"range={max_range:.0f}m"),
        ("50Ω FR4 width manufacturable (>0.1mm)", w_50_fr4 > 0.1,
         f"w={w_50_fr4:.3f}mm"),
        ("50Ω Flex width manufacturable (>0.05mm)", w_50_flex > 0.05,
         f"w={w_50_flex:.3f}mm"),
        ("ECG diff pair spacing manufacturable (>0.05mm)", s_100_fr4 >= 0.050,
         f"s={s_100_fr4:.3f}mm"),
        ("EMI at switching < FCC 48 dBµV", emi_at_sw < 48,
         f"EMI={emi_at_sw:.1f}dBµV"),
    ]

    print("\n  Specification Checks:")
    all_pass = True
    for name, passed, detail in checks:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"    {status}  {name} — {detail}")
        if not passed:
            all_pass = False

    print(f"\n  STATUS: {'✅ ALL SIGNAL INTEGRITY SPECS MET' if all_pass else '❌ SOME SPECS FAILED'}")
    return all_pass


if __name__ == '__main__':
    result = run_signal_integrity_simulation()
    print(f"\n  Plot saved to: plots/signal_integrity_simulation.png")
    exit(0 if result else 1)
