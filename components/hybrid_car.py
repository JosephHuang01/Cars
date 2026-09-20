from components.car import Car
from components.battery import Battery
from components.gas_tank import GasTank

class HybridCar(Car):
    def __init__(self, make, model, year, battery_size, capacity = 15, gallons_used_per_mile = 0.05):
        super().__init__(make, model, year)
        self.battery = Battery(battery_size)
        self.gas_tank = GasTank(capacity, gallons_used_per_mile)
        self.capacity = capacity
        self.capacity_left = capacity
        self.kwh_used_per_mile = 0.2
    
    def travel_distance(self, direction, miles):
        if direction == "forward":
            self.drive_forward(miles)
            self.gas_tank.travel_distance(miles)
            self.miles_drove += miles
    
    def fill_gas(self, gallons):
        self.gas_tank.capacity = min(self.gas_tank.capacity_left + gallons, self.gas_tank.capacity)
        self.gas_tank.percentage = (self.gas_tank.capacity_left/self.gas_tank.capacity) * 100
    
    def charge(self):
        self.capacity_left = self.capacity
        self.life = 100
    
    def recharge_battery(self, kwh_charge):
        self.capacity = min(self.capacity + kwh_charge, self.capacity)
        self.life = (self.capacity/self.capacity) * 100