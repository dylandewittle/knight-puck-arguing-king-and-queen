import numpy as np 

class Board:    
    # represents a board in the game.

    def __init__(self):
        self.rows = 8
        self.columns = 8

        # Some important notes:
        # 1. the board is zero indexed.
        # the first 3 positions are for white pieces.
        # the last 3 positions are for black pieces.
        # the 3rd position in every sub array is the puck position to be passed.
        # it is also important to note that the puck can be in its own spot, alone.
        # but to be passed, it needs to land in the hands of a knight.
        
        self.board = np.array(
            [(0, 0), (7, 0), (4, 0)
            (0, 7), (7, 7), (4, 7)]
            )

    
    # takes a coordinate value and turns it into an integer that can represent the board.
    # hint, there is MATH INVOLVEDDD
    def encode(self, coordinate_point):
        pass

    # takes an encoded value and turns it into a coordinate point.
    # hint, there is MATH INVOLVEDDD
    def decode(self, encoded_value):
        pass

    # print an encoded version of the board, well formatted in the terminal.
    def print_full_board(self):
        pass
