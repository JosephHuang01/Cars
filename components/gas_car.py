from components.car import Car, Seat, Tire
from components.gas_tank import GasTank
from components.person import Driver, Passenger
    
class GasCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.gas_tank = GasTank(0, 0)
    
    def drive(self, direction, distance):
        super().drive(direction, distance)
        #GasTank.travel_distance(distance)
        self.miles_drove += distance
        #self.gas_tank.capacity_left -= (self.miles_drove * self.gas_tank.gallons_used_per_mile)
        self.gas_tank.travel_distance(distance)
            
    # def travel_distance(self, direction, miles):
    #     if direction == "forward":
    #         self.drive_forward(miles)            
    #     elif direction == "backward":
    #         self.drive_backward(miles)
    #     elif direction == "left":
    #         self.turn_left(miles)
    #     elif direction == "right":
    #         self.turn_right(miles)
    
    #     self.gas_tank.travel_distance(miles)
    #     self.miles_drove += miles
        
    def fill_gas(self):
        GasTank.fill_gas()
    
    def add_gas_tank(self, gas_tank):        
        self.gas_tank = gas_tank
    
    def assigned_driver(self, name):
        self.driver = Driver(name)
        return self.driver
    
    def add_passenger(self, name):
        self.passenger = Passenger(name)
        return self.passenger
    
    def seat_number(self, number):
        self.seat = Seat(number)
        return self.seat
    
    def inflation(self, pressure, tire_inflation):
        self.inflation = Tire(pressure)
        # if pressure < 20 and tire_inflation == "yes":
        #     pressure == 35
        return self.inflation