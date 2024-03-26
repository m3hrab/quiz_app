import pygame 

class Button():

    def __init__(self, text, pos, size, bg_color = (255, 255, 255), hover_color = (255, 255, 255), text_color = (0, 0, 0)):

        self.btn_color = bg_color
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.text_color = text_color

        # text position centered on the button
        self.rect = pygame.Rect(pos, size)
        self.text = pygame.font.Font('assets/fonts/Helvetica.otf', 28).render(text, True, self.text_color)
        self.text_rect = self.text.get_rect(center=self.rect.center)

    def update(self, pos):
        if self.rect.collidepoint(pos):
            self.btn_color = self.hover_color
        else:
            self.btn_color = self.bg_color 


    def draw(self, screen):
        pygame.draw.rect(screen, self.btn_color, self.rect)
        screen.blit(self.text, self.text_rect)
        