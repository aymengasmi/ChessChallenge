from math import hypot, sqrt


class ChessPiece(object):

    def __init__(self):
        self.x = 0
        self.y = 0
        self.symbol = ''

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

    def __init__(self):
        ChessPiece.__init__(self)
        self.symbol = 'K'
        print '>>> Build King piece'

    def check_attack(self, target):
        """ check if King object can attack the position pos"""
        dist = hypot(self.x - target.x, self.y - target.y)
        if dist <= sqrt(2):
            return True
        else:
            return False


class Queen(ChessPiece):

    def __init__(self):
        ChessPiece.__init__(self)
        self.symbol = 'Q'
        print '>>> Build Queen piece'

    def check_attack(self, target):
        # Will be true if move can be done as Rook or Bishop
        if self.__check_rook_attack(target) or self.__check_bishop_attack(target):
            return True
        else:
            return False

    def __check_rook_attack(self, target):
        if self.x == target.x or self.y == target.y:
            return True

    def __check_bishop_attack(self, target):
        # Check for non-horizontal/vertical and linear movement
        if abs(self.y-target.y) == abs(self.x-target.x):
            return True
