# -*- coding: utf-8 -*-

"""
`piece` contains class that represent the pieces that formed a chess game
"""


# ///////////////////////////////////////////////////
# Python packages
from math import hypot
from math import sqrt

# ---------------------------------------------------

# ///////////////////////////////////////////////////


class ChessPiece(object):
    """ General chess piece class """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.symbol = ''
        self.square = None
        self.squares = list()

    # Checks piece can attack the specified position
    def deplace_piece(self, square):
        self.x = square.x
        self.y = square.y

    # return the character representation of this chess piece
    def get_symbol(self):
        return self.symbol

    def set_column(self, column):
        self.column = column

    def get_column(self):
        return self.column

    def set_row(self, row):
        self.row = row

    def get_row(self):
        return self.row

    def pos(self):
        return(self.x, self.y)

    def check_attack(self, p):
        return None


class King(ChessPiece):
    """ King class"""
    def __init__(self):
        ChessPiece.__init__(self)
        self.symbol = 'K'

    def check_attack(self, target):
        """ check if King object can attack the position pos"""
        dist = hypot(self.x - target.x, self.y - target.y)
        if dist <= sqrt(2):
            return True
        else:
            return False


class Queen(ChessPiece):
    """ Queen class """
    def __init__(self):
        ChessPiece.__init__(self)
        self.symbol = 'Q'

    def check_attack(self, target):
        # Will be true if move can be done as Rook or Bishop
        if self.__rook_attack(target) or self.__bishop_attack(target):
            return True
        else:
            return False

    def __bishop_attack(self, target):
        if abs(self.y-target.y) == abs(self.x-target.x):
            return True

    def __rook_attack(self, target):
        if self.x == target.x or self.y == target.y:
            return True


class Rook(ChessPiece):
    """ Rook class """
    def __init__(self):
        ChessPiece.__init__(self)
        self.symbol = 'R'

    def check_attack(self, target):
        if self.x == target.x or self.y == target.y:
            return True
        else:
            return False


class Bishop(ChessPiece):
    """ Bishop class """

    def __init__(self):
        ChessPiece.__init__(self)
        self.symbol = 'B'

    def check_attack(self, target):
        # Check for non-horizontal/vertical and linear movement
        if abs(self.y-target.y) == abs(self.x-target.x):
            return True
        else:
            return False


class Knight(ChessPiece):
    """ Knight class """

    def __init__(self):
        ChessPiece.__init__(self)
        self.symbol = 'N'

    def check_attack(self, target):
        if abs(target.x-self.x) == 2 and abs(target.y-self.y) == 1:
            return True
        else:
            if abs(target.x-self.x) == 1 and abs(target.y-self.y) == 2:
                return True
            else:
                return False
