import pygame
import numpy as np
import time

from modules.config import Configurations
from modules.Bag import Bag
from modules.Matrix import Matrix
from modules.Plot import MatrixPlot, BackgroundPlot, NextElementPlot, LabelsPlot
from modules.Scoring import Score


class tetris(Configurations):


    def __init__(self, display, level=1, player='Player 1'):
        """
        
        """
        self.level = level
        self.player = player
        self.display = display
        self.display.fill(self.display_color)


    def pause(self):
        """
        Keeping the game paused until it is not unpaused
        """
        while True:
            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        return


    def play(self):
        ##
        ## Initialize game:
        ##
        bag_obj          = Bag()
        Background_obj   = BackgroundPlot(self.display)
        labels_obj       = LabelsPlot(self.display)
        next_element_obj = NextElementPlot(self.display)
        matrix_plot_obj  = MatrixPlot(self.display)
        scoring_obj      = Score(level=self.level)

        # Initialize matrix
        m = Matrix()

        # Start clock:
        time_elapsed_since_last_action = 0
        clock = pygame.time.Clock()

        # Filling panels:
        labels_obj.update_player(self.player)
        labels_obj.update_score(scoring_obj.get_score())
        labels_obj.update_level(scoring_obj.get_level())
        labels_obj.update_rows(scoring_obj.get_rows())
        labels_obj.update_tetris_rate(scoring_obj.get_tetris_rate())

        while True: 
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT: 
                    break

            # If no tetromino is in the matrix, give one:
            if m.tetromino is None:
                m.add_tetromino(bag_obj.pull_one())
                next_element_obj.draw_next(bag_obj.show_next())

            # Rotating and moving the tetromino:
            for event in events:
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_DOWN:
                        m.move_down()
                        pygame.key.set_repeat(300, 100)
                    if event.key == pygame.K_LEFT:
                        m.move_left()
                        pygame.key.set_repeat(300, 100)
                    if event.key == pygame.K_RIGHT:
                        m.move_right()
                        pygame.key.set_repeat(300, 100)

                    # Rotate:
                    if event.key == pygame.K_a:
                        m.rotate_left()
                        pygame.key.set_repeat(300, 100)
                    if event.key == pygame.K_d:
                        m.rotate_right()
                        pygame.key.set_repeat(300, 100)
                    
                    # Hard dropping:
                    if event.key == pygame.K_SPACE:
                        scoring_obj.add_hard_drop_score(m.drop())
                    
                    # Pause:
                    if event.key == pygame.K_p:
                        self.pause()

                    # Returning to menu:
                    if event.key == pygame.K_m:
                        return scoring_obj

            # Move tetronimo down:
            dt = clock.tick() 
            time_elapsed_since_last_action += dt

            # dt is measured in milliseconds, therefore 250 ms = 0.25 seconds
            if time_elapsed_since_last_action > 700:
                down_ret = m.move_down()

                # If we no longer can move down, returning to menu:
                if down_ret == 'game over':
                    return scoring_obj

                # reset it to 0 so you can count again
                time_elapsed_since_last_action = 0 

            # After every tick, we check for completed rows and update:
            completed_rows = m.test_for_complete_row()

            if completed_rows > 0:
                scoring_obj.rows_cleared(completed_rows)
                labels_obj.update_score(scoring_obj.get_score())
                labels_obj.update_level(scoring_obj.get_level())
                labels_obj.update_rows(scoring_obj.get_rows())
                labels_obj.update_tetris_rate(scoring_obj.get_tetris_rate())

            # Update screen:
            matrix_plot_obj.draw_matrix(m.get_state())
            pygame.display.flip()

