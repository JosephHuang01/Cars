import sys
import pygame
from components.driving_direction import DrivingDirection

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
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                GameFunctions.check_keydown_events(event, car_explorer)
            elif event.type == pygame.KEYUP:
                GameFunctions.check_keyup_events(event, car_explorer)
        
        if car_explorer.moving_right:
                car_explorer.drive(DrivingDirection.RIGHT, 1)
                car_explorer.angle = 0
        elif car_explorer.moving_left:
                car_explorer.drive(DrivingDirection.LEFT, 1)
                car_explorer.angle = 180
        elif car_explorer.moving_up:
                car_explorer.drive(DrivingDirection.FORWARD, 1)
                car_explorer.angle = 90
        elif car_explorer.moving_down:
                car_explorer.drive(DrivingDirection.BACKWARD, 1)
                car_explorer.angle = 270

    def update_screen(ai_settings, screen, car_explorer):
        car_explorer.blitme()

        pygame.display.flip()