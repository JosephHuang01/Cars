from database.car_repo import CarRepo
from components.car import Car
from components.driving_direction import DrivingDirection
from components.position import Position

class Driving():
    def __init__(self, screen, pygame):
        self.screen = screen
        self.pygame = pygame
        self.car_repo = CarRepo()
        car_specs = self.car_repo.get_specs()
        self.car = Car(screen, pygame, car_specs[0])

    def update(self):
        if self.moving_right and self.car.right < self.screen_rect.right:
            self.drive(DrivingDirection.RIGHT, 1)
        elif self.moving_left and self.car.left < 0:
            self.drive(DrivingDirection.LEFT, 1)
        elif self.moving_up and self.car.top > 0:
            self.drive(DrivingDirection.FORWARD, 1)
        elif self.moving_down and self.car.bottom < self.screen_rect.bottom:
            self.drive(DrivingDirection.BACKWARD, 1)
    
    def is_inside_shape(self, road):
        x, y = self.car.position.x, self.car.position.y
        return (road.position.x <= x <= road.position.x + road.width and
            road.position.y <= y <= road.position.y + road.length)

class SelfDrivingCar():
    def __init__(self, car, step = 1):
        self.start_position = Position(0,0)
        self.end_position = Position(0,0)
        self.current_position = self.start_position    
        self.car = car
        self.step = step
    
    def set_start_position(self, position):
        self.start_position = position
        self.current_position = self.start_position
        self.car.position = self.current_position

    def add_destination(self, position):
        self.end_position = position

    def drive(self):
        if not self.current_position.is_same_position(self.end_position):
            proposed_destinations = self.current_position.get_positions_in_four_directions(self.step)
            calculated_shortest_position = self.end_position.find_shortest_distance_to_position(proposed_destinations)
            self.current_position = calculated_shortest_position
            self.car.position = self.current_position