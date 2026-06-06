import pygame
from py_tetris.game import tetris
from py_tetris.config import Configurations
import pygame_menu


class game_menu():

    def __init__(self):
        pass

    def show_controls():
        pass

    def start_the_game():
        pass

    def high_scores():
        pass


def main():
    pygame.init()
    display = pygame.display.set_mode(Configurations.screen_dimensions)

    tetris_obj = tetris(display)
    scoring_obj = tetris_obj.play()


if __name__ == '__main__':
    main()
