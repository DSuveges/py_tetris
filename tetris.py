import pygame
from modules.Tetris import tetris
from modules.config import Configurations


def main():
    # Genertaing the display:
    pygame.init()
    display = pygame.display.set_mode(Configurations.screen_dimensions)

    tetris_obj = tetris(display)


if __name__ == '__main__':
    main()

