from components.car import Car
from components.gas_tank import GasTank
    
class GasCar(Car):
    def __init__(self, make, model, year, gas_tank_supply):
        super().__init__(make, model, year)
        self.gas_tank = GasTank(gas_tank_supply)