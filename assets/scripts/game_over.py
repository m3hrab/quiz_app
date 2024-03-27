import pygame

from assets.scripts.button import Button

class GameOver():

    def __init__(self, screen, settings) -> None:
        self.screen = screen
        self.settings = settings
        self.screen_rect = screen.get_rect()
        self.score = 0
        
        self.message = "Thank you for playing!"
        self.message_font = pygame.font.Font("assets/fonts/Helvetica.otf", 36)
        message_pos = (self.screen_rect.centerx, self.screen_rect.top + 100)
        self.message_rect = self.message_font.render(self.message, True, self.settings.text_color).get_rect(center=message_pos)
        
        self.score_message = "Your score: "
        self.score_message_font = pygame.font.Font("assets/fonts/Helvetica.otf", 30)
        score_message_pos = (self.screen_rect.centerx, self.screen_rect.top + 200)
        self.score_message_rect = self.score_message_font.render(self.score_message, True, self.settings.text_color).get_rect(center=score_message_pos)

        btn_size = (400, 100)
        btn_pos = (self.screen_rect.centerx - btn_size[0]//2, self.screen_rect.top + 400)
        self.start_btn = Button("Main Menu", btn_pos, btn_size, settings.menu_btn_color)

    def handle_events(self, events):

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:

                if self.start_btn.rect.collidepoint(pygame.mouse.get_pos()):
                    return "start" 
                   
            
    def render(self):
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.message_font.render(self.message, True, self.settings.text_color), self.message_rect)
        self.screen.blit(self.score_message_font.render(self.score_message + str(self.score), True, self.settings.text_color), self.score_message_rect)
        self.start_btn.update(pygame.mouse.get_pos())
        self.start_btn.draw(self.screen)
        