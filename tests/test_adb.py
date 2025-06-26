import unittest
from unittest.mock import patch
from utils.adb import ADB

class TestADB(unittest.TestCase):
    @patch('subprocess.run')
    def test_adb_run_success(self, mock_run):
        mock_run.return_value.stdout = "Success"
        adb = ADB("device1")
        result = adb.run("devices")
        self.assertEqual(result, "Success")

    @patch('subprocess.run')
    def test_adb_run_failure(self, mock_run):
        mock_run.side_effect = subprocess.CalledProcessError(1, "adb", stderr="Error")
        adb = ADB("device1")
        with self.assertRaises(Exception):
            adb.run("devices")

if __name__ == '__main__':
    unittest.main()
