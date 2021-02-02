import pygame
import numpy as np
import time
import sys
sys.path.append("/Users/dsuveges/repositories/py_tetris/modules")

from config import Configurations
from Bag import Bag
from Matrix import Matrix
from Plot import MatrixPlot, BackgroundPlot, NextElementPlot
from Scoring import Score



pygame.init()

# Reading configurations:
brick_size = Configurations.brick_size
dimensions = (Configurations.height, Configurations.width)
tetronimos = Configurations.tetronimos
random_method = Configurations.random_method
random_seed = Configurations.random_seed
tetromino_colors = Configurations.tetronimo_colors
matrix_background_color = Configurations.matrix_background_color
matrix_offset = Configurations.matrix_offset
next_element_offset = Configurations.next_element_offset
next_element_size = Configurations.next_element_size

# Initializing 
bag = Bag(tetronimos,random_method=random_method, seed=random_seed)

# Genertaing the display:
screen_size = Configurations.screen_dimensions
display = pygame.display.set_mode(screen_size)
display.fill(Configurations.display_color)
bg = BackgroundPlot(display, Configurations)
bg.draw_matrix_frame()
bg.draw_next_element_frame()
show_next = NextElementPlot(tetromino_colors, brick_size, matrix_background_color, display, next_element_size, next_element_offset)


# Set timing:
time_elapsed_since_last_action = 0
clock = pygame.time.Clock()

# Initilize matrix view:
m_plot = MatrixPlot(tetromino_colors, brick_size, matrix_background_color, display, matrix_offset)

# Initialize the matrix:
m = Matrix(dimensions)

# Initialzing score object
scoring = Score(Configurations.scoring, level=1)


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
        m.move_down()

        # reset it to 0 so you can count again
        time_elapsed_since_last_action = 0 

    # After every tick, we check for completed rows and update:
    completed_rows = m.test_for_complete_row()
    scoring.rows_cleared(completed_rows)

    print(f'score: {scoring.get_score()}, level: {scoring.get_level()}, rows cleared: {scoring.get_lines()}\r')


    # Update screen:
    m_plot.draw_matrix(m.get_state())
    pygame.display.flip()

