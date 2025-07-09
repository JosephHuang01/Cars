import pygame
from components.settings import Settings
from database.car_explorer_3 import CarNavigation
from components.game_functions_2 import GameFunctions as gf
from components.map import Map

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Quick Start')

    grid = Map(screen)
    car_explorer = CarNavigation(ai_settings, screen)
    car_a = car_explorer.get_one_car()
    car_id = car_a.car_id
    row_one = car_explorer.get_last_trip_position(car_id)

    car_row = row_one.y
    car_column = row_one.x

    while True:
        gf.check_events(car_explorer)
        screen.fill(ai_settings.bg_color)
        for row in range(grid.grid_size):
            for column in range(grid.grid_size):
                color = (0, 128, 0)
                grid_x = (grid.margin + grid.cell_size) * column + grid.margin
                grid_y = (grid.margin + grid.cell_size) * row + grid.margin
                pygame.draw.rect(screen, color, [grid_x, grid_y, grid.cell_size, grid.cell_size])
        
        car_x = (grid.margin + grid.cell_size) * car_column + grid.margin
        car_y = (grid.margin + grid.cell_size) * car_row + grid.margin
        
        rotated_car = pygame.transform.rotate(car_explorer.image, car_explorer.angle)
        rotated_rect = rotated_car.get_rect(center=(car_x + grid.cell_size/2, car_y + grid.cell_size/2))
        screen.blit(rotated_car, rotated_rect.topleft)
        
        pygame.display.flip()

run_game()