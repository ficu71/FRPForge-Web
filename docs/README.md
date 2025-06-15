

# FRPForge Web

**PL 🇵🇱 – Edukacyjne narzędzie do demonstracji bypassu Factory Reset Protection (FRP)**  
**ENG 🇬🇧 – Educational tool to demonstrate Android FRP bypass**

---

## 🇵🇱 Opis projektu

**FRPForge Web** to przeglądarkowe narzędzie edukacyjne do demonstracji jak działają techniki ominięcia blokady FRP na Androidzie. Obsługuje najnowsze wersje systemu (Android 12–15) oraz wielu producentów (Samsung, Xiaomi, Huawei, Oppo).

- WebUSB + Flask backend
- Obsługa ADB, Fastboot, TWRP
- Dynamiczna konfiguracja vendorów (`config.json`)
- Tryb demonstracyjny bez fizycznego urządzenia
- Chart.js, WebSocket logi, pełne testy jednostkowe

## 🛠 Wymagania

- Python 3.8+
- Node.js (do http-server)
- Google Chrome (z WebUSB aktywne)
- ADB, Fastboot zainstalowane lokalnie

## 🔧 Uruchomienie

```bash
# Backend
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py



# FRPForge Web

**Educational tool for demonstrating Factory Reset Protection (FRP) bypass on Android devices**  
🧪 For **educational use only** — supports Android 12, 13, 14, 15 and major vendors like Samsung, Xiaomi, Huawei, Oppo.

---

## 🧠 What is FRP?

Factory Reset Protection (FRP) is a security feature on Android introduced in version 5.1 to prevent unauthorized access after a factory reset. FRPForge Web simulates and demonstrates how certain bypass methods work — legally and for learning purposes.

---

## 🚀 Features

- 🧠 Educational simulation of FRP bypass
- 🌐 Browser-based frontend (WebUSB + Chart.js)
- 🧰 Backend in Python Flask with ADB/Fastboot/TWRP support
- 📡 Real-time logs via WebSocket
- 🧪 Demo mode (no physical device required)
- 📦 Easily extendable vendor system via `config.json`

---

## 📦 Requirements

- Python 3.8+
- Node.js (for static frontend hosting)
- ADB and Fastboot installed on your system
- Google Chrome (with WebUSB enabled at `chrome://flags/#enable-webusb`)

---

## ⚙️ How to Run

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
