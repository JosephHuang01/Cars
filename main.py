# from components.battery import Battery

# #python  components/battery_unit_test.py

# test_battery_1 = Battery()
# test_battery_1.travel_distance(25)

# import sys
# print (sys.path )
# #battery_1 = Battery.traveled_distance(25)

import pygame
from factories.build_specification import BuildSpecification
from components.car import CarColor, RandomizeCarColor, CarList
#import pygame_gui

pygame.init()

font = pygame.font.SysFont(None, 24)

build_specification = BuildSpecification()
color_randomizer = RandomizeCarColor()
# car_model = CarModel('', '', 0)
car_color = color_randomizer.randomize_car_color()
# random_car_model = car_model.randomize_car_model()
car_list = CarList.randomize_model_list(self = '')

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

GRID_SIZE = 8
CELL_SIZE = 75
MARGIN = 10

pygame.display.set_caption('Quick Start')

window_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

car_row = 0.5
car_column = 3.5
destination_row = 5.5
destination_column = 6.5

destinations = [
    (5.5, 6.5),
    (2.5, 1.5),
    (6.5, 0.5)
]

current_destination = 0
destination_row, destination_column = destinations[current_destination]

pause_time = 2000
is_paused = Falsepause_start = 0

move_speed = 0.01
#player = pygame.Rect((300, 250, 100, 200))
car_width = CELL_SIZE * 0.12
car_height = CELL_SIZE * 0.075

background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
car_surface = pygame.Surface((car_width, car_height), pygame.SRCALPHA)
car_surface.fill(car_color)
#manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))

grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

direction = 'RIGHT'
previous_direction = 'RIGHT'
status = 'Driving'

is_running = True

original_width = 120
original_height = 70

padding = 5
available_space = CELL_SIZE - 2 * padding
scale_factor = min(available_space/original_width, available_space/original_height)

while is_running:
    window_surface.fill(CarColor.WHITE)
    for row in range(GRID_SIZE):
        for column in range(GRID_SIZE):
            color = CarColor.GREEN
            if grid[row][column] == 1:
                color = CarColor.BLUE
            x = (MARGIN + CELL_SIZE) * column + MARGIN
            y = (MARGIN + CELL_SIZE) * row + MARGIN
            pygame.draw.rect(window_surface, color, [x, y, CELL_SIZE, CELL_SIZE])
    
    car_x = (MARGIN + CELL_SIZE) * car_column + MARGIN
    car_y = (MARGIN + CELL_SIZE) * car_row + MARGIN

    # center_x = car_x + CELL_SIZE/2
    # center_y = car_y + CELL_SIZE/2

    player = pygame.Rect(car_x + (CELL_SIZE - car_width)/2, car_y + (CELL_SIZE - car_height)/2, car_width, car_height)

    #background.fill(pygame.Color("#08226D"))
    #window_surface.fill((173, 216, 230))

    #scale_factor = CELL_SIZE/60
    #center_offset = CELL_SIZE/2

    # player = [
    # (center_x - scale_factor * 60, center_y + scale_factor * 35),  # Rear left
    # (center_x + scale_factor * 60, center_y + scale_factor * 35),  # Rear right
    # (center_x + scale_factor * 60, center_y - scale_factor * 5),   # Front right
    # (center_x + scale_factor * 20, center_y - scale_factor * 35),  # Nose right
    # (center_x - scale_factor * 20, center_y - scale_factor * 35),  # Nose left
    # (center_x - scale_factor * 60, center_y - scale_factor * 5)    # Front left
        # (car_x + 120, car_y),
        # (car_x + 120, car_y - 40),
        # (car_x + 80, car_y - 70),
        # #(car_x + 80, car_y - 40),
        # (car_x + 40, car_y - 70),
        # #(car_x + 40, car_y - 40),
        # (car_x, car_y - 40)
    #]

    #pygame.draw.rect(window_surface, car_color, player)

    #pygame.draw.polygon(window_surface, CarColor.BLUE, player)
    #pygame.draw.polygon(window_surface, CarColor.RED, player)
    #pygame.draw.polygon(window_surface, CarColor.BLUE, player)
    #pygame.draw.polygon(window_surface, color_randomizer.randomize_car_color(), player)

    wheel_radius = 5

    # pygame.draw.circle(window_surface, (CarColor.GRAY),
    #                    (int(center_x + scale_factor * 30), int(center_y + scale_factor * 35 + 5)), wheel_radius)
    # pygame.draw.circle(window_surface, (CarColor.GRAY),
    #                    (int(center_x - scale_factor * 30), int(center_y + scale_factor * 35 + 5)), wheel_radius)

    if not is_paused:
        if abs(car_column - destination_column) > 0.01:
            if car_column < destination_column:
                car_column += move_speed
                direction = 'RIGHT'
            elif car_column > destination_column:
                car_column -= move_speed
                direction = 'LEFT'
        elif abs(car_row - destination_row) > 0.01:
            if car_row < destination_row:
                car_row += move_speed
                direction = 'DOWN'
            elif car_row > destination_row:
                car_row -= move_speed
                direction = 'UP'
        else:
            status = 'Arrived'
            is_paused = True
            pause_start = pygame.time.get_ticks()
    else:
        if pygame.time.get_ticks() - pause_start >= pause_time:
            current_destination += 1
            if current_destination < len(destinations):
                destination_row
    
        if status != 'Arrived':
            if direction != previous_direction:
                status = 'Turning'
            else:
                status = 'Driving'
    
    angle = 0
    if direction == 'RIGHT':
        angle = 0
    elif direction == 'LEFT':
        angle = 180
    elif direction == 'UP':
        angle = 90
    elif direction == 'DOWN':
        angle = 270
    
    rotated_car = pygame.transform.rotate(car_surface, angle)
    rotated_rect = rotated_car.get_rect(center=(car_x + CELL_SIZE/2, car_y + CELL_SIZE/2))
    window_surface.blit(rotated_car, rotated_rect.topleft)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type ==  pygame.KEYDOWN:
            if event.key == pygame.K_a and car_column > 0:
                car_column -= 1
        #player.move_ip(-1, 0)
            elif event.key == pygame.K_d and car_column < GRID_SIZE - 1:
                car_column += 1
        #player.move_ip(1, 0)
            elif event.key == pygame.K_w and car_row > 0:
                car_row -= 1
        #player.move_ip(0, -1)
            elif event.key == pygame.K_s and car_row < GRID_SIZE - 1:
                car_row += 1
        #player.move_ip(0, 1)
    
    # status_text = font.render("Status: " + status, True, (0, 0, 0))
    # direction_text = font.render("Direction: " + direction, True, (0, 0, 0))
    # window_surface.blit(status_text, (50, 50))
    # window_surface.blit(direction_text, (50, 90))

    table_x = 40
    table_y = 40
    cell_width = 120
    cell_height = 40
    rows = 5
    cols = 2

    table_data = [
        ["Status", status],
        ["Direction", direction],
        ["Make", car_list.make],
        ["Model", car_list.model],
        ["Year", car_list.year]
    ]

    table_border_color = (0, 0, 0)
    cell_background_color = (200, 200, 200)
    text_color = (0, 0, 0)
    table_padding = 5
    table_width = 2 * cell_width
    table_height = 5 * cell_height
    table_margin = 20
    table_x = SCREEN_WIDTH - table_width- table_margin
    table_y = SCREEN_HEIGHT - table_height - table_margin

    for row in range(rows):
        for col in range(cols):
            cell_x = table_x + col * cell_width
            cell_y = table_y + row * cell_height
            pygame.draw.rect(window_surface, cell_background_color, (cell_x, cell_y, cell_width, cell_height))
            pygame.draw.rect(window_surface, table_border_color, (cell_x, cell_y, cell_width, cell_height), 2)
            cell_text = font.render(str(table_data[row][col]), True, text_color)
            text_rect = cell_text.get_rect(center=(cell_x + cell_width/2, cell_y + cell_height/2))
            window_surface.blit(cell_text, text_rect)

    pygame.display.update()
    pygame.time.Clock().tick(60)

pygame.quit()