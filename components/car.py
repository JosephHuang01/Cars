class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank_supply = 15
        self.position = Position(0,0)
        self.miles_drove = 0
        self.direction = "forward"

    def drive_forward(self, distance):
        self.direction = "forward"
        self.position.y += distance
        self.__increment_odometer(distance)
    
    def drive_backward(self, distance):
        self.direction = "backward"
        self.position.y -= distance
        self.__increment_odometer(distance)
    
    def turn_left(self, distance):
        self.direction = "left"
        self.position.x -= distance
        self.__increment_odometer(distance)
    
    def turn_right(self, distance):
        self.direction = "right"
        self.position.x += distance
        self.__increment_odometer(distance)
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        return self.odometer_reading
    
    def __increment_odometer(self, miles):
        self.odometer_reading += miles


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y