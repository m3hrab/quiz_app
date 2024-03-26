import pygame

from assets.scripts.button import Button

class StartMenu():

    def __init__(self, screen, settings) -> None:
        self.screen = screen
        self.settings = settings
        
        self.buttons = []

        btn_size = (450, 100)
        quit_btn_pos = ((settings.screen_width - btn_size[0]) // 2, (settings.screen_height - btn_size[1]) // 2 - 80)
        start_btn_pos = ((settings.screen_width - btn_size[0]) // 2, (settings.screen_height - btn_size[1]) // 2 + 40)

        self.start_btn = Button("Press to Start", start_btn_pos, btn_size, settings.menu_btn_color)
        self.quit_btn = Button("Press to Exit", quit_btn_pos, btn_size, settings.menu_btn_color)

        self.buttons.append(self.start_btn)
        self.buttons.append(self.quit_btn)

    def handle_events(self, events):

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                if self.start_btn.rect.collidepoint(pygame.mouse.get_pos()):
                    return "quiz"
                elif self.quit_btn.rect.collidepoint(pygame.mouse.get_pos()):
                    return "quit"
    
    def render(self):
        self.screen.fill(self.settings.bg_color)
        for button in self.buttons:
            button.update(pygame.mouse.get_pos())
            button.draw(self.screen)
        