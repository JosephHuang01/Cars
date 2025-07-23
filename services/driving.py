from components.map import Map
from database.car_repo import CarRepo
from components.shape import Shape, ShapeSpecification
from components.car import Car
import sys
import pygame
from components.driving_direction import DrivingDirection
from components.position import Position

class Driving():
    def __init__(self, screen, pygame):
        self.screen = screen
        self.pygame = pygame
        self.shape_specs = ShapeSpecification()
        self.map = Map(screen, pygame, self.shape_specs)
        self.car_repo = CarRepo()
        car_specs = self.car_repo.get_specs()
        self.car = Car(screen, pygame, car_specs[0])
        self.screen_rect = screen.get_rect()
        self.car.centerx = self.screen_rect.centerx
        self.car.centery = self.screen_rect.centery
        self.centerx = float(self.car.centerx)
        self.centery = float(self.car.centery)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    # def check_keydown_events(event, car_explorer):
    #     if event.key == pygame.K_RIGHT:
    #         car_explorer.moving_right = True
    #     elif event.key == pygame.K_LEFT:
    #         car_explorer.moving_left= True
    #     elif event.key == pygame.K_UP:
    #         car_explorer.moving_up = True
    #     elif event.key == pygame.K_DOWN:
    #         car_explorer.moving_down = True
    
    # def check_keyup_events(event, car_explorer):
    #     if event.key == pygame.K_RIGHT:
    #         car_explorer.moving_right = False
    #     elif event.key == pygame.K_LEFT:
    #         car_explorer.moving_left = False
    #     elif event.key == pygame.K_UP:
    #         car_explorer.moving_up = False
    #     elif event.key == pygame.K_DOWN:
    #         car_explorer.moving_down = False

    def update(self):
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
        #         sys.exit()
        #     elif event.type == pygame.KEYDOWN:
        #         Driving.check_keydown_events(event, car_explorer)
        #     elif event.type == pygame.KEYUP:
        #         Driving.check_keyup_events(event, car_explorer)
        
        if self.moving_right and self.car.right < self.screen_rect.right:
            #self.centerx
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

        # points = [(p.x, p.y) for p in road.drawing_points]
        # inside = False
        # length = len(points)
        # span = length - 1
        # for i in range(length):
        #     xi, yi = points[i]
        #     xj, yj = points[span]
        # if ((yi > y) != (yj > y)) and \
        #    (x < (xj - xi) * (y - yi) / ((yj - yi) or 1e-10) + xi):
        #     inside = not inside
        # span = i
        
    #     self.car.centerx = self.centerx
    #     self.car.centery = self.centery
    
    # def blitme(self):
    #     self.screen.blit()

class SelfDrivingCar():
    def __init__(self, screen, pygame, car):
        self.start_position = Position(Position.x)
        self.end_position = Position(Position.y)
        self.car = car
    
    def set_start_position(self):
        pass

    def add_destination(self):
        pass

    def drive(self):
        self.start_position = Position(250, 250)
        self.position = self.start_position
        self.end_position = Position(500, 600)
        self.potential_path_one = Position(375, 250)
        self.potential_path_two = Position(250, 375)
        self.potential_path_three = Position(125, 250)
        self.potential_path_four = Position(250, 125)

        paths = [
            self.potential_path_one,
            self.potential_path_two,
            self.potential_path_three,
            self.potential_path_four
        ]

        def shortest_distance(position_one, position_two):
            moving_x = position_one.x - position_two.x
            moving_y = position_one.y - position_two.y
            #next_position = min(paths, key=lambda)