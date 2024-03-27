import pygame

class Settings():   
    """A class to store all settings for Quiz app"""

    def __init__(self):
        
        # Screen settings
        screen_info = pygame.display.Info() # Get the screen info
        self.screen_width = screen_info.current_w
        self.screen_height = screen_info.current_h


        # Colors
        self.text_color = (255, 255, 255)
        self.bg_color = "#AA92E0"
        self.menu_btn_color = "#FF8201"
        self.ans_opt_btn_color = "#3db5e7"

        # Timer
        self.timer_duration = 60

