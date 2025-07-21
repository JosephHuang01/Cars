import pygame
from components.settings import Settings
from services.builder import Builder
from components.game_functions_2 import GameFunctions
from database.car_repo import CarRepo
from components.driving_direction import DrivingDirection

def run_game():
    pygame.init()
    ai_settings = Settings()
        
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Quick Start')
    builder = Builder(screen, pygame)
    builder.build()
    car_explorer = builder.cars[0]

    #__cityReference = City(screen, pygame, shape_spec)
    #car_reference = Car(screen, pygame, shape_spec)
    # for city in __cityReference.get_popular_cities():
    #     grid_map.add_city(city)
    # for car in car_reference.get_car():
    #     grid_map.add_car(car)

    #new_position = Position(250, 250)
    # demo_shape = Shape(screen, pygame, 'demo', 'shape', new_position, 150, 150
    #                    , CommonGameColor.WHITE, (255, 255, 255))

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))

        for car in builder.cars:
            if car.position.x < ai_settings.screen_width:
                car.drive(DrivingDirection.RIGHT, 1)
        
        builder.show()
        GameFunctions.check_events(car_explorer)
        #grid_map.surface.fill((0,0,0))
        
        #demo_shape.draw_rectangle(demo_shape.name, center_position, __cityReference.width, __cityReference.length)
        #demo_shape.draw_text_on_rectangle(demo_shape.name, center_position, __cityReference.width, __cityReference.length)
        #demo_shape.show()

        pygame.display.flip()
        clock.tick(60)

run_game()