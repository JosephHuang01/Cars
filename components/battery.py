class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        #print("This car has a " + str(self.battery_size) + "-kWh battery.")
        return self.battery_size
    
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        return range
    
    def travel_distance(self, miles, kwh_used_per_mile = 0.2, capacity_max = 50):
        self.miles = miles
        self.kwh_used_per_mile = kwh_used_per_mile
        self.capacity_used = miles * kwh_used_per_mile
        self.capacity = capacity_max - self.capacity_used
        self.capacity_max = capacity_max
        if self.capacity >= 50:
            self.capacity = capacity_max
        if self.capacity == capacity_max:
            self.life = 100
        self.life = (self.capacity/capacity_max) * 100
        return self.life