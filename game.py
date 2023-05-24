class Board:    
    # represents a board in the game.

    def __init__(self):
        
        # board dimensions 
        self.rows = 9
        self.columns = 9 

        # reference board visualization on readme to understand new game board and how this array works.
        
        self.board = [
             (2, 0), (6, 0), (4, 0),
             (0, 4), (8, 4), 
             (2, 8), (6, 8), (4, 8)
            ]
    
    """
    Design choice: What do I want the list of actions to be?
    hypothetically... you return -> [ (4, 1) ]
    """

    # TODO: take in a new move, and update the global board.
    def update_board(self, new_move):
        pass
    
    # TODO:
    def get_knight_moves(self, player_color):
        pass
    
    def get_football_moves(self, player_color):
        pass

    def some_helper_method_to_traverse_board(self):
        pass

    def get_king_and_queen_moves(self, player_color):
        pass
    
    def has_the_game_ended(self):
        pass
    
    """ 
    Return a list of all the valid moves that you can take.
    """
    def obtain_all_valid_moves(self, player_color):
        pass
    
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
        encoded_board = {}
        for i, coordinate in enumerate(self.board):
            encoded_board[i] = self.encode(coordinate)
        for i in range(1, 82):
            if i in list(encoded_board.values()):
                for key, value in encoded_board.items():
                    if i == value:
                        if key == 0:
                            print("k", end="   ")
                        elif key == 1:
                            print("k", end="   ") 
                        elif key == 2:
                            print("p", end="   ")
                        elif key == 3:
                            print("K", end="   ")
                        elif key == 4:
                            print("Q", end="   ")
                        elif key == 5:
                            print("k", end="   ")
                        elif key == 6:
                            print("k", end="   ")
                        elif key == 7:
                            print("p", end="   ")
            else:
                print(".", end="   ")
            if ((i) % 9) == 0:
                print("\n")
board = Board()
board.print_full_board() 


"""
Players for the game
"""

class DefaultPlayer:

    # default parameters, feel free to change
    def __init__(self, piece_color):
        pass

    # how it plays the game.
    def strategy(self):
        pass    

class RandomPlayer:
    
    def __init__(self, piece_color):
        pass

    def strategy(self):
        pass