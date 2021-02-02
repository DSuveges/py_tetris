import numpy as np 
import pygame
import colorsys


class MatrixPlot():

    def __init__(self, tetromino_colors, brick_size, matrix_background_color, display, offset=(0,0)):
        self.tetromino_colors = tetromino_colors
        self.brick_size = brick_size
        self.display = display # pygame.display.set_mode(screen_size)
        self.brick_offset = brick_size / 10
        self.matrix_background_color = matrix_background_color

        # Offset values are set so the items can be moved around in the screen:
        self.x_offset = offset[0]
        self.y_offset = offset[1]


    def draw_rectangle(self, color, x, y):
        rgb = pygame.Color(color)
        rgb_lighter = color_adjust(rgb, 0.8)
        rgb_darker = color_adjust(rgb, 1.2)

        # Scaling coordinates:
        x = x * self.brick_size + self.x_offset
        y = y * self.brick_size + self.y_offset

        # Drawing the two triangles:
        pygame.draw.polygon(self.display, rgb_lighter, [(x, y), (x + self.brick_size, y), (x, y + self.brick_size)])
        pygame.draw.polygon(self.display, rgb_darker,  [(x + self.brick_size, y), (x, y + self.brick_size), (x + self.brick_size, y + self.brick_size)])

        # rectangle dimensions:
        rect_dim = [
            x + self.brick_offset, # x coordinate shifted to the right by the offset
            y + self.brick_offset, # y coordinate shifted to the bottom by the offset 
            self.brick_size - (2 * self.brick_offset), # Scaling down the rectangle 
            self.brick_size - (2 * self.brick_offset)
        ]
        pygame.draw.rect(self.display, rgb, rect_dim)


    def draw_matrix(self, matrix):
        """
        Each element of the matrix is plotted, but the x,y coordinates are off-set
        """

        # Extract dimensions:
        (y,x) = matrix.shape

        # self.display.fill(pygame.Color(self.matrix_background_color))
        full_game_dim = [
            self.x_offset, # upper left corner of the matrix
            self.y_offset, # 
            self.brick_size * x, # Lower right corner of the matrix
            self.brick_size * y
        ] 

        pygame.draw.rect(self.display, self.matrix_background_color, full_game_dim)

        for yi, row in enumerate(matrix):
            for xi, color_code in enumerate(row):
                if color_code != 0:
                    color = self.tetromino_colors[color_code]
                    self.draw_rectangle(color, xi, yi)


def color_adjust(color, light_factor):
    hls_code = colorsys.rgb_to_hls(color[0]/255,color[1]/255,color[2]/255)
    
    # Get the modifed rgb code:
    new_rgb = colorsys.hls_to_rgb(hls_code[0],
                                  hls_code[1]*light_factor,
                                  hls_code[2])


    return [ x * 255 for x in new_rgb ]


class BackgroundPlot():

    def __init__(self, display, configuration):
        self.display = display
        self.configuration = configuration


    def draw_matrix_frame(self):
        """
        Drawing frame around the tetrix matrix
        """

        # Extracting matrix parameters:
        color = self.configuration.matrix_background_color
        (x,y) = self.configuration.matrix_offset
        height = (self.configuration.height - 1) * self.configuration.brick_size
        width = self.configuration.width * self.configuration.brick_size

        rgb = pygame.Color(color)
        rgb_lighter = color_adjust(rgb, 0.8)
        rgb_darker = color_adjust(rgb, 1.1)

        print(rgb_lighter)
        print(rgb_darker)

        # Scaling coordinates:
        x = x - self.configuration.brick_size / 2
        y = y - self.configuration.brick_size / 2

        triange_1 = [
            (x, y), 
            (x + width + self.configuration.brick_size, y), 
            (x, y + height + self.configuration.brick_size)
        ]

        triange_2 = [
            (x + width + self.configuration.brick_size, y), 
            (x, y + height + self.configuration.brick_size),
            (x + width + self.configuration.brick_size, y + height + self.configuration.brick_size)
        ]

        print(triange_1)
        print(triange_2)

        # Drawing the two triangles:
        pygame.draw.polygon(self.display, rgb_lighter, triange_1)
        pygame.draw.polygon(self.display, rgb_darker, triange_2)

