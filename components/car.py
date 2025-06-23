from components.coordinate_direction import CoordinateDirection
from components.driving_direction import DrivingDirection
from components.city_map import CityMap

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        #self.gas_tank_supply = 15
        self.position = Position(0,0)
        self.miles_drove = 0
        self.direction = DrivingDirection.FORWARD
        self.set_present_coordinate_direction = CoordinateDirection()
        self.max_speed = 100
        

    # todo: change to y plus and add more constants to coordincation class
    # todo: Add x and y calcuation to drive method below and unit tests 

    def drive(self, direction, distance):
        self.direction = direction        
        self.__increment_odometer(distance)
        self.set_present_coordinate_direction.set_present_coordinate_direction(direction)

        if direction == DrivingDirection.FORWARD:
            self.position.y += distance
        elif direction == DrivingDirection.LEFT:
            self.position.x -= distance
        elif direction == DrivingDirection.BACKWARD:
            self.position.y -= distance
        elif direction == DrivingDirection.RIGHT:
            self.position.x += distance

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        return self.odometer_reading
    
    def __increment_odometer(self, miles):
        self.odometer_reading += miles
    
    def passengers_count(self, passengers):
        if 0 < total_population < 5:
            total_population = passengers + 1
            return total_population
    
    def acceleration(self, speed, acceleration_rate):
        speed += (acceleration_rate * 10)
        if speed == self.max_speed:
            speed

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Seat:
    def __init__(self, number):
        self.number = number

class Tire:
    def __init__(self, pressure):
        self.pressure = pressure

class CarColor:
    RED = [255, 0 ,0]
    BLACK = [0, 0, 0]
    GRAY = [128, 128, 128]
    BLUE = [0, 0, 255]
    WHITE = [255, 255, 255]