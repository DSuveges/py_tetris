## This file contains all the configurations for Tetris


class Configurations():

    # screen parameters:
    screen_dimensions = [600, 800]

    # Dimension of the play fields:
    matrix_dimensions = [10, 20]

    # Offsets of fields:
    matrix_offset = (65,140)

    # Pixel size of one brick:
    brick_size = 30

    # Color mappings:
    tetromino_colors = {
        1: 'white',
        2: 'darkorange',
        3: 'gold1',
        4: 'firebrick2',
        5: 'chartreuse3',
        6: 'lightskyblue',
        7: 'turquoise2',
        8: 'plum2'
    }

    #  color definitions for other elements:
    matrix_background_color = 'ivory1'
    display_color = 'cornsilk4'
    frame_color = 'lightsteelblue'
    panel_label_color = 'darkslategray'
    panel_text_color = 'lightskyblue4'

    # Frame with as fraction of a brick:
    frame_fraction = 0.25

    # Tetromino definitions:
    tetronimos = {
        'L': {'shape': [[0,0,0],[2,2,2],[2,0,0]]},
        'O': {'shape': [[3,3],[3,3]]},
        'Z': {'shape': [[0,0,0],[4,4,0],[0,4,4]]},
        'S': {'shape': [[0,0,0],[0,5,5],[5,5,0]]},
        'J': {'shape': [[0,0,0],[6,6,6],[0,0,6]]},
        'I': {'shape': [[0,0,0,0],[0,0,0,0],[7,7,7,7],[0,0,0,0]]},
        'T': {'shape': [[0,0,0],[8,8,8],[0,8,0]]},
    }

    # Tetromino randomization:
    random_method = 'double_bag' # random permutation of group of two sets of tetrominoes are generated
    random_seed = None # Tells if the random seed is set.

    # Score is given for cleared lines and cells being dropped:
    scoring= {
        'multiplier': {
            1: 40,
            2: 100,
            3: 300,
            4: 1200
        },
        'soft_drop_score': 1,
        'hard_drop_score': 2,
    }

    # Speed definitions:

    ##
    ## Panel dimensions
    ##

    player = {
        'offset': [385,140],
        'size': [150,50],
    }

    # Panel showing the next element:
    next_element = {
        'offset': [385,240],
        'size': [150,150],
        'label': 'Next'
    }

    # Panel showing the score
    score = {
        'offset': [385,440],
        'size': [150,50],
        'label': 'Score'
    }

    # Panel showing level:
    level = {
        'offset': [385,540],
        'size': [150,50],
        'label': 'Level'
    }

    # PAnel showing rows cleared:
    rows = {
        'offset': [385,640],
        'size': [150,50],
        'label': 'Rows'
    }


