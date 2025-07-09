import pygame
from components.settings import Settings
from database.car_explorer_2 import CarModel
from components.game_functions import GameFunctions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Quick Start')

    car_explorer = CarModel(ai_settings, screen)

    while True:
        gf.check_events(car_explorer)
        car_explorer.update()
        gf.update_screen(ai_settings, screen, car_explorer)

        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT():
        #         sys.exit()
        
        screen.fill(ai_settings.bg_color)
        car_explorer.blitme()
        
        pygame.display.flip()

run_game()