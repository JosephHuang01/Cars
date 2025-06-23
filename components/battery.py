class Battery():
    def __init__(self, capacity, kwh_used_per_mile = 0.2):
        self.capacity = capacity 
        self.kwh_used_per_mile = kwh_used_per_mile
        self.capacity_left = self.capacity
        self.life = 100
    
    def describe_battery(self):
        #print("This car has a " + str(self.battery_size) + "-kWh battery.")
        return self.capacity
    
    def get_range(self):  # miles
        if self.capacity == 70:
            range = 240 
        elif self.capacity == 85:
            range = 270
        
        return range
    
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