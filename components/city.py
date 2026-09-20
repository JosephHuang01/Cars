from components.shape import Shape

class City(Shape):
    def __init__(self, screen, pygame, shape_spec):
        super().__init__(screen, pygame, shape_spec)
        self.map_grid = map
    
    def show(self):
        super().show()
        self.draw_text_on_rectangle(self.name, self.position, self.width, self.length)