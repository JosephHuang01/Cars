from components.car import Car, Position
from components.gas_tank import GasTank
    
class GasCar(Car):
    def __init__(self, make, model, year, gas_tank_supply = 15):
        super().__init__(make, model, year)
        self.gas_tank = GasTank(gas_tank_supply)
        self.gallons_used_per_mile = 0.05
        miles = 1/self.gallons_used_per_mile
    
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
        if GasCar(Car).read_odometer == 20:
            GasCar(Car).gas_tank_supply -= 1