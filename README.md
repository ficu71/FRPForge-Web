# FRPForge Web

FRPForge Web to edukacyjne narzędzie do demonstracji technik omijania blokady Factory Reset Protection (FRP) na urządzeniach z Androidem poprzez interfejs przeglądarkowy wykorzystujący WebUSB.

Pełna dokumentacja znajduje się w [docs/README.md](docs/README.md).

## Szybki start

1. **Backend**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate    # lub venv\Scripts\activate na Windows
   pip install -r requirements.txt
   python app.py
   ```
2. **Frontend**
   ```bash
   cd frontend
   npx http-server -p 8080
   ```
   Następnie otwórz `http://localhost:8080` w Chrome z włączoną flagą WebUSB.

## Uwaga prawna

Projekt służy wyłącznie do celów edukacyjnych. Nie używaj go na urządzeniach, których nie jesteś właścicielem.
