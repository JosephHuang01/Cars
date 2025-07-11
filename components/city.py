from components.position import Position
from components.shape import Shape

class City(Shape):
    def __init__(self, name, x, y, map):
        self.name = name
        self.position = Position(x, y)
        self.map_grid = map
        self.width = 75
        self.length = 75

    def get_popular_cities(self):
        return [City('Seattle', 100, 100, self.map_grid),
                City('New York', 600, 100, self.map_grid),
                City('Los Angeles', 100, 400, self.map_grid),
                City('Atlanta', 500, 500, self.map_grid)]
    
    def show(self):
        self.map_grid.draw_rectangle(self.name, self.position, self.width, self.length)
        self.map_grid.draw_text_on_rectangle(self.name, self.position, self.width, self.length)
        #Shape.draw_rectangle(self.name, self.position, self.width, self.length)
        #Shape.draw_text_on_rectangle(self.name, self.position, self.width, self.length)