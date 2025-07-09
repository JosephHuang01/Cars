import pygame
from components.settings import Settings
from components.map import Map

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    grid_map = Map(screen)
    pygame.display.set_caption('Quick Start')

    #car_explorer = CarNavigation(ai_settings, screen)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        grid_map.draw_grid()
        grid_map.blit()
        pygame.display.flip()
    
    pygame.quit()

run_game()