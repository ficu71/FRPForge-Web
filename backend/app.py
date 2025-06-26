from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO
from vendors.loader import VendorLoader
from utils.twrp import TWRP
from utils.webusb import WebUSBHandler
import logging

app = Flask(__name__)
CORS(app)  # Włączenie CORS dla frontendu
socketio = SocketIO(app)  # WebSocket dla logów w czasie rzeczywistym

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Inicjalizacja WebUSB i ładowanie vendorów
webusb = WebUSBHandler()
vendor_loader = VendorLoader.load_vendors()

@socketio.on('connect')
def handle_connect():
    socketio.emit('log', {'message': 'Połączono z WebSocket'})

def emit_log(message):
    socketio.emit('log', {'message': message})

@app.route('/api/devices', methods=['GET'])
def list_devices():
    """Lista podłączonych urządzeń przez WebUSB (symulacja w trybie demo)."""
    try:
        devices = webusb.get_devices()
        emit_log(f"Wykryto urządzeń: {len(devices)}")
        return jsonify({"status": "success", "devices": devices})
    except Exception as e:
        logger.error(f"Błąd podczas listy urządzeń: {str(e)}")
        emit_log(f"Błąd podczas listy urządzeń: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/bypass/<vendor>', methods=['POST'])
def bypass_frp(vendor):
    """Wykonanie bypassu FRP dla wybranego vendora."""
    data = request.json
    device_id = data.get('device_id')
    
    try:
        if vendor.lower() not in vendor_loader:
            emit_log(f"Nieobsługiwany vendor: {vendor}")
            return jsonify({"status": "error", "message": "Nieobsługiwany vendor"}), 400
        
        bypass = VendorLoader.create_bypass(vendor.lower(), device_id, vendor_loader[vendor.lower()])
        result = bypass.execute()
        emit_log(f"Bypass wykonany dla {vendor}: {len(result)} kroków")
        return jsonify({"status": "success", "result": result})
    except Exception as e:
        logger.error(f"Błąd podczas bypassu: {str(e)}")
        emit_log(f"Błąd podczas bypassu: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/demo/<vendor>', methods=['GET'])
def demo_bypass(vendor):
    """Symulacja bypassu w trybie demo."""
    try:
        if vendor.lower() not in vendor_loader:
            emit_log(f"Nieobsługiwany vendor w trybie demo: {vendor}")
            return jsonify({"status": "error", "message": "Nieobsługiwany vendor"}), 400
        bypass = VendorLoader.create_bypass(vendor.lower(), None, vendor_loader[vendor.lower()])
        result = bypass.demo_steps()
        emit_log(f"Tryb demo wykonany dla {vendor}")
        return jsonify({"status": "success", "steps": result})
    except Exception as e:
        logger.error(f"Błąd w trybie demo: {str(e)}")
        emit_log(f"Błąd w trybie demo: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/flash_twrp', methods=['POST'])
def flash_twrp():
    """Flashowanie TWRP na urządzeniu."""
    data = request.json
    device_id = data.get('device_id')
    twrp_image_path = data.get('twrp_image_path')
    
    try:
        twrp = TWRP(device_id)
        result = twrp.flash_recovery(twrp_image_path)
        emit_log(f"TWRP zaflashowane: {result}")
        return jsonify({"status": "success", "output": result})
    except Exception as e:
        logger.error(f"Błąd podczas flashowania TWRP: {str(e)}")
        emit_log(f"Błąd podczas flashowania TWRP: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/accessibility/<vendor>', methods=['POST'])
def accessibility_exploit(vendor):
    """Wykonanie exploita Accessibility dla ominięcia kreatora."""
    try:
        adb = ADB(request.json.get('device_id'))
        result = adb.run("am start -n com.android.settings/.accessibility.AccessibilitySettings")
        emit_log(f"Exploit Accessibility wykonany: {result}")
        return jsonify({"status": "success", "output": result})
    except Exception as e:
        emit_log(f"Błąd w exploicie Accessibility: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
