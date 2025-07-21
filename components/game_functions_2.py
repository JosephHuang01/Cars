import sys
import pygame
from components.map import Map
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
        #grid = Map()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                GameFunctions.check_keydown_events(event, car_explorer)
            elif event.type == pygame.KEYUP:
                GameFunctions.check_keyup_events(event, car_explorer)
        
        #if car_explorer.moving_right and car_column < grid.grid_size - 1:
        if car_explorer.moving_right:
                car_explorer.drive(DrivingDirection.RIGHT, 1)
        elif car_explorer.moving_left:
                car_explorer.drive(DrivingDirection.LEFT, 1)
        elif car_explorer.moving_up:
                car_explorer.drive(DrivingDirection.FORWARD, 1)
        elif car_explorer.moving_down:
                car_explorer.drive(DrivingDirection.BACKWARD, 1)
                # car_column += 1
                # car_explorer.moving_right = False
                # car_explorer.direction = 'RIGHT'
                # car_explorer.angle = 0
        # elif car_explorer.moving_left and car_column > 0:
        #     car_column -= 1
        #     car_explorer.moving_left = False
        #     car_explorer.direction = 'LEFT'
        #     car_explorer.angle = 180
        # elif car_explorer.moving_up and car_row > 0:
        #     car_row -= 1
        #     car_explorer.moving_up = False
        #     car_explorer.direction = 'UP'
        #     car_explorer.angle = 90
        # elif car_explorer.moving_down and car_row < grid.grid_size - 1:
        #     car_row += 1
        #     car_explorer.moving_down = False
        #     car_explorer.direction = 'DOWN'
        #     car_explorer.angle = 270

    def update_screen(ai_settings, screen, car_explorer):
        #screen.fill(ai_settings.bg_color)
        car_explorer.blitme()

        pygame.display.flip()