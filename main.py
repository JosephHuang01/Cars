# from components.battery import Battery

# #python  components/battery_unit_test.py

# test_battery_1 = Battery()
# test_battery_1.travel_distance(25)

# import sys
# print (sys.path )
# #battery_1 = Battery.traveled_distance(25)

import pygame
from factories.build_specification import BuildSpecification
from components.car import CarColor, RandomizeCarColor, CarModel
#import pygame_gui

pygame.init()

build_specification = BuildSpecification()
color_randomizer = RandomizeCarColor()
# car_model = CarModel('', '', 0)
car_color = color_randomizer.randomize_car_color()
# random_car_model = car_model.randomize_car_model()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

GRID_SIZE = 10
CELL_SIZE = 50
MARGIN = 5

pygame.display.set_caption('Quick Start')

window_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

car_x = 300
car_y = 300
#player = pygame.Rect((300, 250, 100, 200))

background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
#manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))

grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

is_running = True

while is_running:
    for row in range(GRID_SIZE):
        for column in range(GRID_SIZE):
            x = (MARGIN + CELL_SIZE) * column + MARGIN
            y = (MARGIN + CELL_SIZE) * row + MARGIN

    #background.fill(pygame.Color("#08226D"))
    #window_surface.fill((173, 216, 230))
    window_surface.fill(CarColor.BLACK)

    player = [
        (car_x, car_y),
        (car_x + 120, car_y),
        (car_x + 120, car_y - 40),
        (car_x + 80, car_y - 70),
        #(car_x + 80, car_y - 40),
        (car_x + 40, car_y - 70),
        #(car_x + 40, car_y - 40),
        (car_x, car_y - 40)
    ]

    #pygame.draw.polygon(window_surface, CarColor.BLUE, player)
    #pygame.draw.polygon(window_surface, CarColor.RED, player)
    pygame.draw.polygon(window_surface, car_color, player)
    #pygame.draw.polygon(window_surface, color_randomizer.randomize_car_color(), player)

    pygame.draw.circle(window_surface, (CarColor.GRAY), (car_x + 25, car_y + 10), 15)
    pygame.draw.circle(window_surface, (CarColor.GRAY), (car_x + 95, car_y + 10), 15)

    # Draw car body
    # shifted_body = [(car_x + x, car_y + y) for (x, y) in random_car_model.body_shape]
    # pygame.draw.polygon(window_surface, random_car_model.color, shifted_body)

    # Draw wheels
    # pygame.draw.circle(window_surface, (CarColor.GRAY), (car_x + 25, car_y + 10), random_car_model.wheel_size)
    # pygame.draw.circle(window_surface, (CarColor.GRAY), (car_x + 95, car_y + 10), random_car_model.wheel_size)

    # Optional: Add unique accessories
    # if 'spoiler' in random_car_model.accessories:
    #     pygame.draw.rect(window_surface, (150, 150, 150), (car_x + 40, car_y - 80, 40, 5))
    # if 'sunroof' in random_car_model.accessories:
    #     pygame.draw.rect(window_surface, (100, 100, 100), (car_x + 40, car_y - 60, 40, 10))

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        car_x -= 2
        #player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        car_x += 2
        #player.move_ip(1, 0)
    elif key[pygame.K_w] == True:
        car_y -= 2
        #player.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        car_y += 2
        #player.move_ip(0, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    #window_surface.blit(background, (0, 0))
    pygame.display.update()

pygame.quit()