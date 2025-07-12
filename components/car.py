# from components.coordinate_direction import CoordinateDirection
# from components.driving_direction import DrivingDirection
# from components.city_map import CityMap
# from components.position import Position
# import random
from components.shape import Shape

class Car(Shape):
    def __init__(self, screen, pygame, name, type, position, width, length):
        super().__init__(screen, pygame, name, type, position, width, length)

        # self.car_id = 0
        # self.make = make
        # self.model = model
        # self.year = year
        # self.odometer_reading = 0
        #self.gas_tank_supply = 15
        # self.position = Position(0,0)
        # self.miles_drove = 0
        # self.direction = DrivingDirection.FORWARD
        # self.set_present_coordinate_direction = CoordinateDirection()
        # self.max_speed = 100
        

    # todo: change to y plus and add more constants to coordincation class
    # todo: Add x and y calcuation to drive method below and unit tests 

#     def drive(self, direction, distance):
#         self.direction = direction        
#         self.__increment_odometer(distance)
#         self.set_present_coordinate_direction.set_present_coordinate_direction(direction)

#         if direction == DrivingDirection.FORWARD:
#             self.position.y += distance
#         elif direction == DrivingDirection.LEFT:
#             self.position.x -= distance
#         elif direction == DrivingDirection.BACKWARD:
#             self.position.y -= distance
#         elif direction == DrivingDirection.RIGHT:
#             self.position.x += distance

#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
    
#     def read_odometer(self):
#         return self.odometer_reading
    
#     def __increment_odometer(self, miles):
#         self.odometer_reading += miles
    
#     def passengers_count(self, passengers):
#         if 0 < total_population < 5:
#             total_population = passengers + 1
#             return total_population
    
#     def acceleration(self, speed, acceleration_rate):
#         speed += (acceleration_rate * 10)
#         if speed == self.max_speed:
#             speed

# class Seat():
#     def __init__(self, number):
#         self.number = number

# class Tire():
#     def __init__(self, pressure):
#         self.pressure = pressure

# class CommonGameColor():
#     RED = (255, 0 ,0)
#     BLACK = (0, 0, 0)
#     GRAY = (128, 128, 128)
#     BLUE = (0, 0, 255)
#     WHITE = (255, 255, 255)
#     GREEN = (0, 255, 0)

# class RandomizeCarColor():
#     def randomize_car_color(self):
#         color_options = [CarColor.BLUE, CarColor.RED] #, CarColor.GRAY, CarColor.WHITE]
#         return random.choice(color_options)

# class CarList():
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
    
#     def randomize_model_list(self):
#         make = ['TOYOTA', 'FORD', 'HONDA']
#         model = ['COROLLA', 'MUSTANG', 'CIVIC']
#         year = [2017, 2024, 2020]
#         index = random.randint(0, len(make) -1)
#         return CarList(make[index], model[index], year[index])

# class CarModel():
#     def __init__(self, name, body_shape, wheel_size, accessories=None):
#         self.name = name
#         self.body_shape = body_shape
#         self.wheel_size = wheel_size
#         self.accessories = accessories or []
    
#     def randomize_car_model(self):
#         TOYOTA_MODEL = CarModel(
#             name='Toyota',
#             body_shape=[(0, 0), (120, 0), (120, -40), (80, -70), (40, -70), (0, -40)],
#             wheel_size=15,
#             accessories=['spoiler']
#             )

#         TESLA_MODEL = CarModel(
#             name='Tesla',
#             body_shape=[(0, 0), (140, 0), (140, -35), (100, -65), (40, -65), (0, -35)],
#             wheel_size=20,
#             accessories=['sunroof']
#             )

#         HONDA_MODEL = CarModel(
#             name='Honda',
#             body_shape=[(0, 0), (100, 0), (100, -40), (70, -60), (30, -60), (0, -40)],
#             wheel_size=18,
#             accessories=[]
#             )

#         car_models = [TOYOTA_MODEL, TESLA_MODEL, HONDA_MODEL]
#         selected_car = random.choice(car_models)
#         return selected_car