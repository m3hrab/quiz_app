import pygame
import random

class Quiz():
    """A class to store all the functionalities of the quiz page"""
    def __init__(self, screen, settings) -> None:
        self.screen = screen
        self.settings = settings

        self.questions = []

        self.questions.append(["What does MOD stand for?",
                            ["Ministry of drive", " Ministry of defence", "Mission of Device", "Mission of ministry"],
                            1, 'MOD.jpg'])    
        
        self.questions.append(["What country has the biggest population?",
                              ["India", "China", "Indonesia", "United states of America"],
                            1, "indiaChina.jpg"])

        # Add other questions...

        # shuffle the questions
        random.shuffle(self.questions)

        self.current_question_index = 0
        self.score = 0
        self.asked_questions = set()  # Track which questions have been asked

        self.question_rect = pygame.Rect(0, 0, 400, 200)
        self.question_rect.centerx = self.screen.get_rect().centerx
        self.question_rect.y = 50
        self.font = pygame.font.Font('assets/fonts/Helvetica.otf', 28)

        self.option_font = pygame.font.Font('assets/fonts/Helvetica.otf', 24)
        self.option_buttons = []  # Store the Rects for option buttons

        option_size = (450, 100)
        screen_rect = screen.get_rect()
        # Define positions for answer option buttons
        option_positions = [(screen_rect.centerx - option_size[0] - 10, screen_rect.bottom - option_size[1]*3 - 20),
                            (screen_rect.centerx + 10, screen_rect.bottom - option_size[1]*3 - 20),
                            (screen_rect.centerx - option_size[0] - 10, screen_rect.bottom - option_size[1]*2), 
                            (screen_rect.centerx + 10, screen_rect.bottom - option_size[1]*2)]

        # Create Rects for each answer option button
        for pos in option_positions:
            button_rect = pygame.Rect(pos[0], pos[1], option_size[0], option_size[1])
            self.option_buttons.append(button_rect)

        
        # Timer attributes
        self.clock = pygame.time.Clock()
        self.timer_event = pygame.USEREVENT+1 # Custom event for the timer
        pygame.time.set_timer(self.timer_event, 1000) 
        self.timer_paused = False
        self.time_left = 60
        


    def reset(self):
        self.score = 0
        self.asked_questions.clear()
        self.current_question_index = 0
        self.time_left = 60
        self.timer_paused = False
        random.shuffle(self.questions)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                return "quit"

                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check for button click
                mouse_pos = pygame.mouse.get_pos()
                for index, button_rect in enumerate(self.option_buttons):
                    if button_rect.collidepoint(mouse_pos):
                        self.check_answer(index)
                        if len(self.asked_questions) == len(self.questions) - 1:  # Check if all questions have been asked
                            self.reset()
                            return "game_over"
                        self.next_question()

            else:
                if event.type == self.timer_event and not self.timer_paused:
                    self.time_left -= 1
                    if self.time_left == 0:
                        self.reset()
                        return "game_over"

    def check_answer(self, selected_option_index):
        current_question = self.questions[self.current_question_index]
        correct_option_index = current_question[2]
        if selected_option_index == correct_option_index:
            self.score += 1

    def next_question(self):
        self.asked_questions.add(self.current_question_index)  # Add current question index to asked questions
        # Find the next unanswered question
        for i in range(len(self.questions)):
            if i not in self.asked_questions:
                self.current_question_index = i
                break

    def render(self):
        self.screen.fill(self.settings.bg_color)
        current_question = self.questions[self.current_question_index]
        question_text = current_question[0]
        options = current_question[1]

        question_surface = self.font.render(question_text, True, (0, 0, 0))
        question_rect = question_surface.get_rect(center=(self.screen.get_width() // 2, 50))
        self.screen.blit(question_surface, question_rect)

        # Render answer options as buttons
        for index, option_text in enumerate(options):
            option_surface = self.option_font.render(option_text, True, (0, 0, 0))
            option_rect = option_surface.get_rect(center=self.option_buttons[index].center)
            
            # Check if the mouse is hovering over the button
            if self.option_buttons[index].collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.screen, (200, 200, 200), self.option_buttons[index])  # Change color when hovering
            else:
                pygame.draw.rect(self.screen, self.settings.ans_opt_btn_color, self.option_buttons[index])
            
            self.screen.blit(option_surface, option_rect)

        # Render score
        score_surface = self.font.render(f"Score: {self.score}", True, (0, 0, 0))
        score_rect = score_surface.get_rect(topright=(self.screen.get_width() - 20, 20))
        self.screen.blit(score_surface, score_rect)

        # Render question number
        question_num_surface = self.font.render(f"Question {self.current_question_index + 1}/{len(self.questions)}", True, (0, 0, 0))
        question_num_rect = question_num_surface.get_rect(topright=(self.screen.get_width() - 20, 60))
        self.screen.blit(question_num_surface, question_num_rect)

        # Render image
        image = pygame.image.load(f'assets/images/{current_question[3]}')
        image = pygame.transform.scale(image, (620, 320))
        image_rect = image.get_rect(center=(self.screen.get_width() // 2, 250))
        self.screen.blit(image, image_rect)


        # Render timer
        timer_surface = self.font.render(f"Time left: {self.time_left}", True, (0, 0, 0))
        timer_rect = timer_surface.get_rect(topleft=(20, 20))
        self.screen.blit(timer_surface, timer_rect)

        pygame.display.flip()
