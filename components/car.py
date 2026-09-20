from components.shape import Shape

class Car(Shape):
    def __init__(self, screen, pygame, shape_spec):
        super().__init__(screen, pygame, shape_spec)

    def drive(self, position):
        self.position = position

    def show(self):
        super().show()
        self.draw_text_on_rectangle(self.name, self.position, self.width, self.length)
        car_surface = self.pygame.Surface((self.width, self.length), self.pygame.SRCALPHA)
        car_surface.fill(self.bg_color)