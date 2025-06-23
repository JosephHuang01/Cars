from components.car import Car, Seat
from components.battery import Battery
from components.person import Driver, Passenger

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.kwh_used_per_mile = 0.2
        self.life = 100
        self.battery = Battery(0, 0)

    def drive(self, direction, distance):
        super().drive(direction, distance)
        #self.battery.travel_distance(miles_drove)
        self.miles_drove += distance
        self.battery.travel_distance(distance)
    
    def charge(self):
        #self.capacity_left = self.capacity
        #self.life = 100
        Battery.charge()
    
    def replace_battery(self, battery):
        # if capacity == 0:
        #     capacity = self.battery.capacity
        # self.capacity = capacity
        # self.capacity = Battery(capacity)
        # self.capacity_left = capacity
        # self.life = 100
        # self.battery = Battery(capacity, kwh_used_per_mile)
        self.battery = battery
    
    def assigned_driver(self, name):
        self.driver = Driver(name)
        return self.driver
    
    def add_passenger(self, name):
        self.passenger = Passenger(name)
        return self.passenger
    
    def seat_number(self, number):
        self.seat = Seat(number)
        return self.seat