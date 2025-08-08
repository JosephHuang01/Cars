import pygame
from components.settings import Settings
from services.builder import Builder
from services.driving import SelfDrivingCar
from components.position import Position
from components.map import Map

def run_game():
    pygame.init()
    ai_settings = Settings()
        
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Quick Start')
    builder = Builder(screen, pygame)
    builder.build()
    map = builder.get_map()

    first_car = builder.cars[0]
    self_driving_car = SelfDrivingCar(map, first_car)
    starting_position = Position(44, 47) # Position(946, 164)
    ending_position = Position(1277, 662)
    self_driving_car.set_start_position(starting_position)
    self_driving_car.add_destination(ending_position)

    second_car = builder.cars[1]
    second_self_driving_car = SelfDrivingCar(map, second_car)
    # second_starting_position = builder.cities[4]
    second_starting_position = Position(1455, 90)
    # second_ending_position = builder.cities[1]
    second_ending_position = Position(218, 507)
    second_self_driving_car.set_start_position(second_starting_position)
    second_self_driving_car.add_destination(second_ending_position)

    third_car = builder.cars[2]
    third_self_driving_car = SelfDrivingCar(map, third_car)
    third_starting_position = Position(1274, 662)
    third_ending_position = Position(805, 162)
    third_self_driving_car.set_start_position(third_starting_position)
    third_self_driving_car.add_destination(third_ending_position)

    fourth_car = builder.cars[3]
    fourth_self_driving_car = SelfDrivingCar(map, fourth_car)
    fourth_starting_position = Position(614, 707)
    fourth_ending_position = Position(44, 47)
    fourth_self_driving_car.set_start_position(fourth_starting_position)
    fourth_self_driving_car.add_destination(fourth_ending_position)

    fifth_car = builder.cars[4]
    fifth_self_driving_car = SelfDrivingCar(map, fifth_car)
    fifth_starting_position = Position(805, 162)
    fifth_ending_position = Position(1455, 90)
    fifth_self_driving_car.set_start_position(fifth_starting_position)
    fifth_self_driving_car.add_destination(fifth_ending_position)

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        self_driving_car.drive()
        second_self_driving_car.drive()
        third_self_driving_car.drive()
        fourth_self_driving_car.drive()
        fifth_self_driving_car.drive()
        builder.show()

        pygame.display.flip()
        clock.tick(30)

run_game()