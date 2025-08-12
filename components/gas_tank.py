class GasTank():
    def __init__(self, capacity = 15, gallons_used_per_mile = 0.05):
        self.capacity = capacity
        self.gallons_used_per_mile = gallons_used_per_mile        
        self.capacity_left = capacity
        self.percentage = 100
    
    def travel_distance(self, miles_drove):
        self.capacity_left = self.capacity_left - (miles_drove * self.gallons_used_per_mile)
        self.percentage = (self.capacity_left/self.capacity) * 100
        return self.percentage
    
    def fill_gas(self):
        self.capacity_left = self.capacity
        self.percentage = 100