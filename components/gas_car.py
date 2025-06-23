from components.car import Car
from components.gas_tank import GasTank
    
class GasCar(Car):
    def __init__(self, make, model, year, capacity = 15, gallons_used_per_mile = 0.05):
        super().__init__(make, model, year)
        self.gas_tank = GasTank(capacity, gallons_used_per_mile)
    
    def travel_distance(self, direction, miles):
        if direction == "forward":
            self.drive_forward(miles)
            self.gas_tank.travel_distance(miles)
            self.miles_drove += miles
    
    def fill_gas(self, gallons):
        self.gas_tank.capacity = min(self.gas_tank.capacity_left + gallons, self.gas_tank.capacity)
        self.gas_tank.percentage = (self.gas_tank.capacity_left/self.gas_tank.capacity) * 100