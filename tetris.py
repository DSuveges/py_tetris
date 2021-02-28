import pygame
import numpy as np
import time
import sys
sys.path.append("/Users/dsuveges/repositories/py_tetris/modules")

from config import Configurations
from Bag import Bag
from Matrix import Matrix
from Plot import MatrixPlot, BackgroundPlot, NextElementPlot, LabelsPlot
from Scoring import Score



pygame.init()

# Reading configurations:
brick_size = Configurations.brick_size
dimensions = (Configurations.height, Configurations.width)
tetronimos = Configurations.tetronimos
random_method = Configurations.random_method
random_seed = Configurations.random_seed
tetromino_colors = Configurations.tetromino_colors
matrix_background_color = Configurations.matrix_background_color
matrix_offset = Configurations.matrix_offset

# Initializing 
bag = Bag(tetronimos,random_method=random_method, seed=random_seed)

# Genertaing the display:
screen_size = Configurations.screen_dimensions
display = pygame.display.set_mode(screen_size)
display.fill(Configurations.display_color)
bg = BackgroundPlot(display, Configurations)
show_next = NextElementPlot(tetromino_colors, brick_size, matrix_background_color, display, Configurations.next_element)
labels = LabelsPlot(display, Configurations)

# Set timing:
time_elapsed_since_last_action = 0
clock = pygame.time.Clock()

# Initilize matrix view:
m_plot = MatrixPlot(tetromino_colors, brick_size, matrix_background_color, display, matrix_offset)

# Initialize the matrix:
m = Matrix(dimensions)

# Initialzing score object
scoring = Score(Configurations.scoring, level=1)

# Filling panels:
labels.update_player('Player 1')
labels.update_score(scoring.get_score())
labels.update_level(scoring.get_level())
labels.update_rows(scoring.get_rows())


# 
while True: 
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT: 
            break

    # If no tetromino is in the matrix, give one:
    if m.tetromino is None:
        m.add_tetromino(bag.pull_one())
        show_next.draw_next(bag.show_next())

    # Rotating and moving the tetromino:
    for event in events:
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_DOWN:
                m.move_down()
            if event.key == pygame.K_LEFT:
                m.move_left()
            if event.key == pygame.K_RIGHT:
                m.move_right()
            if event.key == pygame.K_a:
                m.rotate_left()
            if event.key == pygame.K_d:
                m.rotate_right()
            if event.key == pygame.K_SPACE:
                scoring.add_hard_drop_score(m.drop())


    # Move tetronimo down:
    dt = clock.tick() 
    time_elapsed_since_last_action += dt

    # dt is measured in milliseconds, therefore 250 ms = 0.25 seconds
    if time_elapsed_since_last_action > 700:
        down_ret = m.move_down()
        if down_ret == 'game over':
            break

        # reset it to 0 so you can count again
        time_elapsed_since_last_action = 0 

    # After every tick, we check for completed rows and update:
    completed_rows = m.test_for_complete_row()

    if completed_rows > 0:
        scoring.rows_cleared(completed_rows)
        labels.update_score(scoring.get_score())
        labels.update_level(scoring.get_level())
        labels.update_rows(scoring.get_rows())
    

    # Update screen:
    m_plot.draw_matrix(m.get_state())
    pygame.display.flip()



    # If we exit from the loop, it means the game is over:
    # pygame.draw.rect(self.display, self.frame_color, rect)
    my_image = pygame.Surface(screen_size, pygame.SRCALPHA)
    BLUE = (0, 0, 255, 255)
    pygame.draw.rect(my_image, BLUE, my_image.get_rect())


