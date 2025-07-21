from components.map import Map
from database.car_repo import CarRepo
from components.shape import ShapeSpecification
from components.car import Car

class Driving():
    def __init__(self, screen, pygame):
        self.screen = screen
        self.pygame = pygame
        self.shape_specs = ShapeSpecification()
        self.map = Map(screen, pygame, self.shape_specs)
        self.car_repo = CarRepo()
        car_specs = self.car_repo.get_specs()
        self.car = Car(screen, pygame, car_specs)