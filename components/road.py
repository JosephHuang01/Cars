from components.shape import Shape, ShapeSpecification

class Road(Shape):
    def __init__(self, screen, pygame, shape_spec):
        super().__init__(screen, pygame, shape_spec)
    
    def get_roads(self):
        return [Road(self.screen, self.pygame, ShapeSpecification())]
    
    def show(self):
        super().show()
        self.draw_text_on_rectangle(self.name, self.position, self.width, self.length)