import numpy as np
from modules.config import Configurations


class Bag(Configurations):
    """
    This module generates random sequence of tetronimos 
    following a specified rule.

    Supported rules:
      * single, double, triple bag: This method generates a random
        permutation of 1,2 or 3 sets of tetrominos this ensures the 
        repetions of tetrominos within a given distance
      * random: This method generates a random sequence of tetrominos.
        So, arbirarily large sequneces can occur. 
    """
    def __init__(self):

        # Setting the random seed if present:
        if self.random_seed is not None:
            np.random.seed(self.random_seed)

        self.tetronimo_names = list(self.tetronimos.values())
        self.generate_bag()


    def generate_bag(self):
        if self.random_method == 'single_bag':
            self.bag =  self.tetronimo_names.copy()
        elif self.random_method == 'double_bag':
            self.bag = self.tetronimo_names.copy() * 2
        elif self.random_method == 'triple_bag':
            self.bag = self.tetronimo_names.copy() * 3
        elif self.random_method == 'random':
            self.bag = [np.random.choice(self.tetronimo_names)]
        else:
            raise ValueError(f'Unknown bag generation method: {self.random_method}.')

        np.random.shuffle(self.bag)


    def pull_one(self):

        picked_tetronimo = self.bag.pop()

        if len(self.bag) == 0: 
            self.generate_bag()

        return picked_tetronimo['shape']

    def show_next(self):

        return self.bag[-1]['shape']

