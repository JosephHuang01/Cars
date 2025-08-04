import pygame
from components.settings import Settings
from services.builder import Builder
from services.driving import SelfDrivingCar
from components.position import Position
def run_game():
    pygame.init()
    ai_settings = Settings()
        
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Quick Start')
    builder = Builder(screen, pygame)
    builder.build()
    roads = builder.roads[0:4]

    first_car = builder.cars[0]
    self_driving_car = SelfDrivingCar(first_car)
    self_driving_car.is_inside_shape(roads)
    starting_position = Position(100, 100)
    ending_position = Position(300, 400)
    self_driving_car.set_start_position(starting_position)
    self_driving_car.add_destination(ending_position)

    second_car = builder.cars[1]
    alternative_self_driving_car = SelfDrivingCar(second_car)
    second_starting_position = Position(600, 600)
    second_ending_position = Position(700, 400)
    alternative_self_driving_car.set_start_position(second_starting_position)
    alternative_self_driving_car.add_destination(second_ending_position)

    third_car = builder.cars[2]
    final_self_driving_car = SelfDrivingCar(third_car)
    third_starting_position = Position(1460, 675)
    third_ending_position = Position(1200, 400)
    final_self_driving_car.set_start_position(third_starting_position)
    final_self_driving_car.add_destination(third_ending_position)

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        self_driving_car.drive()
        alternative_self_driving_car.drive()
        final_self_driving_car.drive()
        builder.show()

        pygame.display.flip()
        clock.tick(60)

run_game()