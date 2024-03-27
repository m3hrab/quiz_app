import pygame
import sys

# Load the pages (classes)
from assets.scripts.start_menu import StartMenu
from assets.scripts.game import Quiz
from assets.scripts.game_over import GameOver

# Load the settings class that have all the settings of the Quiz app
from assets.scripts.settings import Settings


def run_game():
    # Initialize the game
    pygame.init()
    pygame.mixer.init()

    # Load the settings
    settings = Settings()

    # Set the screen 
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("MOD Quiz")


    # Create instances of all pages
    start_menu = StartMenu(screen, settings)
    quiz = Quiz(screen, settings)
    game_over = GameOver(screen, settings)

    # Set the current page to the start menu
    current_page = start_menu


    # Main loop
    while True:

        # Check for events
        events = pygame.event.get()

        # Call current page's event handler
        flag = current_page.handle_events(events)

        if flag == "quit":
            pygame.quit()
            sys.exit()

        elif flag == "start":
            current_page = start_menu
        elif flag == "quiz":
            current_page = quiz
        elif flag == "game_over":
            game_over.score = quiz.save_score 
            current_page = game_over

        # Render the current page
        current_page.render()

        # Update the display
        pygame.display.flip()


if __name__ == "__main__":
    run_game()


