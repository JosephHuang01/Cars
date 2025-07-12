from components.city import City
from components.shape import Shape

class Map(Shape):
    def __init__(self, screen, pygame, name, type, position, width, length, bg_color, fg_color):
        super().__init__(screen, pygame, name, type, position, width, length, bg_color, fg_color)

        self.grid_size = 8
        self.margin = 10
        self.cell_size = 75.74
        self.screen = screen

        total_width = self.grid_size * self.cell_size + (self.grid_size - 1) * self.margin
        total_height = self.grid_size * self.cell_size + (self.grid_size - 1) * self.margin
        self.surface = pygame.Surface((total_width, total_height))

        self.font = pygame.font.SysFont(None, 18)
        self.offset_x = 50
        self.offset_y = 50
        self.rect = self.surface.get_rect(topleft = (self.offset_x, self.offset_y))
        self.cityReference = City(screen, pygame, name, type, position, 75, 75, bg_color, fg_color, map)
        self.cities = []
    
    def add_city(self, city):
        self.cities.append(city)

    def show_cities(self):
        for city in self.cities:
            city.show()
            #Shape.show(self)
    
    # def center_position(self):
    #     pass

    # def draw_rectangle(self, name, position, width, height):
    #     pygame.draw.rect(self.surface, (0, 128, 0), (position.x, position.y, width, height))

    # def draw_text_on_rectangle(self, text, position, width, height):
    #     text_surface = self.font.render(text, True, (0, 0, 0))
    #     text_rect = text_surface.get_rect(center=(position.x + width/2, position.y + height/2))
    #     self.surface.blit(text_surface, text_rect)
    #     #self.screen.blit(text_surface, text_rect)

    # def show(self):
    #     self.screen.blit(self.surface, self.rect)