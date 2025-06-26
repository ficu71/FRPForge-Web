class WebUSBHandler:
    def get_devices(self):
        """Symulacja detekcji urządzeń WebUSB."""
        return [
            {"id": "device1", "vendor": "Samsung", "model": "Galaxy A50"},
            {"id": "device2", "vendor": "Xiaomi", "model": "Redmi Note 9"},
            {"id": "device3", "vendor": "Huawei", "model": "P30"},
            {"id": "device4", "vendor": "Oppo", "model": "Reno 6"}
        ]
