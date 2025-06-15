<p align="center">
  <img src="https://raw.githubusercontent.com/ficu71/FRPForge-Web/main/docs/banner.png" alt="FRPForge Web" width="600"/>
</p>

# FRPForge Web

## 🇵🇱 Wersja Polska

**FRPForge Web** to edukacyjne narzędzie do demonstracji omijania blokady FRP (Factory Reset Protection) na urządzeniach z Androidem – za pomocą przeglądarki z obsługą WebUSB.  
🔐 **Wyłącznie do celów edukacyjnych** — kompatybilność z Android 12–15 oraz wsparcie dla producentów: Samsung, Xiaomi, Huawei, Oppo.

### 🔍 Czym jest FRP?

Factory Reset Protection (FRP) to zabezpieczenie wprowadzone przez Google od Androida 5.1, które chroni telefon po przywróceniu ustawień fabrycznych.  
FRPForge Web pokazuje, jak działają techniki bypassu – legalnie, do nauki, bez ryzyka.

### ⚙️ Funkcje

- ✅ Edukacyjny symulator FRP  
- 🌐 Interfejs WebUSB + wykresy w Chart.js  
- 🔧 Backend Python Flask z ADB, Fastboot, TWRP  
- 📡 Logi w czasie rzeczywistym przez WebSocket  
- 🧪 Tryb demo (bez podłączonego urządzenia)  
- 🔁 Konfigurowalne kroki przez `config.json`

### 📦 Wymagania

- Python 3.8+  
- Node.js (frontend)  
- ADB i Fastboot zainstalowane w systemie  
- Chrome z włączoną flagą WebUSB (`chrome://flags/#enable-webusb`)

### 🧪 Jak uruchomić

**Backend:**

```
cd backend
python -m venv venv
source venv/bin/activate  # lub venv\Scripts\activate na Windows
pip install -r requirements.txt
python app.py
```

**Frontend:**

```
cd frontend
npx http-server -p 8080
# Otwórz http://localhost:8080 w Chrome
```

### 🛠 Tryb Demo

Kliknij „Tryb Demo” w interfejsie i zobacz symulację bypassu dla wybranego producenta – bez fizycznego telefonu.

### ⚠️ Ostrzeżenie Prawne

> **Ten projekt służy wyłącznie do celów edukacyjnych i testowych.**  
> Nie używaj go na urządzeniach, które nie należą do Ciebie.  
> Omijanie FRP na cudzych urządzeniach jest nielegalne.

### 👤 Autor

**FICU71**  
[https://github.com/ficu71](https://github.com/ficu71)

---

## 🇬🇧 English Version

**FRPForge Web** is an educational tool for demonstrating Android Factory Reset Protection (FRP) bypass through a browser-based WebUSB interface.  
🔐 **For educational use only** — supports Android 12–15 and major vendors: Samsung, Xiaomi, Huawei, Oppo.

### 🔍 What is FRP?

Factory Reset Protection (FRP) is a Google security feature introduced in Android 5.1 to block unauthorized access after a factory reset.  
FRPForge Web safely simulates bypass methods — for learning, testing, and legal use.

### ⚙️ Features

- ✅ Educational FRP bypass simulator  
- 🌐 Browser interface with WebUSB + Chart.js  
- 🔧 Python Flask backend with ADB, Fastboot, TWRP support  
- 📡 Real-time logs via WebSocket  
- 🧪 Demo mode (no physical device needed)  
- 🔁 Easily extendable via `config.json`

### 📦 Requirements

- Python 3.8+  
- Node.js (for frontend hosting)  
- ADB and Fastboot installed  
- Google Chrome with WebUSB enabled (`chrome://flags/#enable-webusb`)

### 🧪 How to Run

**Backend:**

```
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
```

**Frontend:**

```
cd frontend
npx http-server -p 8080
# then open http://localhost:8080 in Chrome
```

### 🛠 Demo Mode

Use “Demo Mode” to simulate a bypass without a phone. Choose a vendor and see the steps displayed in real-time.

### ⚠️ Legal Notice

> **This tool is for educational and testing purposes only.**  
> Do not use it on devices you do not own.  
> FRP bypass on stolen/unauthorized devices is illegal.

### 👤 Author

**FICU71**  
[https://github.com/ficu71](https://github.com/ficu71)

---

<p align="center">
  🔓 Open-source • MIT License • Wiedza to potęga / Knowledge is Power
</p>
