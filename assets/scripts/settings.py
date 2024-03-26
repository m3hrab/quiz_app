import pygame

class Settings():   
    """A class to store all settings for Quiz app"""

    def __init__(self):
        
        # Screen settings
        screen_info = pygame.display.Info() # Get the screen info
        self.screen_width = screen_info.current_w
        self.screen_height = screen_info.current_h


        # Colors
        self.bg_color = "#AA92E0"
        self.menu_btn_color = "#FF8201"
        self.menu_btn_hover_color = (0, 0, 200)

