

class Score(object):
    """
    This class maintains the score of the player, the cleared lines and the current level
    """

    score = 0
    level = 1 
    cleared_lines = 0

    def __init__(self, scoring, level=None):

        # Futureproofing: allows user start from a given level:
        if level:
            self.level = level

        self.scoring_multiplier = scoring['multiplier']
        self.soft_drop_score = scoring['soft_drop_score']
        self.hard_drop_score = scoring['hard_drop_score']

    def rows_cleared(self, rows_cleared=None):
        """
        Takes the number of rows cleared and calculates the score
        """

        if rows_cleared is None or rows_cleared == 0    :
            return

        # If at least one row is cleared:
        self.cleared_lines += rows_cleared

        self.score += self.scoring_multiplier[rows_cleared] * self.level

        # Testing if we go to the next level:
        if int(self.cleared_lines / 10) >= self.level:
            self.level += 1


    def add_hard_drop_score(self, drops):

        if drops is not None:
            self.score += self.hard_drop_score * drops


    def get_level(self):
        return self.level


    def get_score(self):
        return self.score


    def get_rows(self):
        return self.cleared_lines
