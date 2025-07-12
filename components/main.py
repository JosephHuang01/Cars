import pygame
from factories.build_specification import BuildSpecification
from components.car import CommonGameColor, RandomizeCarColor
#import pygame_gui

# todo: move this to main.py in the root folder

pygame.init()

build_specification = BuildSpecification()
randomize_car_color = RandomizeCarColor()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.display.set_caption('Quick Start')

window_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

car_x = 300
car_y = 300
#player = pygame.Rect((300, 250, 100, 200))

background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
#manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))

is_running = True

while is_running:
    #background.fill(pygame.Color("#08226D"))
    #window_surface.fill((173, 216, 230))
    window_surface.fill(build_specification.color_list[0])

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

    pygame.draw.polygon(window_surface, build_specification.color_list[2], player)
    pygame.draw.polygon(window_surface, CommonGameColor.RED, player)

    pygame.draw.circle(window_surface, (50, 50, 50), (car_x + 25, car_y + 10), 15)
    pygame.draw.circle(window_surface, (50, 50, 50), (car_x + 95, car_y + 10), 15)

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