import pygame
from components.settings import Settings
from components.map import Map
from components.city import City
from components.shape import Shape, ShapeSpecification
from components.position import Position
from components.common_game_color import CommonGameColor
from components.car import Car
from database.city_repo import CityRepo

def run_game():
    pygame.init()
    ai_settings = Settings()
        
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    
    shape_spec_map = ShapeSpecification()
    shape_spec_map.name = 'Game Map'
    shape_spec_map.type = 'map'
    shape_spec_map.width = ai_settings.screen_width - 50
    shape_spec_map.length = ai_settings.screen_height - 50
    
    grid_map = Map(screen, pygame, shape_spec_map)
    grid_map.center_position()
    pygame.display.set_caption('Quick Start')
    cities = CityRepo(screen, pygame).get_cities()
    for city in cities:
        grid_map.add_city(city)
    #__cityReference = City(screen, pygame, shape_spec)
    #car_reference = Car(screen, pygame, shape_spec)
    # for city in __cityReference.get_popular_cities():
    #     grid_map.add_city(city)
    # for car in car_reference.get_car():
    #     grid_map.add_car(car)

    #new_position = Position(250, 250)
    # demo_shape = Shape(screen, pygame, 'demo', 'shape', new_position, 150, 150
    #                    , CommonGameColor.WHITE, (255, 255, 255))
    demo_shape = Shape(screen, pygame, ShapeSpecification())
    demo_shape.drawing_points = [Position(125, 125), Position(650, 650), Position(650, 125), Position(125, 125)]
    demo_shape.drawing_points = [Position(700, 400), Position(800, 500), Position(750, 600), Position(650, 600)
                                 , Position(600, 500), Position(700, 400)]
    demo_car = Shape(screen, pygame, ShapeSpecification())

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        #grid_map.surface.fill((0,0,0))
        
        grid_map.show()
        grid_map.show_cities()
        demo_shape.show()
        grid_map.show_cars()
        demo_car.show()
        
        #demo_shape.draw_rectangle(demo_shape.name, center_position, __cityReference.width, __cityReference.length)
        #demo_shape.draw_text_on_rectangle(demo_shape.name, center_position, __cityReference.width, __cityReference.length)
        #demo_shape.show()
        pygame.display.flip()

run_game()