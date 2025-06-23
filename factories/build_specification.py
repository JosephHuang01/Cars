from components.car import CarColor

class BuildSpecification():
    def __init__(self):
        self.make = ''
        self.model = ''
        self.year = 0
        self.gas_tank_capacity = 0
        self.battery_capacity = 0
        self.color_list = [(0, 0, 0), (179, 0, 0), (173, 216, 230)]
        self.car_color = CarColor.RED