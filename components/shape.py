from components.position import Position

class Shape():
    def __init__(self, screen, pygame, name, type, position, width, length, bg_color, fg_color):
        self.screen = screen
        self.pygame = pygame
        self.name = name
        self.type = type
        self.position = position
        self.width = width
        self.length = length
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.font = pygame.font.SysFont(None, 18)
        self.screen_size = self.screen.get_size()           
   
    def center_position(self):
        screen_width, screen_height = self.screen_size
        screen_x = (screen_width - self.width)/2
        screen_y = (screen_height - self.length)/2
        self.position = Position(screen_x, screen_y)

    def draw_rectangle(self, name, position, width, height):
        rect_img = self.pygame.Rect(position.x, position.y, width, height)
        #color = (255, 255, 255)
        self.pygame.draw.rect(self.screen, self.bg_color, rect_img)
        #self.screen.blit(self.screen, self.screen.get_rect())
    
    def draw_text_on_rectangle(self, text, position, width, height):
        text_surface = self.font.render(text, True, self.fg_color)
        text_rect = text_surface.get_rect(center=(position.x + width/2, position.y + height/2))
        self.screen.blit(text_surface, text_rect)
    
    def show(self):
        self.draw_rectangle(self.name, self.position, self.width, self.length)
        #self.draw_text_on_rectangle(self.name, self.position, self.width, self.length)
        self.screen.blit(self.screen, self.screen.get_rect())