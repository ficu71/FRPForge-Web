import unittest
from utils.webusb import WebUSBHandler

class TestWebUSB(unittest.TestCase):
    def test_get_devices(self):
        webusb = WebUSBHandler()
        devices = webusb.get_devices()
        self.assertGreater(len(devices), 0)
        self.assertEqual(devices[0]["vendor"], "Samsung")

if __name__ == '__main__':
    unittest.main()
