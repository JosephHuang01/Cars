from components.car import Car
from components.battery import Battery

class ElectricCar(Car):
    def __init__(self, make, model, year, capacity):
        super().__init__(make, model, year)
        self.capacity = Battery(capacity)
        self.kwh_used_per_mile = 0.2
        self.capacity = capacity
        self.capacity_left = capacity
        self.life = 100
    
    def travel_distance(self, miles):
        capacity_used = miles * self.kwh_used_per_mile
        self.capacity_left = self.capacity_left - capacity_used
        self.life = (self.capacity_left/self.capacity) * 100
        return self.life
    
    def charge(self):
        self.capacity_left = self.capacity
        self.life = 100
    
    def recharge_battery(self, kwh_charge):
        self.capacity = min(self.capacity + kwh_charge, self.capacity)
        self.life = (self.capacity/self.capacity) * 100