import pygame
import sys

pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class Button():
    
    def __init__(self, text, pos, size, function, *args):
        self.fun = function
        self.clicked = False    
        self.got_clicked = False
        self.args = args
        self.size = size
        self.screen = pygame.display.get_surface()
        self.bg_color = WHITE

        self.rect = pygame.Rect(pos, size)

        # text position centered on the button
        self.text = pygame.font.Font(None, 32).render(text, False, BLACK)
        self.text_rect = self.text.get_rect(center=self.rect.center)

    def update(self):
        self.clicked = False
        x, y = pygame.mouse.get_pos()
        if self.rect.collidepoint(x, y):
            self.bg_color = BLUE
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
        else:
            self.bg_color = WHITE

        if self.clicked:
            self.fun(*self.args)
            self.clicked = False
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.bg_color, self.rect)
        screen.blit(self.text, self.text_rect)


screen_info = pygame.display.Info()
SCREEN_WIDTH = screen_info.current_w
SCREEN_HEIGHT = screen_info.current_h
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("MOD Quiz")



def set_state(state):
    global current_state
    current_state = state

# Buttons 
start_btn = Button("Press to Start", ((SCREEN_WIDTH - 300) // 2, SCREEN_HEIGHT//2), (300, 50), set_state, "game")
quit_btn = Button("Press to Quit", ((SCREEN_WIDTH - 300) // 2, SCREEN_HEIGHT//2 + 70), (300, 50), set_state, "quit")
                  
def start_scrren():
    screen.fill(RED)
    # Check for button click 
    start_btn.update()
    quit_btn.update()
    # Draw buttons
    start_btn.draw(screen)
    quit_btn.draw(screen)


def main():
    global current_state
    current_state = "start"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        if current_state == "start":
            start_scrren()
        elif current_state == "quit":
            pygame.quit()
            sys.exit()
        elif current_state == "game":
            pass

        pygame.display.flip()


if __name__ == "__main__":
    main()
