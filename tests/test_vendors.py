import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))
from vendors.loader import VendorLoader

class TestVendors(unittest.TestCase):
    def test_load_vendors(self):
        vendors = VendorLoader.load_vendors()
        self.assertIn("samsung", vendors)
        self.assertIn("xiaomi", vendors)
        self.assertIn("huawei", vendors)
        self.assertIn("oppo", vendors)

    def test_dynamic_bypass_demo_steps(self):
        vendors = VendorLoader.load_vendors()
        bypass = VendorLoader.create_bypass("samsung", None, vendors["samsung"])
        steps = bypass.demo_steps()
        self.assertTrue(len(steps) > 0)
        self.assertEqual(steps[0]["status"], "success")

if __name__ == '__main__':
    unittest.main()
