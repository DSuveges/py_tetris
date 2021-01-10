import numpy as np


# A class to handle matrix actions 

class Matrix():

    def __init__(self, dimensions=(10,20))

        self.matrix = np.zeroes(dimensions)
        self.dimensions = dimensions
        self.tetromino = None
        self.position = None

    def merge_tetromino(self, tetromino, position, inplace=False):
        """
        This method merges the matrix with a tetromino in a given position
        """

        self.matrix = self.matrix

        # Resettig the tetrominos:
        self.tetromino = None
        self.position = None


    def test_for_complete_row(self):

        return np.array([np.all(i) for i in self.matrix])

    def update_matrix(self, full_rows):
        """
        based on a boolean array, this function removes the complete 
        rows from the matrix and adds empty rows to the front
        """
        # Testing if there are a completed row after the merge:
        rows_to_add = self.test_for_complete_row()

        # Update matrix if there is a completed row:
        if not rows_to_add.any():
            return None
        
        # Removing rows:
        try:
            self.matrix = self.matrix[~full_rows]    
        except:
            raise ValueError('could not remove row from matrix.')

        # Adding rows to front:
        rows_to_add = len(full_rows[full_rows])
        self.matrix =  np.vstack((np.zeroes((rows_to_add,self.dimensions[1])),self.matrix))


    ##
    ## Checking tetronimo overlap:
    ##
    def check_overlap(self, position, tetromino):
        if 'overlap':
            return False
        else:
            return True

    ##
    ## Adding tetromino:
    ##
    def add_tetromino(self, tetromino):
        self.tetromino = tetromino 

        # How the T tetromino looks like:
        # 
        # [[0,0,0], 
        #  [1,1,1],
        #  [0,1,0]]
        # 
        # The  top is not shown, but that's alright.

    ##
    ## All logic for the movements of the tetromino are here:
    ##
    def move_left(self):
        return 0

    def move_right(self):
        return 0

    def move_down(self):
        return 0

    def rotate_left(self):
        return 0

    def rotate_right(self):
        return 0