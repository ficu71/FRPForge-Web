import unittest
from vendors.loader import VendorLoader

class TestVendors(unittest.TestCase):
    def test_load_vendors(self):
        vendors = VendorLoader.load_vendors()
        self.assertIn("samsung", vendors)
        self.assertIn("xiaomi", vendors)
        self.assertIn("huawei", vendors)
        self.assertIn("oppo", vendors)

if __name__ == '__main__':
    unittest.main()
