import numpy as np 
import pygame
import colorsys
from modules.config import Configurations 


def color_adjust(color, light_factor):
    hls_code = colorsys.rgb_to_hls(color[0]/255,color[1]/255,color[2]/255)
    
    # Get the modifed rgb code:
    new_rgb = colorsys.hls_to_rgb(hls_code[0],
                                  hls_code[1]*light_factor,
                                  hls_code[2])


    return [ x * 255 for x in new_rgb ]


class MatrixPlot(Configurations):

    def __init__(self, display):

        self.display = display
        self.brick_offset = self.brick_size / 10

        # Offset values are set so the items can be moved around in the screen:
        (self.x_offset, self.y_offset) = self.matrix_offset


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


class NextElementPlot(Configurations):
    """
    This class draws the next tetromino in the next panel
    """

    def __init__(self, display):

        self.display = display 
        self.brick_offset = self.brick_size / 10

        # Offset values are set so the items can be moved around in the screen:
        self.offset = self.next_element['offset']
        self.dimensions = self.next_element['size']

        # Clearing the background
        self.clear()


    def clear(self):
        """
        Clearing up the panel
        """

        pygame.draw.rect(self.display, self.matrix_background_color, self.offset + self.dimensions)


    def draw_next(self, tetromino):

        # Clearing box:
        self.clear()

        # Get shape of the tetromino:
        tetromino_dim = len(tetromino)

        # Get tetromino_offset:
        tetr_offset_x = self.offset[0] + (5 - tetromino_dim) / 2 * self.brick_size
        tetr_offset_y = self.offset[1] + (5 - tetromino_dim) / 2 * self.brick_size


        for yi, row in enumerate(tetromino):
            for xi, color_code in enumerate(row):
                if color_code != 0:
                    # Calculate actual values:
                    color = self.tetromino_colors[color_code]
                    x = xi * self.brick_size + tetr_offset_x
                    y = yi * self.brick_size + tetr_offset_y

                    # Draw square
                    self.draw_rectangle(color, x, y)


    def draw_rectangle(self, color, x, y):
        rgb = pygame.Color(color)
        rgb_lighter = color_adjust(rgb, 0.8)
        rgb_darker = color_adjust(rgb, 1.2)

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


class LabelsPlot(Configurations):

    def __init__(self, display):

        self.display = display

        # Initialize label:
        self.panel_font = pygame.font.SysFont('novamono', 40)


    def write_text(self, dimensions, label):

        # Clearing background:
        pygame.draw.rect(self.display, self.matrix_background_color, dimensions['offset'] + dimensions['size'])

        # Calculate text:
        label = self.panel_font.render(label, True, self.panel_text_color)
        x_center_offset = (dimensions['size'][0] - label.get_rect().width) / 2

        self.display.blit(label, (dimensions['offset'][0] + x_center_offset, dimensions['offset'][1] + 10))


    def update_score(self, score):

        score = str(score).zfill(7)

        dimensions = self.score
        self.write_text(dimensions,score)


    def update_level(self, level):
        dimensions = self.level
        self.write_text(dimensions,str(level))


    def update_rows(self, rows):
        dimensions = self.rows
        self.write_text(dimensions,str(rows))


    def update_player(self, player):
        dimensions = self.player
        self.write_text(dimensions,player)


class BackgroundPlot(Configurations):
    """
    This class draws the game layout except the game matrix
    * player name
    * nextelement
    * score
    * level
    * cleared rows
    """

    def __init__(self, display):
        self.display = display

        # Extracting important values:
        self.frame_width = self.frame_fraction * self.brick_size

        # Initialize labels:
        self.panel_font = pygame.font.SysFont('novamono', 35)

        # Store panel positions and sizes:
        self.draw_panel({
            'offset': self.matrix_offset, 
            'size': [
                self.brick_size * self.matrix_dimensions[0], 
                self.brick_size * (self.matrix_dimensions[1])
            ]
        })
        print('updated')
        self.draw_panel(self.player)
        self.draw_panel(self.next_element)
        self.draw_panel(self.score)
        self.draw_panel(self.level)
        self.draw_panel(self.rows)



    def draw_panel(self,data):
        """
        Daws the panel with frame + adds label
        """
        
        # Calaculating background:
        rect_fg = [
            data['offset'][0],
            data['offset'][1],
            data['size'][0],
            data['size'][1],
        ]

        # Calaculating background:
        rect_bg = [
            data['offset'][0] - self.frame_width,
            data['offset'][1] - self.frame_width,
            data['size'][0] + 2 * self.frame_width,
            data['size'][1] + 2 * self.frame_width,
        ]

        if 'label' in data:
            rect_bg[1] -= 25
            rect_bg[3] += 25


        # Drawing background and foreground rectangle:
        pygame.draw.rect(self.display, self.frame_color, rect_bg)
        pygame.draw.rect(self.display, self.matrix_background_color, rect_fg)

        # Adding text if present:
        if 'label' in data:
            
            # Calculate text:
            label = self.panel_font.render(data['label'], True, self.panel_label_color)
            x_center_offset = (data['size'][0] - label.get_rect().width) / 2


            self.display.blit(label, (rect_bg[0] + x_center_offset, rect_bg[1] + 5))






