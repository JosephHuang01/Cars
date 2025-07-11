class Shape():
    def __init__(self, screen, pygame, name, type, position, width, length):
        self.screen = screen
        self.pygame = pygame
        self.name = name
        self.type = type
        self.position = position
        self.width = width
        self.length = length
        self.font = pygame.font.SysFont(None, 18)
    
    def draw_rectangle(self, name, position, width, height):
        rect_img = self.pygame.Rect(position.x, position.y, width, height)
        color = (255, 255, 255)
        self.pygame.draw.rect(self.screen, color, rect_img)
        #self.screen.blit(self.screen, self.screen.get_rect())
    
    def draw_text_on_rectangle(self, text, position, width, height):
        text_surface = self.font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(position.x + width/2, position.y + height/2))
        self.screen.blit(text_surface, text_rect)
    
    def show(self):
        self.screen.blit(self.screen, self.screen.get_rect())