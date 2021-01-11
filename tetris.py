import pygame
import numpy as np
import time
import sys
sys.path.append("/Users/dsuveges/repositories/py_tetris/modules")

from config import Configurations
from Bag import Bag
from Matrix import Matrix
from Plot import MatrixPlot



pygame.init()

# Reading configurations:
brick_size = Configurations.brick_size
dimensions = (Configurations.height, Configurations.width)
tetronimos = Configurations.tetronimos
random_method = Configurations.random_method
tetromino_colors = Configurations.tetronimo_colors

# Initializing 
bag = Bag(tetronimos)

# Genertaing screen dimensions:
screen_size = [Configurations.width * brick_size, Configurations.height * brick_size]

# Set timing:
time_elapsed_since_last_action = 0
clock = pygame.time.Clock()

# Initilize matrix view:
m_plot = MatrixPlot(screen_size, tetromino_colors, brick_size)

# Initialize the matrix:
m = Matrix(dimensions)

# 
while True: 
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT: 
            break

    # If no tetromino is in the matrix, give one:
    if m.tetromino is None:
        m.add_tetromino(bag.pull_one())

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
                m.drop()


    # Move tetronimo down:
    dt = clock.tick() 
    time_elapsed_since_last_action += dt

    # dt is measured in milliseconds, therefore 250 ms = 0.25 seconds
    if time_elapsed_since_last_action > 700:
        m.move_down()
        m.test_for_complete_row()

        # reset it to 0 so you can count again
        time_elapsed_since_last_action = 0 


    # Update screen:
    m_plot.draw_matrix(m.get_state())
    pygame.display.flip()

