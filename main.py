import pygame
from components.settings import Settings
from components.map import Map
from components.city import City

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    grid_map = Map(screen)
    pygame.display.set_caption('Quick Start')
    cityReference = City('', 0, 0, grid_map)
    for city in cityReference.get_popular_cities():
            grid_map.add_city(city)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        grid_map.surface.fill((128, 128, 128))
        grid_map.show_cities()
       
        grid_map.show()
        pygame.display.flip()

run_game()