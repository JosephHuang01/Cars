class GasTank():
    def __init__(self, gas_tank_supply = 15):
        self.gas_tank_supply = gas_tank_supply
    
    def travel_distance(self, miles, gallons_used_per_mile = 0.05, capacity_max = 15):
        self.miles = miles
        self.gallons_used_per_mile = gallons_used_per_mile
        self.capacity_max = capacity_max
        self.capacity_used = miles * gallons_used_per_mile
        self.capacity = capacity_max - self.capacity_used
        if self.capacity >= 15:
            self.capacity = capacity_max
        if self.capacity == capacity_max:
            self.life = 100
        self.life = (self.capacity/capacity_max) * 100
        return self.life