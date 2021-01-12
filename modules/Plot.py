import numpy as np 
import pygame
import colorsys


class MatrixPlot():

    def __init__(self, screen_size, tetromino_colors, brick_size, matrix_background_color):
        self.tetromino_colors = tetromino_colors
        self.brick_size = brick_size
        self.matrix = pygame.display.set_mode(screen_size)
        self.brick_offset = brick_size / 8
        self.matrix_background_color = matrix_background_color


    def draw_rectangle(self, color, x, y):
        rgb = pygame.Color(color)
        rgb_lighter = self.color_adjust(rgb, 0.8)
        rgb_darker = self.color_adjust(rgb, 1.2)

        # Scaling coordinates:
        x = x * self.brick_size
        y = y * self.brick_size

        # Drawing the two triangles:
        pygame.draw.polygon(self.matrix, rgb_lighter, [(x, y), (x + self.brick_size, y), (x, y + self.brick_size)])
        pygame.draw.polygon(self.matrix, rgb_darker,  [(x + self.brick_size, y), (x, y + self.brick_size), (x + self.brick_size, y + self.brick_size)])

        # rectangle dimensions:
        rect_dim = [
            x + self.brick_offset, # x coordinate shifted to the right by the offset
            y + self.brick_offset, # y coordinate shifted to the bottom by the offset 
            self.brick_size - (2 * self.brick_offset), # Scaling down the rectangle 
            self.brick_size - (2 * self.brick_offset)
        ]
        pygame.draw.rect(self.matrix, rgb, rect_dim)


    def draw_matrix(self, matrix):

        self.matrix.fill(pygame.Color(self.matrix_background_color))

        for yi, row in enumerate(matrix):
            for xi, color_code in enumerate(row):
                if color_code != 0:
                    color = self.tetromino_colors[color_code]
                    self.draw_rectangle(color, xi, yi)


    @staticmethod
    def color_adjust(color, light_factor):
        hls_code = colorsys.rgb_to_hls(color[0]/255,color[1]/255,color[2]/255)
        
        # Get the modifed rgb code:
        new_rgb = colorsys.hls_to_rgb(hls_code[0],
                                      hls_code[1]*light_factor,
                                      hls_code[2])


        return [ x * 255 for x in new_rgb ]

