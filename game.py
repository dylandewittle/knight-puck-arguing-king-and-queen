from itertools import product
class Board:    
    # represents a board in the game.

    def __init__(self):
        
        # board dimensions 
        self.rows = 9
        self.columns = 9 
        self.king_and_queen_fight = False

        # reference board visualization on readme to understand new game board and how this array works.
        
        self.board = [
             (2, 0), (6, 0), (4, 0),
             (0, 4), (8, 4), 
             (2, 8), (6, 8), (4, 8)
            ]
        self.encoded_board = {}
        for i, coordinate in enumerate(self.board):
            self.encoded_board[i] = self.encode(coordinate)
    
    """
    Design choice: What do I want the list of actions to be?
    hypothetically... you return -> [ (4, 1) ]
    """

    # TODO: take in a new move, and update the global board.
    def update_board(self, piece, new_move):
        if piece == "wk1":
            self.board[0] = new_move
        elif piece == "wk2":
            self.board[1] = new_move
        elif piece == "wb":
            self.board[2] = new_move
        elif piece == "K":
            self.board[3] = new_move 
        elif piece == "Q":
            self.board[4] = new_move
        elif piece == "bk1":
            self.board[5] = new_move
        elif piece == "bk2":
            self.board[6] = new_move    
        elif piece == "bp":
            self.board[7] = new_move
        else:
            print("Invalid piece entered.")      
    # TODO:
    def get_knight_moves(self, player_color):
        if player_color == "White":
            #moves of first white knight
            x, y = self.board[0][0], self.board[0][1] 
            moves = list(product([x-1, x+1],[y-2, y+2])) + list(product([x-2,x+2],[y-1,y+1]))
            moves = [(x,y) for x,y in moves if x >= 0 and y >= 0 and x < 8 and y < 8]
            #moves of second white knight
            x, y = self.board[1][0], self.board[1][1] 
            moves2 = list(product([x-1, x+1],[y-2, y+2])) + list(product([x-2,x+2],[y-1,y+1]))
            moves2 = [(x,y) for x,y in moves2 if x >= 0 and y >= 0 and x < 8 and y < 8]
            #total moves of both white knights, remove duplicates and coordinates king, queen, and white knights occupy
            total_moves = set(moves + moves2)
            total_moves = total_moves.difference((self.board[0], self.board[1], self.board[3], self.board[4]))
            return total_moves
        if player_color == "Black":
            #moves of first black knight
            x, y = self.board[5][0], self.board[5][1] 
            moves = list(product([x-1, x+1],[y-2, y+2])) + list(product([x-2,x+2],[y-1,y+1]))
            moves = [(x,y) for x,y in moves if x >= 0 and y >= 0 and x < 8 and y < 8]
            #moves of second black knight
            x, y = self.board[6][0], self.board[6][1] 
            moves2 = list(product([x-1, x+1],[y-2, y+2])) + list(product([x-2,x+2],[y-1,y+1]))
            moves2 = [(x,y) for x,y in moves2 if x >= 0 and y >= 0 and x < 8 and y < 8]
            #total moves of both black knights, remove duplicates and coordinates king, queen, and black knights occupy
            total_moves = set(moves + moves2)
            total_moves = total_moves.difference((self.board[5], self.board[6], self.board[3], self.board[4]))
            return total_moves

    def get_football_moves(self, player_color):
        if player_color == "White":
            return []
        if player_color == "Black":
            return []

    def some_helper_method_to_traverse_board(self):
        pass

    def get_king_moves(self):
        #if king is on edges, return only one move to left or right
        if self.board[3][0] == 0:
            return [(1, 4)]
        if self.board[3][0] == 8:
            return [(7, 4)]
        #otherwise return moves to both left in right
        else:
            return [((self.board[3][0] - 1), 4), ((self.board[3][0] + 1), 4)]

    def get_queen_moves(self):
        #exact same idea as king
        if self.board[4][0] == 0:
            return [(1, 4)]
        if self.board[4][0] == 8:
            return [(7, 4)]
        else:
            return [((self.board[3][0] - 1), 4), ((self.board[3][0] + 1), 4)]
    
    def has_the_game_ended(self):
        if self.board[2][1] == 8:
            if self.board[0] == self.board[2] or self.board[1] == self.board[2]:
                return "White Wins"
        if self.board[7][1] == 0:
            if self.board[5] == self.board[7] or self.board[6] == self.board[7]:
                return "Black Wins"
        return "No Winner Yet"
    
    """ 
    Return a list of all the valid moves that you can take.
    """
    def obtain_all_valid_moves(self, player_color):
        valid_moves = []
        if player_color == "White":
            valid_moves += self.get_king_moves() + self.get_queen_moves() + list(self.get_knight_moves("White")) + self.get_football_moves("White")
            return valid_moves
        if player_color == "Black":
            valid_moves += self.get_king_moves() + self.get_queen_moves() + list(self.get_knight_moves("Black")) + self.get_football_moves("Black")
            return valid_moves

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
        for i in range(1, 82):
            if i in list(self.encoded_board.values()):
                for key, value in self.encoded_board.items():
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
print(board.get_queen_moves())
print(board.get_knight_moves("White"))

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