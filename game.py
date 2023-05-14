import numpy as np 
class Board:    
    # represents a board in the game.

    def __init__(self):
        
        # board dimensions 
        self.rows = 9
        self.columns = 9 

        # reference board visualization on readme to understand new game board and how this array works.
        
        self.board = np.array([
             (2, 0), (6, 0), (4, 0),
             (0, 4), (8, 4), 
             (2, 8), (6, 8), (4, 8)
            ])

    
    # takes a coordinate value and turns it into an integer that can represent the board.
    # hint, there is MATH INVOLVEDDD
    def encode(self, coordinate_point):
         return ((coordinate_point[1] + 1) * 9) - (8 - coordinate_point[0])

    # takes an encoded value and turns it into a coordinate point.
    # hint, there is MATH INVOLVEDDD
    def decode(self, encoded_value):
        return ((( encoded_value - 1 ) % 9), ((encoded_value - 1) // 9))

    # print an encoded version of the board, well formatted in the terminal.
    def print_full_board(self):
        pass
