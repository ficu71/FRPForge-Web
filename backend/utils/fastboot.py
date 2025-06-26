import subprocess

class Fastboot:
    def __init__(self, device_id=None):
        self.device_id = device_id

    def run(self, command):
        """Uruchom komendę Fastboot."""
        cmd = ["fastboot"]
        if self.device_id:
            cmd.extend(["-s", self.device_id])
        cmd.extend(command.split())
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise Exception(f"Komenda Fastboot nie powiodła się: {e.stderr}")
