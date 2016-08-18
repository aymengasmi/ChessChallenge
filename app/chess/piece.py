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
        """ Initiate a piece in a chessboard"""
        self.x_cord = 0
        self.y_cord = 0
        self.symbol = ''
        self.square = None
        self.squares = list()

    def deplace_piece(self, square):
        """ change piece current position to the square position """
        self.x_cord = square.x_cord
        self.y_cord = square.y_cord

    def get_symbol(self):
        """return the character representation of this chess piece """
        return self.symbol

    def pos(self):
        """ return current piece position  """
        return(self.x_cord, self.y_cord)


class King(ChessPiece):
    """ King class"""
    def __init__(self):
        """ Initiate a King"""
        ChessPiece.__init__(self)
        self.symbol = 'K'

    def check_attack(self, target):
        """ check if King object can attack the position pos"""
        dist = hypot(self.x_cord - target.x_cord, self.y_cord - target.y_cord)
        if dist <= sqrt(2):
            return True
        else:
            return False


class Queen(ChessPiece):
    """ Queen class """
    def __init__(self):
        """ Initiate the queen """
        ChessPiece.__init__(self)
        self.symbol = 'Q'

    def check_attack(self, target):
        """ check if the queen attack can be done as Rook or Bishop """
        if self.__rook_attack(target) or self.__bishop_attack(target):
            return True
        else:
            return False

    def __bishop_attack(self, target):
        """ bishop attack method """
        if abs(self.y_cord-target.y_cord) == abs(self.x_cord-target.x_cord):
            return True

    def __rook_attack(self, target):
        """ rook attack method"""
        if self.x_cord == target.x_cord or self.y_cord == target.y_cord:
            return True


class Rook(ChessPiece):
    """ Rook class """
    def __init__(self):
        """ initiate  Rook """
        ChessPiece.__init__(self)
        self.symbol = 'R'

    def check_attack(self, target):
        """ check if the rook can attack"""
        if self.x_cord == target.x_cord or self.y_cord == target.y_cord:
            return True
        else:
            return False


class Bishop(ChessPiece):
    """ Bishop class """

    def __init__(self):
        """ Initiate Bishop piece  """
        ChessPiece.__init__(self)
        self.symbol = 'B'

    def check_attack(self, target):
        """ check the attack of the bishop """
        if abs(self.y_cord-target.y_cord) == abs(self.x_cord-target.x_cord):
            return True
        else:
            return False


class Knight(ChessPiece):
    """ Knight class """
    def __init__(self):
        """ Initiate Knight """
        ChessPiece.__init__(self)
        self.symbol = 'N'

    def check_attack(self, target):
        """ check if the knight can attack """
        if abs(target.x_cord-self.x_cord) == 2 and abs(target.y_cord-self.y_cord) == 1:
            return True
        else:
            if abs(target.x_cord-self.x_cord) == 1 and abs(target.y_cord-self.y_cord) == 2:
                return True
            else:
                return False
