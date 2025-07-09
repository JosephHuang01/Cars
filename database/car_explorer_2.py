import pygame
import pyodbc
from components.car import Car, Position
from components.map import Map

class CarModel():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.grid = Map()
    
        self.image = pygame.Surface((20, 8))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        #self.rect.bottom = self.screen_rect.bottom

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.direction = 'RIGHT'

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.conn = self.__get_connection()
    
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            #self.rect.centerx += 1
            self.centerx += self.ai_settings.car_explorer_speed_factor
            self.direction = 'RIGHT'
            self.moving_right = False
        if self.moving_left and self.rect.left > 0:
            #self.rect.centerx -= 1
            self.centerx -= self.ai_settings.car_explorer_speed_factor
            self.direction = 'LEFT'
            self.moving_left = False
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.car_explorer_speed_factor
            self.direction = 'UP'
            self.moving_up = False
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.car_explorer_speed_factor
            self.direction = 'DOWN'
            self.moving_down = False
        
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
    
    def blitme(self):
        #self.screen.blit(self.image, self.rect)
        if self.direction == 'RIGHT':
            angle = 0
        elif self.direction == 'LEFT':
            angle = 180
        elif self.direction == 'UP':
            angle = 90
        elif self.direction == 'DOWN':
            angle = 270
        
        rotated_car = pygame.transform.rotate(self.image, angle)
        rotated_rect = rotated_car.get_rect(center=self.rect.center)
        self.screen.blit(rotated_car, rotated_rect.topleft)
    
    def __get_connection(self):
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=localhost;'
            'DATABASE=CarExplorer;'
            'Trusted_Connection=yes;'
        )
        return conn
    
    def get_one_car(self):
        cursor = self.conn.cursor()
        cursor.execute("select top 5 * from game.Cars")

        first_row = cursor.fetchone()
        if first_row:
            car_id = first_row.CarId
            car_make = first_row.Make
            car_model = first_row.Model
            car_year = first_row.Year

        car_a = Car(car_make, car_model, car_year)
        car_a.car_id = car_id
        return car_a
    
    def get_last_trip_position(self, car_id):
        cursor = self.conn.cursor()        
        cursor.execute("select * from game.Trips where CarID = ? ORDER BY EndDateTime DESC", car_id)
        row_one = cursor.fetchone()
        
        if row_one:
            trip_id = row_one.TripId
            start_x = row_one.StartX
            start_y = row_one.StartY
            end_x = row_one.EndX
            end_y = row_one.EndY
            start_date_time = row_one.StartDateTime
            end_date_time = row_one.EndDateTime

        return Position(end_x, end_y)