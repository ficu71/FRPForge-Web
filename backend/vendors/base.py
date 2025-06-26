class BaseBypass:
    def __init__(self, device_id):
        self.device_id = device_id

    def execute(self):
        raise NotImplementedError("Metoda execute musi być zaimplementowana przez podklasę")

    @staticmethod
    def demo_steps():
        raise NotImplementedError("Metoda demo_steps musi być zaimplementowana przez podklasę")
