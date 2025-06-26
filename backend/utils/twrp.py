import subprocess

class TWRP:
    def __init__(self, device_id=None):
        self.device_id = device_id

    def flash_recovery(self, twrp_image_path):
        cmd = ["fastboot"]
        if self.device_id:
            cmd.extend(["-s", self.device_id])
        cmd.extend(["flash", "recovery", twrp_image_path])
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise Exception(f"Flashowanie TWRP nie powiodło się: {e.stderr}")
