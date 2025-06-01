class Battery():
    def __init__(self, battery_size=70, kwh_used_per_mile = 0.2, capacity_max = 50):
        self.battery_size = battery_size
        self.kwh_used_per_mile = kwh_used_per_mile
        self.capacity_max = capacity_max
        self.capacity = capacity_max
    
    def describe_battery(self):
        #print("This car has a " + str(self.battery_size) + "-kWh battery.")
        return self.battery_size
    
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        return range
    
    def traveled_distance(self, miles):
        self.miles = miles
        self.life = 100
        #self.life = self.capacity/capacity_max
        #self.capacity_used = miles * kwh_used_per_mile