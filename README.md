# Ble-security-auditor
Audit Bluetooth Low Energy device security from Termux (non-rooted Android)

> **Auditer la sécurité des appareils Bluetooth Low Energy depuis ton smartphone Termux**

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9+-green.svg)](https://www.python.org/)
[![Android](https://img.shields.io/badge/Android-11%2B-brightgreen.svg)](https://www.android.com/)
[![Stars](https://img.shields.io/github/stars/padreola/ble-security-auditor?style=social)](https://github.com/padreola/ble-security-auditor)

**PADRÉ OLA** | *Code Sur Android* 🎯

---

## 🎯 Qu'est-ce que c'est ?

**BLE Security Auditor Pro** est une suite complète pour :

- 🔎 **Scanner** les appareils Bluetooth Low Energy (BLE) à proximité
- 📊 **Analyser** leurs services GATT, caractéristiques et permissions
- 🚨 **Détecter** les configurations de sécurité faibles (pas d'auth, UUIDs exposés, etc.)
- 📝 **Générer** des rapports d'audit (JSON, PDF, Markdown)
- 🎨 **Visualiser** les données en temps réel via dashboard web

**Sans root, depuis Termux.**

---

## 📸 Démo

```bash
# Installation (one-liner)
curl https://install.ble-auditor.fr | bash

# Scanner
ble-auditor scan --verbose

# Analyser un appareil
ble-auditor analyze --device "EA:B0:34:AA:BB:CC" --export json

# Dashboard
ble-auditor dashboard --port 8080
```

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│                  TERMUX (Non-rooted)                 │
├─────────────────────────────────────────────────────┤
│                                                      │
│  ┌──────────────────────────────────────────────┐  │
│  │  Flask Server (Python)                       │  │
│  │  • Logging + Storage                         │  │
│  │  • Report Generation                         │  │
│  │  • WebSocket Real-time Updates               │  │
│  └──────────────────────────────────────────────┘  │
│           ↑ (HTTP/WebSocket)                        │
│           │                                         │
│  ┌────────▼──────────────────────────────────────┐  │
│  │  Native Kotlin App (BLE Scanning)            │  │
│  │  • Device enumeration                        │  │
│  │  • GATT service discovery                    │  │
│  │  • Advertisement data parsing                │  │
│  │  • Real-time packet capture                  │  │
│  └────────────────────────────────────────────────┘  │
│           │                                         │
│           ↓ (HTTP POST)                             │
│                                                      │
│  ┌──────────────────────────────────────────────┐  │
│  │  SQLite Database                             │  │
│  │  • Device profiles                           │  │
│  │  • Vulnerability signatures                  │  │
│  │  • Scan history                              │  │
│  └──────────────────────────────────────────────┘  │
│                                                      │
└─────────────────────────────────────────────────────┘
         ↓
    ┌────────────┐
    │  Dashboard │
    │  (Web UI)  │
    │  http://   │
    │  localhost │
    │  :8080     │
    └────────────┘
```

---

## ⚡ Features

### Core
- [x] BLE device scanning (non-rooted)
- [x] GATT service enumeration
- [x] Advertisement data parsing
- [x] Real-time monitoring
- [ ] Custom vulnerability signatures (v2)
- [ ] ML-based anomaly detection (v3)

### Analysis
- [x] Security scoring (1-100)
- [x] Known vulnerabilities detection
- [x] Permission analysis
- [ ] Firmware version tracking (v2)
- [ ] Device fingerprinting (v2)

### Reports
- [x] JSON export
- [x] Markdown reports
- [ ] PDF generation (v1.5)
- [ ] HTML dashboards (v1.5)
- [ ] Excel multi-scan comparison (v2)

### Dashboard
- [x] Real-time device list
- [x] Service/characteristic viewer
- [ ] Timeline analysis (v2)
- [ ] Threat heat map (v2)
- [ ] API for integrations (v2)

---

## 🚀 Démarrage rapide

### Prérequis
- Android 11+ (non-rooted)
- Termux (F-Droid)
- Python 3.9+
- Kotlin (native app)

### Installation

**1. Clone le repo**
```bash
cd ~
git clone https://github.com/padreola/ble-security-auditor.git
cd ble-security-auditor
```

**2. Install dependencies**
```bash
./scripts/install.sh
```

**3. Build Kotlin app**
```bash
cd android-app
./gradlew assembleDebug
# Output: android-app/build/outputs/apk/debug/app-debug.apk
```

**4. Install APK**
```bash
adb install android-app/build/outputs/apk/debug/app-debug.apk
# Ou transfer via USB et install manuellement
```

**5. Start Flask server**
```bash
python3 backend/app.py
# Server running at http://localhost:8080
```

**6. Open dashboard**
```bash
# Sur Termux
termux-open http://localhost:8080

# Ou via Chrome sur ton téléphone
# Navigate to 127.0.0.1:8080
```

---

## 📖 Usage Examples

### CLI Mode

**Liste tous les appareils BLE**
```bash
ble-auditor scan
```

Output:
```
╔══════════════════════════════════════════════════════════╗
║ BLE Devices Found (3)                                   ║
╠══════════════════════════════════════════════════════════╣
║ 1. Fitbit Charge 4                                      ║
║    Address: EA:B0:34:AA:BB:CC                           ║
║    RSSI: -45 dBm | Distance: ~2m                        ║
║    Security: ⚠️  Weak (score: 34/100)                   ║
╠══════════════════════════════════════════════════════════╣
║ 2. Apple AirTag                                         ║
║    Address: F2:1A:BC:DE:F0:12                           ║
║    RSSI: -67 dBm | Distance: ~10m                       ║
║    Security: ✅ Good (score: 78/100)                    ║
╠══════════════════════════════════════════════════════════╣
║ 3. Unknown Device                                       ║
║    Address: 11:22:33:44:55:66                           ║
║    RSSI: -72 dBm | Distance: ~15m                       ║
║    Security: 🚨 Critical (score: 12/100)                ║
╚══════════════════════════════════════════════════════════╝
```

**Analyser un appareil spécifique**
```bash
ble-auditor analyze --device "EA:B0:34:AA:BB:CC" --verbose
```

Output:
```
════════════════════════════════════════════════════════════
 DEVICE ANALYSIS: Fitbit Charge 4
════════════════════════════════════════════════════════════

📱 Device Info
─────────────────────────────────────────────────────────
Name: Fitbit Charge 4
Address: EA:B0:34:AA:BB:CC
TX Power: 0 dBm
Flags: [LE General Discoverable Mode, BR/EDR Not Supported]

🔐 Security Assessment
─────────────────────────────────────────────────────────
Overall Score: 34/100 ⚠️  WEAK

Issues Found:
1. ❌ No encryption on device communication
2. ❌ Unauthenticated service access
3. ⚠️  Device name exposes manufacturer (Fitbit)
4. ⚠️  TX power reveals approximate range

Recommendations:
→ Disable BLE if not actively used
→ Use strong password for app pairing
→ Check firmware updates

🛠️  Services Enumerated (4)
─────────────────────────────────────────────────────────
• Generic Access (UUID: 1800)
  └─ Device Name (characteristic)
  └─ Appearance (characteristic)

• Generic Attribute (UUID: 1801)
  └─ Service Changed (characteristic)

• Device Information (UUID: 180A)
  └─ Manufacturer Name String
  └─ Model Number String
  └─ Serial Number String

• Battery Service (UUID: 180F)
  └─ Battery Level (read, notify)

════════════════════════════════════════════════════════════
```

**Exporter un rapport**
```bash
ble-auditor audit --device "EA:B0:34:AA:BB:CC" \
  --export json \
  --output fitbit-audit-$(date +%Y%m%d).json

ble-auditor audit --device "EA:B0:34:AA:BB:CC" \
  --export pdf \
  --output fitbit-audit-$(date +%Y%m%d).pdf
```

---

## 🎓 Cas d'usage

### 🔍 **Security Researchers**
- Audit BLE devices pour vulnérabilités
- Build vulnerability database
- Publish research findings

### 📱 **IoT Device Manufacturers**
- Test BLE security avant production
- Benchmark competitors
- Compliance checking

### 🎓 **Students & Hobbyists**
- Learn BLE security concepts
- Understand GATT protocol
- Hands-on hacking practice

### 🛡️ **Penetration Testers**
- Mobile device security assessments
- BLE network reconnaissance
- Proof-of-concept exploits

---

## 🛠️ Configuration

Crée un fichier `config.yaml` :

```yaml
# BLE Auditor Configuration

scanner:
  scan_duration: 30  # seconds
  update_interval: 2  # seconds
  rssi_threshold: -100  # dBm

security:
  # Vulnerability signatures
  enable_custom_rules: true
  rules_path: ./data/rules

  # Known devices database
  known_devices_db: ./data/known_devices.json

  # Threat intelligence
  fetch_cves: true
  cve_api: "nvd.nist.gov"

reporting:
  format: json  # json, pdf, markdown
  include_raw_data: false
  anonymize_ips: true

ui:
  dashboard_port: 8080
  theme: dark
  refresh_rate: 1000  # ms

logging:
  level: INFO
  file: ./logs/auditor.log
  rotate: daily
```

---

## 📚 Documentation

- [Installation Guide](./docs/INSTALL.md)
- [Architecture Deep Dive](./docs/ARCHITECTURE.md)
- [API Reference](./docs/API.md)
- [Vulnerability Database](./docs/VULNS.md)
- [FAQ](./docs/FAQ.md)

---

## 🤝 Contributing

On accepte les contributions ! 🎉

```bash
# Fork + clone
git clone https://github.com/YOUR_USERNAME/ble-security-auditor.git

# Create branch
git checkout -b feature/cool-feature

# Commit
git commit -am "Add cool feature"

# Push
git push origin feature/cool-feature

# Open PR ✨
```

See [CONTRIBUTING.md](./CONTRIBUTING.md) for details.

---

## 📄 License

MIT License - See [LICENSE](./LICENSE) file.

---

## 🙏 Credits

Built with ❤️ by **PADRÉ OLA** (Benin)

- [Bleak](https://github.com/hbldh/bleak) - BLE library
- [Androguard](https://github.com/androguard/androguard) - Android analysis
- [Flask](https://flask.palletsprojects.com/) - Web framework

---

## 📮 Support

- 💬 **Discord**: [Join Community](https://discord.gg/padreola)
- 📧 **Email**: contact@padreola.dev
- 🐦 **Twitter**: [@PadreOlaDev](https://twitter.com/PadreOlaDev)
- 📺 **YouTube**: [PADRÉ OLA Channel](https://youtube.com/@padreola)

---

## 🗺️ Roadmap

### v1.0 (Semaine 8 - NOW)
- ✅ Core scanning
- ✅ GATT enumeration
- ✅ Basic reporting

### v1.5 (Semaine 12)
- 📅 PDF reports
- 📅 HTML dashboard
- 📅 Multi-device comparison

### v2.0 (Semaine 16)
- 🔮 Custom signatures
- 🔮 ML anomaly detection
- 🔮 Firmware tracking
- 🔮 Community database

### v3.0+ (Moyen terme)
- 🚀 Mobile app (React Native)
- 🚀 SaaS platform (B2B)
- 🚀 API for integrations
- 🚀 Threat intelligence feeds

---

**⭐ Si ça t'a plu, mets une star !**

```
Made with 🔧 in Termux, 🎓 for learning, 🛡️ for security
```
