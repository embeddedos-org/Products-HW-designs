# eRadar360 — Flutter Mobile App

> 360° driver awareness radar

## Stack
- **Flutter 3.32** (Dart 3) — iOS, Android & Web
- **Riverpod 2** — state management
- **go_router 14** — declarative navigation
- **Dio 5** — HTTP client → AmericanGroupLLC API Gateway
- **Google Fonts (Inter)** — typography
- **Material 3** — design system

## Features
- Live Radar
- Threat Map
- V2X Feed
- Alert History

## Getting Started
```bash
cd mobile
flutter pub get
flutter run
```

## Build
```bash
# Android APK
flutter build apk --release

# iOS (requires macOS + Xcode)
flutter build ios --release

# Web
flutter build web --release
```

## Architecture
```
lib/
  core/
    theme/        ← AppTheme (Material 3 + Google Fonts)
    router/       ← go_router shell with bottom nav
    services/     ← ApiService (Dio → AGL API Gateway)
    widgets/      ← Shared UI components
  features/
    home/         ← Live Radar
    search/       ← Threat Map
    profile/      ← V2X Feed
    settings/     ← App settings & preferences
test/             ← Domain unit tests
```
