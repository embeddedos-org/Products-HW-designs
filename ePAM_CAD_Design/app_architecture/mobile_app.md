# ePAM Mobile App — Unified Vehicle Control

> **One app. Any vehicle. Full control.**
> Like Tesla app, but for drones, cars, shuttles, and trans-atmospheric craft.

## App Overview

```
+--------------------------------------------------+
|  9:41           ePAM           ...        87%     |
+--------------------------------------------------+
|                                                    |
|  Good morning, Srikanth                    [SP]   |
|  2 vehicles connected                             |
|                                                    |
|  +----------------------------------------------+ |
|  |  MY VEHICLES                                  | |
|  |                                               | |
|  |  +------------------+  +------------------+   | |
|  |  | [drone icon]     |  | [car icon]       |   | |
|  |  | Urban Drone      |  | Eco Car          |   | |
|  |  | "Sky Runner"     |  | "Sol"            |   | |
|  |  |                  |  |                  |   | |
|  |  | @ Vertiport SFO  |  | @ Home Garage    |   | |
|  |  | Battery: 82%     |  | Battery: 94%     |   | |
|  |  | Solar: +2.1kW    |  | Solar: +0.8kW    |   | |
|  |  | Status: PARKED   |  | Status: CHARGING |   | |
|  |  | Locked           |  | Locked           |   | |
|  |  +------------------+  +------------------+   | |
|  +----------------------------------------------+ |
|                                                    |
|  +----------------------------------------------+ |
|  |  QUICK ACTIONS                                | |
|  |  +--------+  +--------+  +--------+          | |
|  |  | Summon |  | Climate|  | Locate |          | |
|  |  +--------+  +--------+  +--------+          | |
|  |  +--------+  +--------+  +--------+          | |
|  |  | Lock   |  | Charge |  | Share  |          | |
|  |  +--------+  +--------+  +--------+          | |
|  +----------------------------------------------+ |
|                                                    |
|  +----------------------------------------------+ |
|  |  FLEET OVERVIEW                               | |
|  |  Total solar harvest today: 18.4 kWh          | |
|  |  V2G earnings this month: $42.30              | |
|  |  Next service: Eco Car in 12 days             | |
|  |  Software update: v2.4.1 available            | |
|  +----------------------------------------------+ |
|                                                    |
+--------------------------------------------------+
|  Home    Control   Fly    Energy   Profile         |
|   .                                                |
+--------------------------------------------------+
```

## Vehicle Selection & Auto-Detection

When you approach any ePAM vehicle, the app auto-detects via BLE and switches to that vehicle's control panel — just like Tesla.

```
DETECTION FLOW

  User walks toward vehicle
         |
         v
  [BLE beacon detected]  <-- Each vehicle broadcasts unique ID
         |
         v
  [Distance < 10m?] -- No --> Show vehicle list
         |
        Yes
         |
         v
  [Auto-switch to vehicle control panel]
         |
         v
  [Show: Unlock / Climate / Status]
         |
         v
  [Distance < 2m?] -- Yes --> Auto-unlock (if enabled)
```

## Tab Navigation

| Tab | Icon | Function |
|-----|------|----------|
| **Home** | House | Vehicle list, quick actions, fleet overview |
| **Control** | Steering wheel | Full vehicle control panel (per vehicle) |
| **Fly** | Wings | Flight planning, route, airspace (drone/shuttle/combo) |
| **Energy** | Lightning | Solar harvest, battery, H2 level, V2G, charging |
| **Profile** | Person | Account, subscription, service, OTA updates |

---

## Control Tab — Per-Vehicle Panels

### Eco Car Control (Tesla-like)

```
+--------------------------------------------------+
|  < Back         Eco Car "Sol"            [share]  |
+--------------------------------------------------+
|                                                    |
|         +------------------------------+          |
|         |                              |          |
|         |      [TOP-DOWN CAR VIEW]     |          |
|         |                              |          |
|         |   FL: 36 psi    FR: 36 psi   |          |
|         |                              |          |
|         |        UNLOCKED              |          |
|         |                              |          |
|         |   RL: 35 psi    RR: 35 psi   |          |
|         |                              |          |
|         +------------------------------+          |
|                                                    |
|  +------+ +------+ +------+ +------+ +------+    |
|  |UNLOCK| |START | |CLIMA | |TRUNK | |SUMMON|    |
|  +------+ +------+ +------+ +------+ +------+    |
|                                                    |
|  CLIMATE                               21 C       |
|  +--------------------------------------------+   |
|  |  [------|--------]  Fan: Auto               |   |
|  |  Lo              Hi                         |   |
|  |  [x] Seat heat L   [x] Seat heat R         |   |
|  |  [ ] Defrost        [x] Auto                |   |
|  +--------------------------------------------+   |
|                                                    |
|  CHARGING                                          |
|  +--------------------------------------------+   |
|  |  Battery: 94%  ||||||||||||||||||||--        |   |
|  |  Range: 470 km                              |   |
|  |  Charging: 11 kW (home AC)                  |   |
|  |  Full at: 6:30 AM                           |   |
|  |  Solar today: +4.2 kWh (28 km added)        |   |
|  |  [Set charge limit: 90%]                    |   |
|  +--------------------------------------------+   |
|                                                    |
|  LOCATION                                          |
|  +--------------------------------------------+   |
|  |  [========= MAP =========]                  |   |
|  |  Home Garage - Sunnyvale, CA                |   |
|  |  Parked since: 8:42 PM                      |   |
|  |  [Navigate to vehicle]                      |   |
|  +--------------------------------------------+   |
|                                                    |
|  CONTROLS                                          |
|  +--------+  +--------+  +--------+               |
|  | Lights |  | Horn   |  | Frunk  |               |
|  +--------+  +--------+  +--------+               |
|  +--------+  +--------+  +--------+               |
|  | Windows|  | Mirror |  | Dashcam|               |
|  +--------+  +--------+  +--------+               |
|                                                    |
|  H2 FUEL CELL (if equipped)                        |
|  +--------------------------------------------+   |
|  |  H2 level: 78%  |||||||||||||||----         |   |
|  |  Range boost: +340 km                       |   |
|  |  Nearest H2 station: 4.2 km                |   |
|  +--------------------------------------------+   |
+--------------------------------------------------+
```

### Urban Drone Control

```
+--------------------------------------------------+
|  < Back      Urban Drone "Sky Runner"    [share]  |
+--------------------------------------------------+
|                                                    |
|         +------------------------------+          |
|         |                              |          |
|         |     [TOP-DOWN DRONE VIEW]    |          |
|         |                              |          |
|         |   R1: OK   R2: OK           |          |
|         |   R3: OK   R4: OK           |          |
|         |   R5: OK   R6: OK   Status: |          |
|         |   R7: OK   R8: OK   READY   |          |
|         |                              |          |
|         +------------------------------+          |
|                                                    |
|  FLIGHT STATUS                                     |
|  +--------------------------------------------+   |
|  |  Mode: PARKED (grounded)                    |   |
|  |  Pre-flight check: PASSED                   |   |
|  |  Airspace: CLEAR (FAA approved corridor)    |   |
|  |  Weather: VFR conditions, wind 8 kt         |   |
|  +--------------------------------------------+   |
|                                                    |
|  +------+ +------+ +------+ +------+              |
|  |SUMMON| |PRE-  | |CABIN | | LOCK |              |
|  |      | |FLIGHT| |TEMP  | |      |              |
|  +------+ +------+ +------+ +------+              |
|                                                    |
|  BATTERY & SOLAR                                   |
|  +--------------------------------------------+   |
|  |  Battery: 82%  ||||||||||||||||||----       |   |
|  |  Range: 380 km                              |   |
|  |  Solar in-flight: +5.1 kW                   |   |
|  |  Est. solar boost: +45 km                   |   |
|  +--------------------------------------------+   |
|                                                    |
|  ROTOR STATUS                                      |
|  +--------------------------------------------+   |
|  |  R1: 48C OK  R2: 47C OK  R3: 49C OK        |   |
|  |  R4: 48C OK  R5: 47C OK  R6: 48C OK        |   |
|  |  R7: 49C OK  R8: 48C OK                     |   |
|  |  Tilt angle: 0 deg (vertical ready)          |   |
|  |  Vibration: nominal                          |   |
|  +--------------------------------------------+   |
|                                                    |
|  SAFETY SYSTEMS                                    |
|  +--------------------------------------------+   |
|  |  BPS (parachute): ARMED                     |   |
|  |  LiDAR: 8/8 online                          |   |
|  |  Cameras: 12/12 online                      |   |
|  |  ADS-B: broadcasting                        |   |
|  |  Satellite link: connected                   |   |
|  +--------------------------------------------+   |
|                                                    |
|  AUTONOMY                                          |
|  +--------------------------------------------+   |
|  |  Level 4 autonomous: ENABLED                |   |
|  |  Pilot override: available                  |   |
|  |  Geofence: active (SFO urban corridor)      |   |
|  +--------------------------------------------+   |
+--------------------------------------------------+
```

### Space Shuttle Control

```
+--------------------------------------------------+
|  < Back      Space Shuttle "Apex"        [share]  |
+--------------------------------------------------+
|                                                    |
|  MISSION STATUS                                    |
|  +--------------------------------------------+   |
|  |  Vehicle state: GROUND OPS                  |   |
|  |  Next window: Apr 28, 10:00 UTC             |   |
|  |  Mission type: Suborbital tourism           |   |
|  |  Passengers: 0/3 booked                     |   |
|  +--------------------------------------------+   |
|                                                    |
|  PRE-FLIGHT CHECKLIST                              |
|  +--------------------------------------------+   |
|  |  [x] Propellant loaded (H2: 100%, N2O: 95%)|   |
|  |  [x] Solar concentrator: deployed/tested    |   |
|  |  [x] Life support: O2 full, CO2 scrub OK    |   |
|  |  [x] TPS tiles: inspected, no damage        |   |
|  |  [x] RCS thrusters: 16/16 test-fired        |   |
|  |  [ ] Weather clearance: pending              |   |
|  |  [ ] FAA AST launch approval: pending        |   |
|  |  [ ] Passenger medical clearance: pending    |   |
|  +--------------------------------------------+   |
|                                                    |
|  PROPULSION                                        |
|  +--------------------------------------------+   |
|  |  Hybrid rocket: STANDBY                     |   |
|  |  Solar-thermal: STOWED                      |   |
|  |  Thrust available: 145 kN                   |   |
|  |  Propellant mass: 1,850 kg                  |   |
|  |  Delta-V budget: 1,200 m/s                  |   |
|  +--------------------------------------------+   |
|                                                    |
|  LIFE SUPPORT                                      |
|  +--------------------------------------------+   |
|  |  Cabin pressure: 101.3 kPa (sea level)      |   |
|  |  O2: 21%          CO2: 0.04%                |   |
|  |  Temp: 22 C       Humidity: 45%             |   |
|  |  Radiation dose: 0.0 mSv (ground)           |   |
|  +--------------------------------------------+   |
|                                                    |
|  THERMAL PROTECTION                                |
|  +--------------------------------------------+   |
|  |  TPS status: ALL GREEN                      |   |
|  |  Nose: 25 C    Leading edge: 25 C           |   |
|  |  Belly: 25 C   Windward: 25 C               |   |
|  |  (During re-entry: monitored up to 1600 C)  |   |
|  +--------------------------------------------+   |
+--------------------------------------------------+
```

### Combo Unit Control

```
+--------------------------------------------------+
|  < Back      Combo Unit "Phoenix"        [share]  |
+--------------------------------------------------+
|                                                    |
|  CURRENT MODE              +------------------+   |
|                             | [DRONE] | SPACE  |   |
|                             +------------------+   |
|                                                    |
|  DRONE MODE PANEL (active)                         |
|  +--------------------------------------------+   |
|  |  Rotors: 8/8 deployed                       |   |
|  |  Tilt: 0 deg (VTOL ready)                   |   |
|  |  Battery: 72%   H2: 85%                     |   |
|  |  Solar (atm): +4.8 kW                       |   |
|  |  Range: 280 km (drone) + 95 km (rocket)     |   |
|  +--------------------------------------------+   |
|                                                    |
|  MODE TRANSITION                                   |
|  +--------------------------------------------+   |
|  |  [DRONE] ----> [TRANSITION] ----> [SPACE]   |   |
|  |    0-500m       500m-30km        30km-100km |   |
|  |                                              |   |
|  |  Transition checklist:                       |   |
|  |  [x] Altitude > 500m                         |   |
|  |  [x] Airspace clear above                    |   |
|  |  [ ] Rocket ignition armed                   |   |
|  |  [ ] Rotor retraction ready                  |   |
|  |  [ ] Cabin pressurized                       |   |
|  |  [ ] TPS heating activated                   |   |
|  +--------------------------------------------+   |
|                                                    |
|  DUAL POWER STATUS                                 |
|  +--------------------------------------------+   |
|  |  ELECTRIC          H2 FUEL CELL             |   |
|  |  150 kWh           50 kW PEM                |   |
|  |  72% ||||||||--    85% ||||||||||--          |   |
|  |  Drone mode        Transition boost          |   |
|  |                                              |   |
|  |  ROCKET             SOLAR-THERMAL            |   |
|  |  200 kN hybrid      25 kN sustained          |   |
|  |  Prop: 95%          Concentrator: stowed     |   |
|  |  Boost phase        Space cruise             |   |
|  +--------------------------------------------+   |
+--------------------------------------------------+
```

---

## Fly Tab — Flight Planning

```
+--------------------------------------------------+
|            PLAN YOUR FLIGHT                        |
+--------------------------------------------------+
|                                                    |
|  FROM: [Current location - Sunnyvale, CA]         |
|  TO:   [Search destination...]                     |
|                                                    |
|  VEHICLE: [Urban Drone v] [Eco Car] [Combo]        |
|                                                    |
|  +--------------------------------------------+   |
|  |                                              |   |
|  |          [======= MAP =======]               |   |
|  |                                              |   |
|  |    * Sunnyvale                               |   |
|  |     \                                        |   |
|  |      \--- Flight corridor (FAA approved)     |   |
|  |           \                                  |   |
|  |            * San Francisco                   |   |
|  |                                              |   |
|  |  Vertiports along route:                     |   |
|  |  [*] SFO Hub  [*] Palo Alto  [*] Downtown   |   |
|  +--------------------------------------------+   |
|                                                    |
|  ROUTE DETAILS                                     |
|  +--------------------------------------------+   |
|  |  Distance: 52 km                            |   |
|  |  Flight time: 14 min                        |   |
|  |  Altitude: 300m (urban corridor)             |   |
|  |  Weather: Clear, wind 6 kt                  |   |
|  |  Airspace: Class G (approved)               |   |
|  |  Energy cost: 18 kWh (15% battery)          |   |
|  |  Solar recovery: +1.2 kWh in-flight         |   |
|  +--------------------------------------------+   |
|                                                    |
|  +--------------------------------------------+   |
|  |                                              |   |
|  |         [  REQUEST FLIGHT  ]                 |   |
|  |                                              |   |
|  |  Est. cost: $45 (subscription) / $89 (ride)  |   |
|  +--------------------------------------------+   |
|                                                    |
|  SPACE FLIGHT (Combo/Shuttle only)                 |
|  +--------------------------------------------+   |
|  |  [  BOOK SUBORBITAL EXPERIENCE  ]            |   |
|  |  Next window: Apr 28, 10:00 UTC             |   |
|  |  Duration: 90 min total, 5 min microgravity  |   |
|  |  Max altitude: 110 km                        |   |
|  |  Seats available: 3/3                        |   |
|  +--------------------------------------------+   |
+--------------------------------------------------+
```

## Energy Tab — Unified Power Dashboard

```
+--------------------------------------------------+
|                ENERGY HUB                          |
+--------------------------------------------------+
|                                                    |
|  FLEET ENERGY STATUS                               |
|  +--------------------------------------------+   |
|  |                                              |   |
|  |  Eco Car "Sol"        Drone "Sky Runner"     |   |
|  |  Batt: 94% |||||||||| Batt: 82% ||||||||--  |   |
|  |  H2:   78% ||||||||-- Solar: +5.1 kW        |   |
|  |  Solar: +0.8 kW      Range: 380 km          |   |
|  |  Range: 614 km                               |   |
|  +--------------------------------------------+   |
|                                                    |
|  TODAY'S SOLAR HARVEST                             |
|  +--------------------------------------------+   |
|  |  Total: 18.4 kWh                            |   |
|  |  +------+                                   |   |
|  |  |      |     +---+                          |   |
|  |  |      |     |   |                          |   |
|  |  |  Car |     |Dro|                          |   |
|  |  | 4.2  |     |14.|                          |   |
|  |  | kWh  |     |2kW|                          |   |
|  |  +------+     +---+                          |   |
|  |  6am  9am  12pm  3pm  6pm                    |   |
|  +--------------------------------------------+   |
|                                                    |
|  V2G EARNINGS                                      |
|  +--------------------------------------------+   |
|  |  This month: $42.30                         |   |
|  |  This year:  $380.50                        |   |
|  |  Grid sell rate: $0.18/kWh (peak)           |   |
|  |  Next sell window: 4-7 PM (peak demand)     |   |
|  |  [Enable V2G selling]  [Set reserve: 50%]   |   |
|  +--------------------------------------------+   |
|                                                    |
|  CHARGING SCHEDULE                                 |
|  +--------------------------------------------+   |
|  |  Eco Car: Charge to 90% by 7:00 AM          |   |
|  |           Use off-peak rate ($0.08/kWh)      |   |
|  |  Drone:   Fast-charge at vertiport           |   |
|  |           400V DC, 20 min to 80%             |   |
|  +--------------------------------------------+   |
|                                                    |
|  H2 NETWORK                                       |
|  +--------------------------------------------+   |
|  |  Home electrolyzer: producing 0.3 kg/hr     |   |
|  |  H2 stored: 2.1 kg (Eco Car tank)           |   |
|  |  Nearest H2 station: Shell H2 - 4.2 km      |   |
|  |  [Map all H2 stations]                       |   |
|  +--------------------------------------------+   |
+--------------------------------------------------+
```

---

## Summon Feature (All Vehicles)

Like Tesla Summon, but for drones too:

| Vehicle | Summon Behavior |
|---------|----------------|
| **Eco Car** | Drives itself out of garage/parking to your GPS pin (ground summon) |
| **Urban Drone** | Flies from vertiport to nearest landing pad near your location |
| **Combo Unit** | Ground taxi or short flight to your location |
| **Space Shuttle** | N/A (spaceport ops only) |

```
SUMMON FLOW

  [User taps SUMMON button]
        |
        v
  [Confirm pickup location on map]
        |
        v
  [Vehicle runs pre-flight/drive check]
        |
        +-- Car: checks path, obstacles, distance
        +-- Drone: checks airspace, weather, battery, landing zone
        |
        v
  [Live tracking on map]
  [ETA countdown]
  [Camera feed (if available)]
        |
        v
  [Vehicle arrives]
  [Haptic + notification: "Your ride is here"]
```

## OTA Software Updates

```
+--------------------------------------------------+
|  SOFTWARE UPDATE                                   |
+--------------------------------------------------+
|                                                    |
|  Version 2.4.1 available                           |
|                                                    |
|  WHAT'S NEW:                                       |
|  - Improved solar MPPT efficiency (+3%)            |
|  - New autopilot neural net (v7.2)                 |
|  - H2 fuel cell cold-start optimization            |
|  - Bug fix: V2G metering accuracy                  |
|  - Drone: reduced hover noise (-2 dB)              |
|                                                    |
|  Applies to: All vehicles                           |
|  Size: 1.2 GB                                      |
|  Install time: ~25 min (vehicle parked)             |
|                                                    |
|  [Install Now]  [Schedule for Tonight]              |
|                                                    |
+--------------------------------------------------+
```

## Tech Stack

| Layer | Technology |
|-------|-----------|
| **Framework** | React Native 0.73+ (iOS + Android) |
| **Vehicle comms** | BLE 5.3 (proximity) + 5G-NR (remote) + Satellite (space) |
| **Real-time telemetry** | MQTT over TLS (vehicle → cloud → app) |
| **Maps** | Mapbox GL (ground) + custom airspace overlay (FAA corridors) |
| **Flight planning** | Custom route engine with airspace/weather integration |
| **Authentication** | Biometric + hardware key (vehicle pairing) |
| **Streaming** | WebRTC (live camera feeds from vehicle) |
| **State** | Redux Toolkit + WebSocket real-time |
| **Backend** | EoS cloud (Kubernetes) + edge compute on vehicle |
| **AI** | On-device TFLite (summon path planning, parking) |

## Security

| Feature | Implementation |
|---------|---------------|
| **Vehicle pairing** | BLE bonding + RSA-2048 key exchange |
| **Remote commands** | End-to-end encrypted (AES-256-GCM) |
| **Authentication** | Biometric (FaceID/fingerprint) + PIN + hardware token |
| **Geofencing** | Stolen vehicle lockout if outside owner-defined zone |
| **Anti-relay** | UWB ranging prevents relay attacks (like Tesla fix) |
| **Flight authorization** | Multi-factor: app + voice + biometric for flight commands |
| **Kill switch** | Emergency remote disable (cloud-authenticated) |
