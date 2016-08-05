from piece import King, Queen
from itertools import product


class Chess(object):

    def __init__(self, params):

        self.solutions = 0
        self.width = params[0]
        self.height = params[1]
        self.number_pieces = reduce(lambda x, y: x+y, params[2].values())

        # Create all pieces objects
        self.pieces = self.create_pieces(params[2])
        self.pieces_types = [p.get_symbol() for p in self.pieces]
        print self.pieces_types

    def create_pieces(self, pieces_dict):
        kings_list = [King() for _ in xrange(pieces_dict['King'])]
        queens_list = [Queen() for _ in xrange(pieces_dict['Queen'])]
        pieces = list() 
        
        pieces.extend(kings_list)
        pieces.extend(queens_list)
        return pieces

    def build_chess(self):
        board = Chessboard(self.width, self.height)
        self.populate(board, self.pieces)

    def populate(self):
        return self.solutions


class Chessboard():

    def __init__(self, x, y):
        list_of_board = list(product(xrange(1, x+1), xrange(1, y+1)))
        self.board = [Square(x[0], x[1]) for x in list_of_board]
        print ">>> Chess Board", list_of_board
        self.allocated_squares = []
        self.empty_squares = self.board
        print "Empty Square ChessBoard", [x.call() for x in self.empty_squares]
        print "Empty Allocated Squares in ChessBoard", self.allocated_squares

    def check_allocated_squares(self):
        for square in self.board:
            if square.is_allocated:
                self.allocated_squares.append(square)


class Square():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_allocated = False

    def call(self):
        return (self.x, self.y)

    def allocate(self):
        self.is_allocated = True
