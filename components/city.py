from components.shape import Shape
from components.position import Position
from components.common_game_color import CommonGameColor

class City(Shape):
    def __init__(self, screen, pygame, name, type, position, width, length, bg_color, fg_color, map):
        super().__init__(screen, pygame, name, type, position, width, length, bg_color, fg_color)
        self.map_grid = map

    def get_popular_cities(self):
        
        return [City(self.screen, self.pygame, 'Seattle', 'city'
                    , Position(100, 100), 75, 75
                    , CommonGameColor.BLUE, CommonGameColor.RED, self.map_grid),
                City(self.screen, self.pygame, 'New York', 'city'
                     , Position(600, 100), 75, 75
                     , CommonGameColor.BLUE, CommonGameColor.RED, self.map_grid),
                City(self.screen, self.pygame, 'Los Angeles', 'city'
                     , Position(100, 400), 75, 75
                     , CommonGameColor.BLUE, CommonGameColor.RED, self.map_grid),
                City(self.screen, self.pygame, 'Atlanta', 'city'
                     , Position(500, 500), 75, 75
                     , CommonGameColor.BLUE, CommonGameColor.RED, self.map_grid)]
    
    def show(self):
        #self.draw_rectangle(self.name, self.position, self.width, self.length)
        super().show()
        self.draw_text_on_rectangle(self.name, self.position, self.width, self.length)
        #Shape.draw_rectangle(self.name, self.position, self.width, self.length)
        #Shape.draw_text_on_rectangle(self.name, self.position, self.width, self.length)