import numpy as np



class Bag():
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
    def __init__(self, tetronimos, random_method='double_bag', seed=None):

        # Setting the random seed if present:
        if seed is not None:
            np.random.seed(seed)

        self.tetronimos = list(tetronimos.values())
        self.random_method = random_method
        self.generate_bag()


    def generate_bag(self):
        if self.random_method == 'single_bag':
            self.bag =  self.tetronimos.copy()
        elif self.random_method == 'double_bag':
            self.bag = self.tetronimos.copy() * 2
        elif self.random_method == 'triple_bag':
            self.bag = self.tetronimos.copy() * 3
        elif self.random_method == 'random':
            self.bag = [np.random.choice(self.tetronimos)]
        else:
            raise ValueError(f'Unknown bag generation method: {self.random_method}.')

        np.random.shuffle(self.bag)


    def pull_one(self):

        picked_tetronimo = self.bag.pop()

        if len(self.bag) == 0: 
            self.generate_bag()

        return picked_tetronimo['shape']

    def next_one(self):

        return self.bag[-1]['shape']

