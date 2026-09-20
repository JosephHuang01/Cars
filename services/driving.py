from database.car_repo import CarRepo
from components.car import Car
from components.driving_direction import DrivingDirection
from components.position import Position
from database.road_repo import RoadRepo
from database.car_repo import CarRepo

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

class SelfDrivingCar():
    def __init__(self, map, car, step = 1):
        self.map = map
        self.start_position = Position(0,0)
        self.end_position = Position(0,0)
        self.current_position = self.start_position    
        self.car = car
        self.step = step
        self.road_repo = RoadRepo()
        self.road_specs = self.road_repo.get_specs()
        self.car_repo = CarRepo()
        self.car_specs = self.car_repo.get_specs()
    
    def set_start_position(self, position):
        self.start_position = position
        self.current_position = self.start_position
        self.car.position = self.current_position

    def add_destination(self, position):
        self.end_position = position

    def drive(self):
        if not self.current_position.is_same_position(self.end_position):
            proposed_destinations = self.current_position.get_positions_in_four_directions(self.step)
            proposed_destinations_on_road_or_in_city = []
            for position in proposed_destinations:
                if (self.map.is_position_on_road(position)):
                    proposed_destinations_on_road_or_in_city.append(position)
                elif (self.map.is_position_on_city(position)):
                    proposed_destinations_on_road_or_in_city.append(position)

            calculated_shortest_position = self.end_position.find_shortest_distance_to_position(proposed_destinations_on_road_or_in_city)
            self.current_position = calculated_shortest_position
            self.car.position = self.current_position
            print ("Proposed positions: ", proposed_destinations)
            print ("On road or in city: ", proposed_destinations_on_road_or_in_city)
            print ("Shortest position: ", self.current_position)