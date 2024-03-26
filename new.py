import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame State Management")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.SysFont(None, 40)

# Define different game states
START_MENU = 0
GAME_MENU = 1
LAST_SCREEN = 2

# Button class
class Button:
    def __init__(self, x, y, width, height, text, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def clicked(self):
        if self.action:
            self.action()

# Function to start the game
def start_game():
    global current_state
    current_state = GAME_MENU

# Function to go back to the start menu
def back_to_start_menu():
    global current_state
    current_state = START_MENU

# Function to go to the last screen
def go_to_last_screen():
    global current_state
    current_state = LAST_SCREEN

# Initialize buttons for each screen
start_button = Button(300, 250, 200, 50, "Start Game", start_game)
next_button = Button(300, 250, 200, 50, "Next Page", go_to_last_screen)
back_button = Button(300, 250, 200, 50, "Back to Start Menu", back_to_start_menu)

# Game loop
current_state = START_MENU
running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if current_state == START_MENU:
                start_button.clicked()
            elif current_state == GAME_MENU:
                next_button.clicked()
            elif current_state == LAST_SCREEN:
                back_button.clicked()

    # Draw buttons based on current state
    if current_state == START_MENU:
        screen.fill(WHITE)
        start_button.draw()
    elif current_state == GAME_MENU:
        screen.fill(WHITE)
        next_button.draw()
    elif current_state == LAST_SCREEN:
        screen.fill(WHITE)
        back_button.draw()

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
