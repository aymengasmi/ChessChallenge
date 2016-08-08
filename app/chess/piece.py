# -*- coding: utf-8 -*-

"""
`piece` module is responsible for creating the pieces and their parameters

"""


# ///////////////////////////////////////////////////
# Python packages
from math import hypot
from math import sqrt


class ChessPiece(object):
    """
    Define a piece of a chess game
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.symbol = ''

    def deplace_piece(self, square):
        self.x = square.x
        self.y = square.y

    def get_symbol(self):
        """
        return the character that represent the piece
        """
        return self.symbol

    def set_column(self, column):
        self.x = column

    def get_column(self):
        return self.x

    def set_row(self, row):
        self.y = row

    def get_row(self):
        return self.y

    def pos(self):
        return(self.x, self.y)

    def check_attack(self, p):
        return None


class King(ChessPiece):
    """The king piece of a chess game """
    def __init__(self):
        ChessPiece.__init__(self)
        self.symbol = 'K'
        print '>>> Buil king piece'

    def check_attack(self, pos):
        dist = hypot(self.x - pos.x, self.y - pos.y)
        if dist <= sqrt(2):
            return True
        else:
            return False


class Queen(ChessPiece):
    """ The Queen piece of a chess game """
    def __init__(self):
        ChessPiece.__init__(self)
        self.symbol = 'Q'
        print '>>> Buil Queen piece'

    def check_attack(self, pos):
        return False
