import pygame
import sys
import os

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
        else:
            self.bg_color = WHITE

        if pygame.mouse.get_pressed()[0]:
            if self.rect.collidepoint(x, y):
                self.clicked = True
                


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

# Global variables
current_question = 0
questions = []

def set_state(state):
    global current_state
    current_state = state

def load_questions():
    global questions
    questions_dir = 'assets/questions/'
    question_files = sorted(os.listdir(questions_dir))
    for file_name in question_files:
        with open(os.path.join(questions_dir, file_name), 'r') as file:
            question_data = file.readlines()
            questions.append(question_data)

def game_screen():
    global current_question
    screen.fill(GREEN)
    current_question_data = questions[current_question]
    question_text = current_question_data[0].strip()
    draw_text(question_text, BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
    options = [option.strip() for option in current_question_data[1:5]]
    option_y = SCREEN_HEIGHT // 2
    for option in options:
        draw_text(option, BLACK, SCREEN_WIDTH // 2, option_y)
        option_y += 50

    # Draw question number and score
    draw_text("Question: {}".format(current_question + 1), BLACK, SCREEN_WIDTH - 100, 20)
    draw_text("Score: {}".format(score), BLACK, 100, 20)

    # Update button
    quit_btn.update()
    quit_btn.draw(screen)

def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)


def main():
    global current_state, score
    current_state = "start"
    load_questions()
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        if current_state == "start":
            screen.fill(RED)
            start_btn.update()
            quit_btn.update()
            start_btn.draw(screen)
            quit_btn.draw(screen)
        elif current_state == "quit":
            pygame.quit()
            sys.exit()
        elif current_state == "game":
            game_screen()

        pygame.display.flip()

if __name__ == "__main__":
    main()
