from components.gas_tank import GasTank

class GasTankFactory():
    def __init__(self):
        pass

    def build_gas_tank(self, capacity):
        return GasTank(capacity)