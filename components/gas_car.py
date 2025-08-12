from components.car import Car
from components.gas_tank import GasTank
from components.person import Driver, Passenger
    
class GasCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.gas_tank = GasTank(0, 0)
    
    def drive(self, direction, distance):
        super().drive(direction, distance)
        self.miles_drove += distance
        self.gas_tank.travel_distance(distance)
        
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