# eMedical — eBuild Simulation

## Simulation Targets

| Product | Simulation Type | eOS Module |
|---|---|---|
| diagnostic_equipment | Signal chain noise, power budget | eOS Medical HAL |
| surgical_devices | Real-time control loop, safety monitoring | eOS RT, eOS Safety |
| patient_care | Alarm system, battery backup | eOS Medical, eOS Power |
| laboratory_equipment | Thermal PID, optical detection | eOS Lab |

## Running Simulations
```bash
cd eMedical_CAD_Design/{product}/simulation/
python3 power_budget_sim.py
```
