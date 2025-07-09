import sys
import pygame

class GameFunctions():
    def check_keydown_events(event, car_explorer):
        if event.key == pygame.K_RIGHT:
            car_explorer.moving_right = True
        elif event.key == pygame.K_LEFT:
            car_explorer.moving_left= True
        elif event.key == pygame.K_UP:
            car_explorer.moving_up = True
        elif event.key == pygame.K_DOWN:
            car_explorer.moving_down = True
    
    def check_keyup_events(event, car_explorer):
        if event.key == pygame.K_RIGHT:
            car_explorer.moving_right = False
        elif event.key == pygame.K_LEFT:
            car_explorer.moving_left = False
        elif event.key == pygame.K_UP:
            car_explorer.moving_up = False
        elif event.key == pygame.K_DOWN:
            car_explorer.moving_down = False

    def check_events(car_explorer):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                GameFunctions.check_keydown_events(event, car_explorer)
            elif event.type == pygame.KEYUP:
                GameFunctions.check_keyup_events(event, car_explorer)

    def update_screen(ai_settings, screen, car_explorer):
        #screen.fill(ai_settings.bg_color)
        car_explorer.blitme()

        pygame.display.flip()