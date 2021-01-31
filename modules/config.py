## This file contains all the configurations for Tetris


class Configurations():

    # Dimension of the field:
    width = 10
    height = 21 # The top row is hidden.

    # Pixel size of one brick:
    brick_size = 30

    # Color mappings:
    tetronimo_colors = {
        1: 'white',
        2: 'darkorange',
        3: 'lightgoldenrod1',
        4: 'firebrick',
        5: 'olivedrab1',
        6: 'lightskyblue',
        7: 'cyan',
        8: 'plum2'
    }

    #
    matrix_background_color = 'gray85'

    # Tetromino definitions:
    tetronimos = {
        'L': {'shape': [[0,0,0],[2,2,2],[2,0,0]]},
        'O': {'shape': [[3,3],[3,3]]},
        'Z': {'shape': [[0,0,0],[4,4,0],[0,4,4]]},
        'S': {'shape': [[0,0,0],[0,5,5],[5,5,0]]},
        'J': {'shape': [[0,0,0],[6,6,6],[0,0,6]]},
        'I': {'shape': [[0,0,0,0],[0,0,0,0],[7,7,7,7],[0,0,0,0]]},
        'T': {'shape': [[0,0,0],[8,8,8],[0,8,0]]}
    }

    # Tetromino randomization:
    random_method = 'double_bag' # random permutation of group of two sets of tetrominoes are generated

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
