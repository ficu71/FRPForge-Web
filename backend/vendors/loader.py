import json
from vendors.base import BaseBypass
from utils.adb import ADB
from utils.fastboot import Fastboot
import time

class VendorLoader:
    @staticmethod
    def load_vendors(config_path="backend/vendors/config.json"):
        with open(config_path, 'r') as f:
            return json.load(f)

    @staticmethod
    def create_bypass(vendor_name, device_id, config):
        class DynamicBypass(BaseBypass):
            def __init__(self, device_id):
                super().__init__(device_id)
                self.steps = config["steps"]

            def execute(self):
                adb = ADB(self.device_id)
                fastboot = Fastboot(self.device_id)
                results = []
                for step in self.steps:
                    try:
                        if step["command"].startswith("fastboot"):
                            result = fastboot.run(step["command"].replace("fastboot ", ""))
                        elif step["command"].startswith("qfil"):
                            result = "Symulowane flashowanie QFIL"
                        else:
                            result = adb.run(step["command"])
                        results.append({"step": step["step"], "status": "success", "output": result})
                        time.sleep(2)
                    except Exception as e:
                        results.append({"step": step["step"], "status": "error", "error": str(e)})
                return results

            @staticmethod
            def demo_steps():
                return [{"step": s["step"], "status": "success", "output": f"Symulowany {s['step']}"} for s in config["steps"]]

        return DynamicBypass(device_id)
