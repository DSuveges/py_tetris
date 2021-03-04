import pygame
from modules.Tetris import tetris
from modules.config import Configurations
import pygame_menu



class game_menu():

    def __init__(self):
        pass

    def show_controls():
        # Do the job here !
        pass

    def start_the_game():
        # Do the job here !
        pass

    def high_scores():
        # Do the job here !
        pass

    def start_the_game():
        # Do the job here !
        pass


def main():
    # Genertaing the display:
    pygame.init()
    display = pygame.display.set_mode(Configurations.screen_dimensions)

    tetris_obj = tetris(display)
    scoring_obj = tetris_obj.play()


if __name__ == '__main__':
    main()

