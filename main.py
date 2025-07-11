import pygame
from components.settings import Settings
from components.map import Map
from components.city import City
from components.shape import Shape
from components.position import Position

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    grid_map = Map(screen)
    pygame.display.set_caption('Quick Start')
    __cityReference = City('', 0, 0, grid_map)
    for city in __cityReference.get_popular_cities():
            grid_map.add_city(city)

    new_position = Position(250, 250)
    demo_shape = Shape(screen, pygame, 'demo', 'shape', new_position, 150, 150)
       

    
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        grid_map.surface.fill((128, 128, 128))
        grid_map.show_cities()
        grid_map.show()
        
        demo_shape.draw_rectangle(demo_shape.name, new_position, __cityReference.width, __cityReference.length)
        demo_shape.draw_text_on_rectangle(demo_shape.name, new_position, __cityReference.width, __cityReference.length)
        #demo_shape.show()
        pygame.display.flip()

run_game()