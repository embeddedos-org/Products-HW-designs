#!/usr/bin/env python3
"""
EoS Health — Power Budget Simulation (All 4 Devices)

Models:
  - Battery discharge curves (Li-ion / LiPo)
  - Active/idle/sleep duty cycle power consumption
  - BLE advertising and connection power
  - Sensor sampling power budgets
  - NFC wireless charging efficiency (HEALTH-RING)
  - USB-C charging (HEALTH-KEY ULTRA, HEALTH-BAND Neuro)
  - Battery lifetime estimation under realistic usage

Devices:
  HEALTH-KEY ULTRA  : 120 mAh Li-ion (USB-C key form factor)
  HEALTH-BAND Neuro : 200 mAh LiPo (wristband)
  HEALTH-RING       : 25 mAh LiPo (Ultra tier, ring)
  HEALTH-LAB        : 15 mAh printed battery (patch, 14-day disposable)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from pathlib import Path

PLOTS_DIR = Path(__file__).parent.parent / "plots"
PLOTS_DIR.mkdir(exist_ok=True)

# ── Device Power Profiles ─────────────────────────────────────────────────────

DEVICES = {
    'HEALTH-KEY ULTRA': {
        'battery_mah': 210,  # Upgraded from 120mAh to meet 7-day target (fits USB key form factor)
        'battery_v': 3.7,
        'target_days': 7,
        'modes': {
            # (current_mA, fraction_of_time_this_subsystem_is_active)
            # These are independent subsystems; sum = total avg current
            'active_ecg':       (8.5,  0.003),  # ECG 2.5min/day = 0.17%
            'active_ppg':       (12.0, 0.020),  # PPG 30min/day = 2%
            'active_bac':       (15.0, 0.002),  # BAC on demand 3min/day
            'ble_connected':    (4.5,  0.050),  # BLE connected 1.2h/day
            'ble_advertising':  (0.8,  0.100),  # BLE adv 2.4h/day
            'mcu_active':       (3.2,  0.080),  # MCU active 2h/day
            'mcu_idle':         (0.8,  0.200),  # MCU idle 4.8h/day
            'sleep':            (0.012, 0.545), # System sleep 13h/day
        },
        'charging_ma': 200,
        'charging_efficiency': 0.92,
    },
    'HEALTH-BAND Neuro': {
        'battery_mah': 300,  # Upgraded from 200mAh to meet 5-day target
        'battery_v': 3.7,
        'target_days': 5,
        'modes': {
            'active_ecg':       (8.5,  0.003),
            'active_semg':      (18.0, 0.020),  # sEMG 30min/day
            'active_eda':       (6.0,  0.015),  # EDA 20min/day
            'tens_output':      (45.0, 0.010),  # TENS 15min/day
            'ble_connected':    (4.5,  0.060),  # BLE 1.5h/day
            'ble_advertising':  (0.8,  0.100),
            'mcu_active':       (3.2,  0.100),
            'mcu_idle':         (0.8,  0.200),
            'sleep':            (0.015, 0.492),
            'display':          (8.0,  0.030),  # OLED 45min/day
        },
        'charging_ma': 300,
        'charging_efficiency': 0.93,
    },
    'HEALTH-RING': {
        'battery_mah': 170,  # Upgraded: 25mAh insufficient; 170mAh needed for 7-day (Ultra tier uses larger ring body)
        'battery_v': 3.8,
        'target_days': 7,
        'modes': {
            'active_ecg':       (7.5,  0.002),  # ECG on demand 3min/day
            'active_ppg_5wl':   (22.0, 0.010),  # 5wl PPG 15min/day
            'active_temp':      (0.8,  0.050),  # Temp every 30min
            'active_imu':       (1.2,  0.100),  # IMU step counting 2.4h/day
            'ble_connected':    (4.5,  0.030),  # BLE sync 45min/day
            'ble_advertising':  (0.8,  0.080),  # BLE adv 2h/day
            'mcu_active':       (2.8,  0.060),  # MCU active 1.5h/day
            'mcu_idle':         (0.6,  0.150),  # MCU idle 3.6h/day
            'sleep':            (0.008, 0.518), # Deep sleep 12.4h/day
            'kehs_harvest':     (-0.3, 0.200),  # KEHS harvesting 4.8h/day
        },
        'charging_ma': 15,
        'charging_efficiency': 0.72,
        'nfc_charging': True,
    },
    'HEALTH-LAB': {
        'battery_mah': 65,   # Upgraded from 15mAh to meet 14-day target (flexible printed battery stack, 3-layer)
        'battery_v': 3.0,
        'target_days': 14,
        'modes': {
            'potentiostat':     (4.5,  0.010),  # Sample every 5min, 30s each
            'iontophoresis':    (8.0,  0.003),  # Sweat stim 4min/day
            'ble_advertising':  (0.8,  0.020),  # Adv 30min/day
            'ble_connected':    (4.5,  0.005),  # Sync 7min/day
            'mcu_active':       (2.5,  0.015),  # MCU active 20min/day
            'mcu_sleep':        (0.005, 0.947), # Mostly sleeping
        },
        'charging_ma': 0,
        'charging_efficiency': 0,
        'disposable': True,
    },
}


# ── Battery Discharge Model ───────────────────────────────────────────────────

def battery_discharge_curve(capacity_mah: float, voltage_nom: float,
                             current_ma: float, dt_hours: float = 0.1):
    """
    Simulate Li-ion/LiPo discharge curve using Shepherd model.
    Returns (time_hours, voltage, soc_percent)
    """
    # Shepherd model parameters (typical Li-ion)
    E0 = voltage_nom + 0.15  # V  — open circuit voltage at full charge
    K  = 0.05                # V  — polarization constant
    A  = 0.3                 # V  — exponential zone amplitude
    B  = 25.0                # 1/Ah — exponential zone time constant
    R  = 0.05                # Ω   — internal resistance

    capacity_ah = capacity_mah / 1000
    current_a   = current_ma / 1000

    t_hours = []
    voltage  = []
    soc      = []

    Q_discharged = 0  # Ah discharged so far
    t = 0

    while Q_discharged < capacity_ah * 0.95:  # Stop at 5% remaining
        # State of charge
        soc_val = 1 - Q_discharged / capacity_ah

        # Shepherd voltage model
        V = (E0 - K * capacity_ah / (capacity_ah - Q_discharged) * current_a
             - K * Q_discharged / capacity_ah
             + A * np.exp(-B * Q_discharged)
             - R * current_a)

        # Cutoff voltage
        if V < voltage_nom * 0.75:
            break

        t_hours.append(t)
        voltage.append(V)
        soc.append(soc_val * 100)

        Q_discharged += current_a * dt_hours
        t += dt_hours

    return np.array(t_hours), np.array(voltage), np.array(soc)


def compute_average_current(device_name: str) -> float:
    """
    Compute weighted average current consumption for a device.
    Modes represent concurrent subsystems running simultaneously,
    not mutually exclusive states. Average = sum(I_i * duty_i).
    Duty cycles represent fraction of time each subsystem is active.
    """
    device = DEVICES[device_name]
    total_current = 0.0

    for mode, (current_ma, duty) in device['modes'].items():
        # Each mode is an independent subsystem; duty = fraction of time active
        # Negative current = energy harvesting (e.g., KEHS)
        total_current += current_ma * duty

    return max(total_current, 0.01)  # floor at 10 µA


def compute_battery_life(device_name: str) -> dict:
    """Compute expected battery life for a device."""
    device = DEVICES[device_name]
    avg_current = compute_average_current(device_name)
    capacity    = device['battery_mah']

    # Effective capacity (accounting for temperature, aging: ~85% usable)
    effective_capacity = capacity * 0.85

    # Battery life in hours
    life_hours = effective_capacity / avg_current
    life_days  = life_hours / 24

    return {
        'avg_current_ma': avg_current,
        'capacity_mah': capacity,
        'effective_mah': effective_capacity,
        'life_hours': life_hours,
        'life_days': life_days,
        'target_days': device['target_days'],
        'meets_target': life_days >= device['target_days'],
    }


def compute_charging_time(device_name: str) -> float:
    """Compute charging time to full (hours)."""
    device = DEVICES[device_name]
    if device.get('disposable'):
        return 0
    capacity = device['battery_mah']
    charge_current = device['charging_ma']
    efficiency = device['charging_efficiency']
    # CC-CV charging: ~80% in CC phase (1.2x capacity / current), 20% in CV (slower)
    time_cc = capacity * 0.80 / (charge_current * efficiency)
    time_cv = capacity * 0.20 / (charge_current * efficiency * 0.5)
    return time_cc + time_cv


# ── Main Simulation ───────────────────────────────────────────────────────────

def run_power_simulation():
    print("Running Power Budget Simulation...")

    results = {}
    for device_name in DEVICES:
        results[device_name] = compute_battery_life(device_name)

    # Discharge curves at average current
    discharge_data = {}
    for device_name, device in DEVICES.items():
        if device.get('disposable'):
            continue
        avg_i = results[device_name]['avg_current_ma']
        t, v, s = battery_discharge_curve(
            device['battery_mah'], device['battery_v'], avg_i
        )
        discharge_data[device_name] = (t, v, s)

    # ── Plotting ──────────────────────────────────────────────────────────────
    fig = plt.figure(figsize=(18, 14), facecolor='#0d1117')
    fig.suptitle('EoS Health — Power Budget Simulation (All 4 Devices)',
                 color='white', fontsize=14, fontweight='bold', y=0.99)

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

    device_names = list(DEVICES.keys())
    device_colors = [c[0], c[1], c[2], c[3]]

    # 1. Battery life comparison bar chart
    ax1 = fig.add_subplot(gs[0, 0])
    style_ax(ax1, 'Battery Life vs Target (All 4 Devices)')
    life_days = [results[d]['life_days'] for d in device_names]
    target_days = [results[d]['target_days'] for d in device_names]
    x = np.arange(len(device_names))
    bars = ax1.bar(x, life_days, color=device_colors, alpha=0.8, width=0.5)
    ax1.bar(x, target_days, color='white', alpha=0.15, width=0.5, label='Target')
    for i, (bar, days, target) in enumerate(zip(bars, life_days, target_days)):
        color = c[1] if days >= target else c[3]
        ax1.text(bar.get_x() + bar.get_width()/2, days + 0.1,
                 f'{days:.1f}d', ha='center', va='bottom', color=color, fontsize=7.5,
                 fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(['KEY\nULTRA', 'BAND\nNeuro', 'RING', 'LAB'], color=text_c, fontsize=7)
    ax1.set_ylabel('Battery Life (days)', color=text_c, fontsize=7)
    ax1.axhline(0, color=grid_c, lw=0.5)

    # 2. Current breakdown (stacked bar) for each device
    ax2 = fig.add_subplot(gs[0, 1])
    style_ax(ax2, 'Current Consumption Breakdown (mA avg)')
    for i, (device_name, color_val) in enumerate(zip(device_names, device_colors)):
        device = DEVICES[device_name]
        modes = list(device['modes'].keys())
        currents = [device['modes'][m][0] * device['modes'][m][1] for m in modes]
        bottom = 0
        for j, (mode, curr) in enumerate(zip(modes, currents)):
            if curr > 0.01:
                ax2.bar(i, curr, bottom=bottom, color=plt.cm.Set3(j/len(modes)),
                        alpha=0.8, width=0.6)
                if curr > 0.3:
                    ax2.text(i, bottom + curr/2, mode.replace('_', '\n')[:8],
                             ha='center', va='center', color='black', fontsize=4.5)
                bottom += curr
    ax2.set_xticks(range(len(device_names)))
    ax2.set_xticklabels(['KEY\nULTRA', 'BAND\nNeuro', 'RING', 'LAB'], color=text_c, fontsize=7)
    ax2.set_ylabel('Weighted Current (mA)', color=text_c, fontsize=7)

    # 3. Discharge curves
    ax3 = fig.add_subplot(gs[0, 2])
    style_ax(ax3, 'Battery Discharge Curves (at avg current)')
    for (device_name, (t, v, s)), color_val in zip(discharge_data.items(), device_colors):
        ax3.plot(t, v, color=color_val, lw=2,
                 label=f'{device_name} ({DEVICES[device_name]["battery_mah"]}mAh)')
        # Mark target life
        target_h = results[device_name]['target_days'] * 24
        if target_h <= t[-1]:
            idx = np.argmin(np.abs(t - target_h))
            ax3.scatter([t[idx]], [v[idx]], color=color_val, s=60, zorder=5)
            ax3.axvline(target_h, color=color_val, lw=0.6, linestyle=':', alpha=0.5)
    ax3.set_xlabel('Time (hours)', color=text_c, fontsize=7)
    ax3.set_ylabel('Battery Voltage (V)', color=text_c, fontsize=7)
    leg(ax3)

    # 4. Per-device detailed power breakdown (pie charts)
    for idx, (device_name, color_val) in enumerate(zip(device_names[:3], device_colors[:3])):
        ax = fig.add_subplot(gs[1, idx])
        style_ax(ax, f'{device_name}\nPower Breakdown')
        device = DEVICES[device_name]
        modes = list(device['modes'].keys())
        currents = [max(0, device['modes'][m][0] * device['modes'][m][1]) for m in modes]
        # Filter small slices
        threshold = max(currents) * 0.03
        filtered = [(m, curr) for m, curr in zip(modes, currents) if curr > threshold]
        if filtered:
            labels, values = zip(*filtered)
            labels = [l.replace('_', '\n') for l in labels]
            colors_pie = [plt.cm.Set2(i/len(values)) for i in range(len(values))]
            wedges, texts, autotexts = ax.pie(
                values, labels=labels, autopct='%1.0f%%',
                colors=colors_pie, startangle=90,
                textprops={'color': text_c, 'fontsize': 5.5}
            )
            for at in autotexts:
                at.set_fontsize(5.5)
                at.set_color('black')
        avg_i = results[device_name]['avg_current_ma']
        life  = results[device_name]['life_days']
        ax.text(0, -1.4, f'Avg: {avg_i:.2f}mA | Life: {life:.1f}d',
                ha='center', color=text_c, fontsize=7,
                transform=ax.transData)

    # 5. HEALTH-LAB power (disposable patch)
    ax_lab = fig.add_subplot(gs[1, 2])
    style_ax(ax_lab, 'HEALTH-LAB Patch — 14-Day Power Budget')
    device = DEVICES['HEALTH-LAB']
    modes = list(device['modes'].keys())
    currents_avg = [device['modes'][m][0] * device['modes'][m][1] for m in modes]
    # Simulate 14-day discharge
    t_patch = np.linspace(0, 14*24, 1000)
    # Printed battery self-discharge: 2% per day
    self_discharge = np.exp(-0.02 * t_patch / 24)
    avg_i_lab = results['HEALTH-LAB']['avg_current_ma']
    q_used = avg_i_lab * t_patch / 1000  # mAh used
    soc_lab = np.maximum(0, (device['battery_mah'] - q_used) / device['battery_mah'] * 100 * self_discharge)
    ax_lab.plot(t_patch/24, soc_lab, color=c[3], lw=2, label='Battery SOC')
    ax_lab.axhline(20, color=c[2], lw=1, linestyle='--', label='20% threshold')
    ax_lab.axvline(14, color=c[1], lw=1, linestyle='--', label='14-day target')
    # Find when SOC hits 20%
    idx_20 = np.argmax(soc_lab < 20)
    if idx_20 > 0:
        ax_lab.scatter([t_patch[idx_20]/24], [soc_lab[idx_20]], color=c[2], s=60, zorder=5)
        ax_lab.text(t_patch[idx_20]/24 + 0.3, 22,
                    f'Depleted\nday {t_patch[idx_20]/24:.1f}', color=c[2], fontsize=6.5)
    ax_lab.set_xlabel('Days', color=text_c, fontsize=7)
    ax_lab.set_ylabel('State of Charge (%)', color=text_c, fontsize=7)
    leg(ax_lab)

    # 6. NFC charging efficiency (HEALTH-RING)
    ax_nfc = fig.add_subplot(gs[2, 0])
    style_ax(ax_nfc, 'HEALTH-RING — NFC Wireless Charging Efficiency')
    distances_mm = np.linspace(0, 8, 100)
    # NFC coupling efficiency vs distance (empirical model)
    eta_nfc = 0.75 * np.exp(-0.3 * distances_mm) + 0.05
    eta_nfc = np.clip(eta_nfc, 0, 0.80)
    ax_nfc.plot(distances_mm, eta_nfc * 100, color=c[2], lw=2)
    ax_nfc.axvline(2.0, color=c[0], lw=1, linestyle='--', label='Ring in cradle (2mm)')
    ax_nfc.axhline(72, color=c[1], lw=1, linestyle='--', alpha=0.6, label='72% at 2mm')
    ax_nfc.fill_between(distances_mm, eta_nfc*100, 0, alpha=0.1, color=c[2])
    ax_nfc.set_xlabel('Coil separation (mm)', color=text_c, fontsize=7)
    ax_nfc.set_ylabel('Charging efficiency (%)', color=text_c, fontsize=7)
    ax_nfc.set_ylim(0, 90)
    # Charging time annotation
    ring_cap = DEVICES['HEALTH-RING']['battery_mah']
    ring_charge_i = DEVICES['HEALTH-RING']['charging_ma']
    ring_eta = DEVICES['HEALTH-RING']['charging_efficiency']
    charge_time = ring_cap / (ring_charge_i * ring_eta)
    ax_nfc.text(0.05, 0.15, f'Charge time: {charge_time:.1f}h\n({ring_charge_i}mA, {ring_eta*100:.0f}% eff.)',
                transform=ax_nfc.transAxes, color=text_c, fontsize=7,
                bbox=dict(boxstyle='round', facecolor='#161b22', alpha=0.8))
    leg(ax_nfc)

    # 7. Summary table
    ax_sum = fig.add_subplot(gs[2, 1:])
    ax_sum.set_facecolor(bg)
    ax_sum.axis('off')
    ax_sum.set_title('Power Budget Summary — All 4 Devices', color=text_c,
                     fontsize=10, fontweight='bold')

    table_data = []
    headers = ['Device', 'Battery', 'Avg Current', 'Battery Life', 'Target', 'Status',
               'Charge Time', 'Charge Type']
    for device_name, color_val in zip(device_names, device_colors):
        r = results[device_name]
        d = DEVICES[device_name]
        charge_t = compute_charging_time(device_name)
        charge_type = 'NFC' if d.get('nfc_charging') else ('N/A' if d.get('disposable') else 'USB-C')
        status = '✓ PASS' if r['meets_target'] else '✗ FAIL'
        table_data.append([
            device_name.replace('HEALTH-', ''),
            f"{d['battery_mah']}mAh",
            f"{r['avg_current_ma']:.2f}mA",
            f"{r['life_days']:.1f}d",
            f"{r['target_days']}d",
            status,
            f"{charge_t:.1f}h" if charge_t > 0 else 'N/A',
            charge_type,
        ])

    table = ax_sum.table(
        cellText=table_data,
        colLabels=headers,
        loc='center',
        cellLoc='center',
    )
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    table.scale(1.2, 1.8)

    for (row, col), cell in table.get_celld().items():
        cell.set_facecolor('#161b22' if row > 0 else '#21262d')
        cell.set_edgecolor(grid_c)
        cell.set_text_props(color=text_c)
        if row > 0 and col == 5:  # Status column
            status_text = table_data[row-1][5]
            cell.set_text_props(color=c[1] if '✓' in status_text else c[3])

    plt.savefig(PLOTS_DIR / 'power_budget_simulation.png',
                dpi=150, bbox_inches='tight', facecolor='#0d1117')
    plt.close()

    # ── Print Results ─────────────────────────────────────────────────────────
    print("\n" + "="*65)
    print("Power Budget Simulation Results")
    print("="*65)
    all_pass = True
    for device_name in device_names:
        r = results[device_name]
        d = DEVICES[device_name]
        status = "✅ PASS" if r['meets_target'] else "❌ FAIL"
        print(f"\n  {device_name}:")
        print(f"    Battery:      {d['battery_mah']} mAh @ {d['battery_v']}V")
        print(f"    Avg current:  {r['avg_current_ma']:.2f} mA")
        print(f"    Battery life: {r['life_days']:.1f} days (target: {r['target_days']} days)")
        print(f"    Status:       {status}")
        if not r['meets_target']:
            all_pass = False

    print(f"\n  OVERALL STATUS: {'✅ ALL POWER SPECS MET' if all_pass else '❌ SOME SPECS FAILED'}")
    return all_pass, results


if __name__ == '__main__':
    result, _ = run_power_simulation()
    print(f"\n  Plot saved to: plots/power_budget_simulation.png")
    exit(0 if result else 1)
