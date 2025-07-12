import pygame
from components.settings import Settings
from components.map import Map
from components.city import City
from components.shape import Shape
from components.position import Position

def run_game():
    pygame.init()
    ai_settings = Settings()
        
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    
    map_position = Position(350, 350)
    grid_map = Map(screen, pygame, 'map', 'map', map_position
                    , ai_settings.screen_width - 50, ai_settings.screen_height - 50, (128, 128, 128), (255, 255, 255))
    grid_map.center_position()
    pygame.display.set_caption('Quick Start')
    __cityReference = City(screen, pygame, grid_map.name, type, grid_map.position, 75, 75, grid_map.bg_color, grid_map.fg_color, map)
    for city in __cityReference.get_popular_cities():
        grid_map.add_city(city)

    new_position = Position(250, 250)
    demo_shape = Shape(screen, pygame, 'demo', 'shape', new_position, 150, 150, (128, 128, 128), (255, 255, 255))
    
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        #grid_map.surface.fill((0,0,0))
        
        grid_map.show()
        grid_map.show_cities()
        
        #demo_shape.draw_rectangle(demo_shape.name, center_position, __cityReference.width, __cityReference.length)
        #demo_shape.draw_text_on_rectangle(demo_shape.name, center_position, __cityReference.width, __cityReference.length)
        #demo_shape.show()
        pygame.display.flip()

run_game()