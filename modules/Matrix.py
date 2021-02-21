import numpy as np
import colorsys


# A class to handle matrix actions 

class Matrix():

    def __init__(self, dimensions=(20,10)):

        self.matrix = np.zeros(dimensions)
        self.dimensions = dimensions
        self.tetromino = None
        self.position = [0,0]

        
    def get_state(self):
        """
        This method merges the matrix with a tetromino in a given position
        and returns the matrix.
        
        No update is made here.
        """
        
        if self.tetromino is None or self.position is None:
            return self.matrix[1:]
        
        # Resettig the tetrominos:
        x = self.position[0]
        y = self.position[1]
        m = self.matrix.copy()
        
        for yi, row in enumerate(self.tetromino):
            for xi, value in enumerate(row):
                if value != 0 and yi+y >= 0:
                    m[yi+y][xi+x] = value
                    
        return m[1:]
                

    def test_for_complete_row(self):
        """
        This function call removes completed rows from the matrix 
        and adds new rows to the top.

        Returns with the number of rows deleted
        """

        # Testing if there are a completed row after the merge:
        is_row_complete = np.array([np.all(i) for i in self.matrix])

        # Update matrix if there is a completed row:
        if not is_row_complete.any():
            return 0
        
        # Removing rows:
        try:
            self.matrix = self.matrix[~is_row_complete]    
        except:
            raise ValueError('could not remove row from matrix.')

        # Adding rows to front:
        rows_to_add = len(is_row_complete[is_row_complete])
        self.matrix = np.vstack((np.zeros((rows_to_add,self.dimensions[1])),self.matrix))
        
        return rows_to_add


    ##
    ## Checking tetromino overlap:
    ##
    def is_valid(self, position=None, tetromino=None):
        """
        Might get a new tetromino of a new position. 
        It is superposed to the matrix, and if no clashing is found, 
        the position/tetromino is updated
        """
        if position is None:
            position = self.position.copy()
            
        elif tetromino is None:
            tetromino = self.tetromino.copy()
        else:
            return False
            
        # Loop through all the tetromino cells to see if there's any clash:
        for yi, row in enumerate(tetromino):
            for xi, value in enumerate(row):
                if value == 0:
                    continue
                    
                pos_x = xi + position[0]
                pos_y = yi + position[1]
                                
                # Blocked by the floor:
                if pos_y > self.dimensions[0]:
                    return False
                
                # blocked by the wall:
                if pos_x < 0 or pos_x >= self.dimensions[1]:
                    return False
                
                # blocked by an old tetromino:
                try:
                    if self.matrix[pos_y][pos_x] != 0:
                        return False

                # Reached the floor:
                except IndexError:
                    return False
                
        # If all tests passed, we update the tetromino and the positon:
        self.position = position
        self.tetromino = tetromino
        return True

        
    def add_tetromino(self, tetromino):
        """
        Tetromino is added to the object.
        Also the starting position is calculated based on the type.
        """

        self.tetromino = tetromino 
        if len(tetromino) == 3:
            self.position = [3,-2]
        elif len(tetromino) == 2:
            self.position = [4,-1]
        elif len(tetromino) == 4:
            self.position = [3,-3]
    
    
    def merge_tetromino(self):
        """
        This method updates the matrix by adding the current tetromino
        then deletes the tetromino and its position.
        No check applied here
        """
        x = self.position[0]
        y = self.position[1]
        
        for yi, row in enumerate(self.tetromino):
            for xi, value in enumerate(row):
                if value != 0:
                    self.matrix[yi+y][xi+x] = value
                
        self.tetromino = None
        self.position = None           
        
        
    ##
    ## All logic for the movements of the tetromino are here:
    ##
    def move_left(self):
        """
        Moving the tetromino left with one unit
        """
        if not self.position:
            return None
        new_position = self.position.copy()
        new_position[0] -= 1
        
        # Is it a walid move?
        self.is_valid(position=new_position)


    def move_right(self):
        """
        Moving the tetromino right with one unit
        """
        if not self.position:
            return None
        new_position = self.position.copy()
        new_position[0] += 1
        
        # Is it a walid move?
        self.is_valid(position=new_position)
        

    def move_down(self):
        """
        Moving the tetromino down with one unit. 
        Not testing if there's any complete row.
        """
        if not self.position:
            return None
        
        new_position = self.position.copy()
        new_position[1] += 1
        
        # Is it a walid move?
        is_valid = self.is_valid(position=new_position)
        
        # If it's not a valid move, merge tetromino and test if an rows completed:
        if not is_valid and self.position[1] < 0:
            return 'game over'  
        elif not is_valid:
            self.merge_tetromino()
            return 'Stop'
    
    def rotate_left(self):
        """
        Rotating the tetromino counterclockwise
        """
        if self.tetromino is None:
            return None
        
        tetromino = np.rot90(self.tetromino.copy())
        is_valid = self.is_valid(tetromino=tetromino)       


    def rotate_right(self):
        """
        Rotating the tetromino clockwise
        """
        if self.tetromino is None:
            return None
        
        tetromino = np.rot90(self.tetromino.copy(), k=3)
        is_valid = self.is_valid(tetromino=tetromino)


    def drop(self):
        """
        Hard drop movement
        """
        dropped_rows = 0
        while True:
            return_value = self.move_down()
            dropped_rows += 1
            if return_value is not None:
                return dropped_rows


