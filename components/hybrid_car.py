from components.car import Car
from components.battery import Battery
from components.gas_tank import GasTank
from components.electric_car import ElectricCar
from components.gas_car import GasCar

class HybridCar(Car):
    def __init__(self, make, model, year, gas_tank_gallon, battery_size):
        super().__init__(make, model, year)
        self.battery = Battery(battery_size)
        self.gas_tank = GasTank(gas_tank_gallon)
        self.gallons_used_per_mile = 0.05
    
    def battery_charge(self, battery):
        if ElectricCar(Car).battery == 0:
            battery += 70
        elif ElectricCar(Car).battery > 0:
            GasCar(Car).gas_tank_supply > 0
    
    def move_with_gas(self, gallons, direction, distance):
        if gallons > 0:
            if self.gas_tank.travel_distance(distance, self.gallons_used_per_mile):
                if direction == "forward":
                    self.position.y += distance
                elif direction == "backward":
                    self.position.y -= distance
                elif direction == "left":
                    self.position.x -= distance
                elif direction == "right":
                    self.position.x += distance
        if distance >= 300:
            GasCar(Car).gas_tank_supply = 0
            if GasCar(Car).gas_tank_supply == 0:
                distance += 0
        if self.read_odometer() == 20:
            self.gas_tank.capacity -= 1