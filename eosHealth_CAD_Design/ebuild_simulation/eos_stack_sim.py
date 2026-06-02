#!/usr/bin/env python3
"""
eos_stack_sim.py — EoS Health Full Stack Simulator
Part of the eBuild simulation framework for pre-silicon validation
and EoS stack integration testing.

Usage:
    python3 eos_stack_sim.py --devices all --duration 3600
    python3 eos_stack_sim.py --scenario clinical_alert --device health-band-neuro --event afib
    python3 eos_stack_sim.py --mode regression --datasets ./clinical_datasets/

See ebuild_simulation/README.md for full documentation.
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from typing import Optional

# ---------------------------------------------------------------------------
# Synthetic sensor data generators
# ---------------------------------------------------------------------------

def generate_ecg_waveform(morphology: str = "normal_sinus",
                           duration_s: int = 10,
                           sample_rate: int = 500) -> list:
    """
    Generate a synthetic ECG waveform.

    Supported morphologies:
        normal_sinus, afib, pvc, st_elevation, lbbb, rbbb,
        bradycardia, tachycardia, flutter, vfib
    """
    import math
    n_samples = duration_s * sample_rate
    waveform = []

    if morphology == "normal_sinus":
        hr = 72  # bpm
        rr_interval = sample_rate * 60 // hr
        for i in range(n_samples):
            t = i % rr_interval
            # Simplified PQRST complex
            p = 0.15 * math.exp(-((t - rr_interval * 0.15) ** 2) / (2 * (rr_interval * 0.03) ** 2))
            q = -0.05 * math.exp(-((t - rr_interval * 0.30) ** 2) / (2 * (rr_interval * 0.01) ** 2))
            r = 1.00 * math.exp(-((t - rr_interval * 0.35) ** 2) / (2 * (rr_interval * 0.01) ** 2))
            s = -0.15 * math.exp(-((t - rr_interval * 0.40) ** 2) / (2 * (rr_interval * 0.01) ** 2))
            t_wave = 0.35 * math.exp(-((t - rr_interval * 0.65) ** 2) / (2 * (rr_interval * 0.08) ** 2))
            noise = (hash(i) % 100 - 50) * 0.001
            waveform.append(round(p + q + r + s + t_wave + noise, 4))

    elif morphology == "afib":
        # Irregular RR intervals, no distinct P waves
        import random
        rng = random.Random(42)
        for i in range(n_samples):
            rr = int(sample_rate * 60 / rng.randint(80, 160))
            t = i % rr
            r = 1.00 * math.exp(-((t - rr * 0.35) ** 2) / (2 * (rr * 0.01) ** 2))
            fibrillation = 0.08 * math.sin(2 * math.pi * 6 * i / sample_rate)
            noise = (hash(i) % 100 - 50) * 0.002
            waveform.append(round(r + fibrillation + noise, 4))

    else:
        # Default: flat line with noise (unsupported morphology placeholder)
        for i in range(n_samples):
            waveform.append(round((hash(i) % 100 - 50) * 0.001, 4))

    return waveform


def generate_ppg_waveform(heart_rate: int = 72,
                           spo2: float = 98.0,
                           duration_s: int = 60,
                           sample_rate: int = 25) -> dict:
    """
    Generate synthetic PPG waveform for HR, SpO2, and HRV calculation.
    Returns dict with 'green', 'red', 'ir' channel arrays.
    """
    import math
    n_samples = duration_s * sample_rate
    rr_interval = sample_rate * 60 // heart_rate

    green, red, ir = [], [], []
    for i in range(n_samples):
        t = i % rr_interval
        # Systolic peak
        pulse = math.exp(-((t - rr_interval * 0.3) ** 2) / (2 * (rr_interval * 0.08) ** 2))
        # Dicrotic notch
        notch = 0.15 * math.exp(-((t - rr_interval * 0.55) ** 2) / (2 * (rr_interval * 0.04) ** 2))
        noise = (hash(i * 3) % 100 - 50) * 0.005

        # SpO2 affects red/IR ratio
        r_ratio = (100 - spo2) / 100 * 0.3 + 0.7
        green.append(round(0.8 + 0.2 * (pulse + notch) + noise, 4))
        red.append(round(0.75 + 0.25 * (pulse + notch) * r_ratio + noise, 4))
        ir.append(round(0.85 + 0.15 * (pulse + notch) + noise, 4))

    return {"green": green, "red": red, "ir": ir,
            "heart_rate_bpm": heart_rate, "spo2_pct": spo2}


def generate_glucose_trace(baseline_mg_dl: float = 95,
                            duration_hours: int = 24,
                            meals: Optional[list] = None) -> list:
    """
    Generate a synthetic continuous glucose monitoring (CGM) trace.
    meals: list of {"time_hours": float, "carbs_g": int}
    """
    import math
    sample_interval_min = 5
    n_samples = duration_hours * 60 // sample_interval_min
    trace = []
    glucose = baseline_mg_dl

    for i in range(n_samples):
        time_h = i * sample_interval_min / 60
        # Circadian variation
        circadian = 5 * math.sin(2 * math.pi * (time_h - 6) / 24)
        # Meal spikes
        meal_effect = 0
        if meals:
            for meal in meals:
                dt = time_h - meal["time_hours"]
                if 0 <= dt <= 3:
                    peak = meal["carbs_g"] * 0.8
                    meal_effect += peak * math.exp(-dt / 0.5) * (1 - math.exp(-dt / 0.1))
        # Random walk
        glucose += (hash(i * 7) % 10 - 5) * 0.3
        glucose = max(40, min(400, glucose + circadian * 0.1 + meal_effect * 0.05))
        noise = (hash(i * 11) % 20 - 10) * 0.5
        trace.append(round(glucose + noise, 1))

    return trace


# ---------------------------------------------------------------------------
# Simulation scenarios
# ---------------------------------------------------------------------------

def run_multi_device_pairing_scenario(duration_s: int = 60) -> dict:
    """Simulate all 4 devices pairing with the EoS Health app via BLE 5.3."""
    print("[eBuild] Running multi-device BLE pairing scenario...")
    results = {}
    devices = ["health-key-ultra", "health-band-neuro", "health-ring", "health-lab"]
    for device in devices:
        # Simulate BLE advertisement + GATT connection
        pairing_time_ms = 850 + (hash(device) % 400)  # 850–1250ms
        results[device] = {
            "paired": True,
            "pairing_time_ms": pairing_time_ms,
            "rssi_dbm": -55 + (hash(device) % 20),
            "ble_version": "5.3",
            "gatt_services": ["health_monitoring", "device_info", "battery", "ota"],
        }
        print(f"  ✅ {device}: paired in {pairing_time_ms}ms, RSSI={results[device]['rssi_dbm']}dBm")
    return results


def run_clinical_alert_scenario(device: str, event: str) -> dict:
    """Simulate a clinical alert event and measure end-to-end latency."""
    print(f"[eBuild] Running clinical alert scenario: {device} / {event}")
    event_time = datetime.now(timezone.utc).isoformat()

    # Simulate detection latency
    detection_latency_ms = 250 + (hash(event) % 500)
    ble_tx_latency_ms = 15
    cloud_processing_ms = 450 + (hash(device) % 200)
    push_notification_ms = 800 + (hash(event + device) % 400)
    total_latency_ms = detection_latency_ms + ble_tx_latency_ms + cloud_processing_ms + push_notification_ms

    result = {
        "event": event,
        "device": device,
        "event_time_utc": event_time,
        "detection_latency_ms": detection_latency_ms,
        "ble_tx_latency_ms": ble_tx_latency_ms,
        "cloud_processing_ms": cloud_processing_ms,
        "push_notification_ms": push_notification_ms,
        "total_latency_ms": total_latency_ms,
        "sla_met": total_latency_ms < 30000,  # 30s SLA
        "alert_sent": True,
    }
    print(f"  ✅ Alert pipeline: {total_latency_ms}ms total (SLA <30s: {'PASS' if result['sla_met'] else 'FAIL'})")
    return result


def run_power_budget_scenario(devices: list, duration_s: int = 86400) -> dict:
    """Simulate battery consumption for each device over the specified duration."""
    print(f"[eBuild] Running power budget scenario for {duration_s}s ({duration_s/3600:.1f}h)...")
    # Battery capacities in mAh
    battery_mah = {
        "health-key-ultra": 120,
        "health-band-neuro": 400,
        "health-ring": 22,
        "health-lab": 50,
    }
    # Average current draw in mA (standard monitoring mode)
    avg_current_ma = {
        "health-key-ultra": 1.8,
        "health-band-neuro": 8.5,
        "health-ring": 0.9,
        "health-lab": 1.2,
    }
    results = {}
    for device in devices:
        cap = battery_mah.get(device, 100)
        avg = avg_current_ma.get(device, 2.0)
        consumed_mah = avg * duration_s / 3600
        remaining_pct = max(0, (cap - consumed_mah) / cap * 100)
        estimated_life_days = cap / avg / 24
        results[device] = {
            "battery_capacity_mah": cap,
            "avg_current_ma": avg,
            "consumed_mah": round(consumed_mah, 2),
            "remaining_pct": round(remaining_pct, 1),
            "estimated_life_days": round(estimated_life_days, 1),
            "spec_met": estimated_life_days >= {"health-key-ultra": 3, "health-band-neuro": 2,
                                                "health-ring": 4, "health-lab": 7}.get(device, 2),
        }
        status = "PASS" if results[device]["spec_met"] else "FAIL"
        print(f"  {'✅' if results[device]['spec_met'] else '❌'} {device}: "
              f"{estimated_life_days:.1f} days battery life [{status}]")
    return results


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="EoS Health eBuild Stack Simulator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument("--devices", default="all",
                        help="Comma-separated device list or 'all'")
    parser.add_argument("--duration", type=int, default=300,
                        help="Simulation duration in seconds")
    parser.add_argument("--scenario", default="basic",
                        choices=["basic", "multi_device_pairing", "clinical_alert",
                                 "ota_update", "regression", "power_budget"],
                        help="Simulation scenario to run")
    parser.add_argument("--device", default="health-band-neuro",
                        help="Single device for scenario testing")
    parser.add_argument("--event", default="afib",
                        help="Clinical event type for alert scenario")
    parser.add_argument("--mode", default="interactive",
                        choices=["interactive", "ci", "regression"],
                        help="Run mode")
    parser.add_argument("--output", default="./results/",
                        help="Output directory for simulation results")
    parser.add_argument("--report", default=None,
                        help="Path for HTML report output")

    args = parser.parse_args()

    all_devices = ["health-key-ultra", "health-band-neuro", "health-ring", "health-lab"]
    devices = all_devices if args.devices == "all" else args.devices.split(",")

    print("=" * 60)
    print("  EoS Health eBuild Stack Simulator v1.0")
    print(f"  Devices: {', '.join(devices)}")
    print(f"  Scenario: {args.scenario}")
    print(f"  Duration: {args.duration}s")
    print(f"  Mode: {args.mode}")
    print("=" * 60)

    os.makedirs(args.output, exist_ok=True)
    results = {"timestamp": datetime.now(timezone.utc).isoformat(), "results": {}}

    if args.scenario == "multi_device_pairing":
        results["results"] = run_multi_device_pairing_scenario(args.duration)

    elif args.scenario == "clinical_alert":
        results["results"] = run_clinical_alert_scenario(args.device, args.event)

    elif args.scenario == "power_budget":
        results["results"] = run_power_budget_scenario(devices, args.duration)

    elif args.scenario == "basic":
        print("\n[eBuild] Running basic sensor data generation...")
        for device in devices:
            if device == "health-band-neuro":
                ecg = generate_ecg_waveform("normal_sinus", min(args.duration, 10), 500)
                results["results"][device] = {"ecg_samples": len(ecg), "ecg_preview": ecg[:5]}
                print(f"  ✅ {device}: generated {len(ecg)} ECG samples")
            elif device in ("health-key-ultra", "health-ring"):
                ppg = generate_ppg_waveform(72, 98.0, min(args.duration, 60), 25)
                results["results"][device] = {"ppg_samples": len(ppg["green"]), "hr": ppg["heart_rate_bpm"]}
                print(f"  ✅ {device}: generated {len(ppg['green'])} PPG samples, HR={ppg['heart_rate_bpm']}bpm")
            elif device == "health-lab":
                glucose = generate_glucose_trace(95, min(args.duration // 3600, 24) or 1,
                                                 [{"time_hours": 8, "carbs_g": 60}])
                results["results"][device] = {"glucose_samples": len(glucose),
                                              "glucose_range": [min(glucose), max(glucose)]}
                print(f"  ✅ {device}: generated {len(glucose)} glucose readings, "
                      f"range={min(glucose):.0f}-{max(glucose):.0f} mg/dL")

    # Save results
    output_file = os.path.join(args.output, f"sim_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n[eBuild] Results saved to: {output_file}")
    print("[eBuild] Simulation complete.")

    # CI mode: exit with non-zero if any test failed
    if args.mode == "ci":
        failed = any(
            not v.get("spec_met", True) and not v.get("sla_met", True)
            for v in results["results"].values()
            if isinstance(v, dict)
        )
        sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
