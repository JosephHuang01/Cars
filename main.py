import pygame
from components.car import CarColor, RandomizeCarColor, Position
from datetime import datetime
from database.car_explorer import CarExplorer

car_explorer = CarExplorer()
car_a = car_explorer.get_one_car()
car_id = car_a.car_id
row_one = car_explorer.get_last_trip_position(car_id)

pygame.init()

text_input_rect = pygame.Rect(700, 300, 140, 32)
font = pygame.font.SysFont(None, 24)
text_input = ''

color_randomizer = RandomizeCarColor()
car_color = color_randomizer.randomize_car_color()
car_list = car_a # CarList.randomize_model_list(self = '')

state_grid_positions = {(6, 6): ("Atlanta", CarColor.BLUE)}

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

GRID_SIZE = 8
CELL_SIZE = 75
MARGIN = 10

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
active = False

car_row = row_one.y
car_column = row_one.x

x_1 = input("Please tell me the first x position? ")
print ('x_1: ', x_1)

y_1 = input("Please tell me the first y position? ")
print ('y_1: ', y_1)

destination_1 = Position(float(x_1), float(y_1))

x_2 = input("Please tell me the second x position? ")
print ('x_2: ', x_2)

y_2 = input("Please tell me the second y position? ")
print ('y_2: ', y_2)

destination_2 = Position(float(x_2), float(y_2))

destinations = [
    (destination_1.x, destination_1.y),
    (destination_2.x, destination_2.y),
]
start_date_time = datetime(2025, 6, 29, 3, 15, 7)
current_destination = 0
destination_column, destination_row = destinations[current_destination]

pause_time = 2000
pause_start = 0

move_speed = 0.01
car_width = CELL_SIZE * 0.12
car_height = CELL_SIZE * 0.075

background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
car_surface = pygame.Surface((car_width, car_height), pygame.SRCALPHA)
car_surface.fill(car_color)
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

direction = 'RIGHT'
previous_direction = 'RIGHT'
status = 'Driving'

is_running = True
button_width = 100
button_height = 40
button_x = 40
button_y = SCREEN_HEIGHT - button_height - 40
button_color = (CarColor.GRAY)
button_text_color = (CarColor.BLACK)
manual_pause = False

show_save_button = False
save_button_x = button_x + button_width + 20

manual_pause_start = 0
total_manual_pause_duration = 0
is_waiting = False

reached_destinations = []
original_width = 120
original_height = 70

padding = 5
available_space = CELL_SIZE - 2 * padding
scale_factor = min(available_space/original_width, available_space/original_height)

table_x = 40
table_y = 40
table_data = [
    ["Status", status],
    ["Direction", direction],
    ["Make", car_list.make],
    ["Model", car_list.model],
    ["Year", car_list.year]
]

cell_width = 120
cell_height = 40
rows = 5
cols = 2

table_border_color = CarColor.BLACK
cell_background_color = CarColor.GRAY
text_color = CarColor.BLACK
table_padding = 5
table_width = 2 * cell_width
table_height = 5 * cell_height
table_margin = 20
table_x = SCREEN_WIDTH - table_width - table_margin
table_y = SCREEN_HEIGHT - table_height - table_margin

while is_running:
    window_surface.fill(CarColor.WHITE)
    for row in range(GRID_SIZE):
        for column in range(GRID_SIZE):
            color = CarColor.GREEN
            if (row, column) in state_grid_positions:
                state_name, state_color = state_grid_positions[(row, column)]
                color = state_color
            grid_x = (MARGIN + CELL_SIZE) * column + MARGIN
            grid_y = (MARGIN + CELL_SIZE) * row + MARGIN
            pygame.draw.rect(window_surface, color, [grid_x, grid_y, CELL_SIZE, CELL_SIZE])
            if (row, column) in state_grid_positions:
                state_name, _ = state_grid_positions[(row, column)]
                text_surface = font.render(state_name, True, CarColor.BLACK)
                text_rect = text_surface.get_rect(center=(grid_x + CELL_SIZE/2, grid_y + CELL_SIZE/2))
                window_surface.blit(text_surface, text_rect)
    
    car_x = (MARGIN + CELL_SIZE) * car_column + MARGIN
    car_y = (MARGIN + CELL_SIZE) * car_row + MARGIN
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

    pygame.draw.rect(window_surface, button_color, (button_x, button_y, button_width, button_height))
    button_label = 'Resume' if manual_pause else 'Pause'
    button_text = font.render(button_label, True, button_text_color)
    button_text_rect = button_text.get_rect(center=(button_x + button_width/2, button_y + button_height/2))
    window_surface.blit(button_text, button_text_rect)

    if show_save_button:
        pygame.draw.rect(window_surface, button_color, (save_button_x, button_y, button_width, button_height))
        save_button_text = font.render('Save', True, button_text_color)
        save_button_text_rect = save_button_text.get_rect(center=(save_button_x + button_width / 2, button_y + button_height / 2))
        window_surface.blit(save_button_text, save_button_text_rect)
    
    pygame.draw.rect(window_surface, CarColor.BLUE, text_input_rect)
    pygame.draw.rect(window_surface, CarColor.BLUE, text_input_rect, 2)
    text_surface = font.render(text_input, True, CarColor.BLACK)
    window_surface.blit(text_surface, (text_input_rect.x + 5, text_input_rect.y + 5))
    text_input_rect.w = max(100, text_surface.get_width() + 10)

    for row in range(rows):
        for col in range(cols):
            cell_x = table_x + col * cell_width
            cell_y = table_y + row * cell_height
            pygame.draw.rect(window_surface, cell_background_color, (cell_x, cell_y, cell_width, cell_height))
            pygame.draw.rect(window_surface, table_border_color, (cell_x, cell_y, cell_width, cell_height), 2)
            cell_text = font.render(str(table_data[row][col]), True, text_color)
            text_rect = cell_text.get_rect(center=(cell_x + cell_width/2, cell_y + cell_height/2))
            window_surface.blit(cell_text, text_rect)
    
    dest_table_width = 2 * cell_width
    dest_table_y = table_margin
    pygame.draw.rect(window_surface, cell_background_color, (table_x, dest_table_y, dest_table_width, cell_height))
    pygame.draw.rect(window_surface, table_border_color, (table_x, dest_table_y, dest_table_width, cell_height), 2)
    header_text = font.render("Reached Destinations", True, text_color)
    header_rect = header_text.get_rect(center = (table_x + dest_table_width/2, dest_table_y + cell_height/2))
    window_surface.blit(header_text, header_rect)

    player = pygame.Rect(car_x + (CELL_SIZE - car_width)/2, car_y + (CELL_SIZE - car_height)/2, car_width, car_height)
    wheel_radius = 5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and car_column > 0:
                car_column -= 1
            elif event.key == pygame.K_d and car_column < GRID_SIZE - 1:
                car_column += 1
            elif event.key == pygame.K_w and car_row > 0:
                car_row -= 1
            elif event.key == pygame.K_s and car_row < GRID_SIZE - 1:
                car_row += 1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if (button_x <= mouse_x <= button_x + button_width) and (button_y <= mouse_y <= button_y + button_height):
                if is_waiting:
                    if manual_pause:
                        total_manual_pause_duration += pygame.time.get_ticks() - manual_pause_start
                    else:
                        manual_pause_start = pygame.time.get_ticks()
                manual_pause = not manual_pause
                show_save_button = manual_pause
            if show_save_button:
                if (save_button_x <= mouse_x <= save_button_x + button_width) and (button_y <= mouse_y <= button_y + button_height):
                    current_x = car_column
                    current_y = car_row
                    current_time = datetime.now()
                    car_explorer.save_trip(car_id, row_one.StartX, row_one.StartY, current_x, current_y, start_date_time, current_time)
                    print("Saved current position: ", current_x, current_y, "at", current_time)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if text_input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                text_input = text_input[:-1]
            else:
                text_input += event.unicode
    
    #pygame.display.flip()

    if not manual_pause:
        if status == 'Driving':
            if abs(car_column - destination_column) > 0.01:
                if car_column < destination_column:
                    car_column += move_speed
                    previous_direction = direction
                    direction = 'RIGHT'
                elif car_column > destination_column:
                    car_column -= move_speed
                    previous_direction = direction
                    direction = 'LEFT'
            elif abs(car_row - destination_row) > 0.01:
                if car_row < destination_row:
                    car_row += move_speed
                    previous_direction = direction
                    direction = 'DOWN'
                elif car_row > destination_row:
                    car_row -= move_speed
                    previous_direction = direction
                    direction = 'UP'
            else:
                status = 'Arrived'
                pause_start = pygame.time.get_ticks()
                is_waiting = True
                total_manual_pause_duration = 0
                reached_destinations.append((destination_column, destination_row))
        elif status == 'Arrived' and is_waiting:
            if pygame.time.get_ticks() - pause_start - total_manual_pause_duration >= pause_time:
                current_destination += 1
                if current_destination < len(destinations):
                    destination_column, destination_row = destinations[current_destination]
                    status = 'Driving'
                    is_waiting = False
                else:
                    status = 'Trip Complete'
    else:
        if is_waiting:
            pass

    if status != 'Arrived':
        status = 'Driving'

    pygame.display.update()
    pygame.time.Clock().tick(60)
pygame.quit()

# Save the x, y to database
#CarId, StartX, StartY, EndX, EndY, StartDateTime, EndDateTime
car_id_insert = car_id
start_x_insert = row_one.x
start_y_insert = row_one.y
end_x_insert = destination_1.x
end_y_insert = destination_1.y
end_date_time = datetime.now()
print  ('Trip details: ', car_id_insert, start_x_insert, start_y_insert, end_x_insert, end_y_insert, start_date_time, end_date_time)
print(end_date_time)
car_explorer.save_trip(car_id_insert, start_x_insert, start_y_insert, end_x_insert, end_y_insert, start_date_time, end_date_time)
# end of saving