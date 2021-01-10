import pygame
import numpy as np
import time
import sys
sys.path.append("/Users/dsuveges/repositories/py_tetris/modules")

from config import Configurations
from Bag import Bag

def can_move_down(tetronimo_shape, position, base):

    # If the tetronimo reaches the bottom it cannot go furhter:
    if position[1] + tetronimo_shape.shape[1] == 20:
        return False
    else:
        return True


def merge(tetronimo_shape, position, base):
    """
    Combining the tetronimo with a base.
    """

    # looping trough tetronimo:
    for idy, row in enumerate(tetronimo_shape):
        for idx, color in enumerate(row):
            if color == '0':
                continue

            base[idy+position[0]][idx+position[1]] = color

    print(base)
    return base


pygame.init()

# Reading configurations:
brick_size = Configurations.brick_size
dimensions = (Configurations.width, Configurations.height)
tetronimos = Configurations.tetronimos
bag = Bag(list(tetronimos.keys()), Configurations.random_method)

# Genertaing screen dimensions:
screen_size = [dim * brick_size for dim in dimensions]

time_elapsed_since_last_action = 0
clock = pygame.time.Clock()

tetronimo_name = '.' #bag.pull_one()
# tetronimo_name = bag.pull_one()


# Playground matrix:
base = np.full(dimensions, "0")

playground = pygame.display.set_mode(screen_size)

# This is where the tetronimo starts:
position = [5,0]

# Format ternomio:
tetronimo_shape = np.array(tetronimos[tetronimo_name]['shape'])
tetronimo_shape = np.where(tetronimo_shape == 1, tetronimos[tetronimo_name]['color'], tetronimo_shape)

# 
while True: 
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT: 
            break
    # Cleaning screen:
    playground.fill((0, 0, 0))

    # Rotating ternomino:
    for event in events:
        if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_UP:
            #     position[1] -= 1
            if event.key == pygame.K_DOWN:
                position[1] += 1
            if (event.key == pygame.K_LEFT) & (position[0] > 0):
                position[0] -= 1
            if (event.key == pygame.K_RIGHT) & (position[0] + tetronimo_shape.shape[0] < 10):
                position[0] += 1
            if event.key == pygame.K_SPACE:
                tetronimo_shape = np.rot90(tetronimo_shape)
            if event.key == pygame.K_RETURN:
                tetronimo_name = bag.pull_one()
                tetronimo_shape = np.array(tetronimos[tetronimo_name]['shape'])
                tetronimo_shape = np.where(tetronimo_shape == 1, tetronimos[tetronimo_name]['color'], tetronimo_shape)

    # Draw tetronimo:
    for idy, row in enumerate(tetronimo_shape):
        for idx, color in enumerate(row):
            if color == '0':
                continue

            # Calculate x,y coordinate:
            x = (position[0] + idy) * brick_size
            y = (position[1] + idx) * brick_size

            # Draw rectangle:
            print( f"x:{position[0]}, y:{position[1]}. Shape: {tetronimo_shape.shape}")
            pygame.draw.rect(playground, pygame.Color(color), [x, y, brick_size, brick_size])

    # Move tetronimo down:
    dt = clock.tick() 

    # If the tetronimo cannot go further down:
    if not can_move_down(tetronimo_shape, position, base):
        base = merge(tetronimo_shape, position, base)
        print(base)
        # Init new:
        position = [5,0]
        tetronimo_name = bag.pull_one()
        tetronimo_shape = np.array(tetronimos[tetronimo_name]['shape'])
        tetronimo_shape = np.where(tetronimo_shape == 1, tetronimos[tetronimo_name]['color'], tetronimo_shape)

    # Draw base:
    for idy, row in enumerate(base):
        for idx, color in enumerate(row):
            if color == '0':
                continue

            # Calculate x,y coordinate:
            x = (position[0] + idy) * brick_size
            y = (position[1] + idx) * brick_size

            # Draw rectangle:
            print(f'color: {color}, processed color: ')
            pygame.draw.rect(playground, pygame.Color(color), [x, y, brick_size, brick_size])


    time_elapsed_since_last_action += dt
    # dt is measured in milliseconds, therefore 250 ms = 0.25 seconds
    if time_elapsed_since_last_action > 700:
        position[1] += 1
        time_elapsed_since_last_action = 0 # reset it to 0 so you can count again


    # Update screen:
    pygame.display.flip()

