

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
