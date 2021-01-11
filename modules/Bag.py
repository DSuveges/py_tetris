import numpy as np



class Bag():
    """
    This module generates a permuation of the provided list of tetronimos
    """
    def __init__(self, tetronimos, random_method='double_bag'):
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
        else:
            self.bag = np.random.choice(self.tetronimos)

        np.random.shuffle(self.bag)


    def pull_one(self):

        picked_tetronimo = self.bag.pop()

        if len(self.bag) == 0: 
            self.generate_bag()

        return picked_tetronimo['shape']

    def next_one(self):

        return self.bag[-1]['shape']

