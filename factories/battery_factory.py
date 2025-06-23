from components.battery import Battery

class BatteryFactory():
    def __init__(self):
        pass

    def build_battery(self, capacity):
        return Battery(capacity)