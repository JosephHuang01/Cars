import pygame
from components.city import City

class Map():
    def __init__(self, screen):
        self.grid_size = 8
        self.margin = 10
        self.cell_size = 75.74
        self.screen = screen

        total_width = self.grid_size * self.cell_size + (self.grid_size - 1) * self.margin
        total_height = self.grid_size * self.cell_size + (self.grid_size - 1) * self.margin
        self.surface = pygame.Surface((total_width, total_height))

        self.font = pygame.font.SysFont(None, 24)
        self.offset_x = 50
        self.offset_y = 50
        self.rect = self.surface.get_rect(topleft = (self.offset_x, self.offset_y))
        self.cityReference = City('', 0, 0, map)
        self.cities = []
    
    def add_city(self, city):
        self.cities.append(city)

    def show_cities(self):
        for city in self.cities:
            city.show()

    def draw_rectangle(self, name, position, width, height):
        pygame.draw.rect(self.surface, (0, 128, 0), (position.x, position.y, width, height))

    def draw_text_on_rectangle(self, text, position, width, height):
        text_surface = self.font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(position.x + self.cell_size/2, position.y + self.cell_size/2))
        self.surface.blit(text_surface, text_rect)

    def blit(self):
        self.screen.blit(self.surface, self.rect)