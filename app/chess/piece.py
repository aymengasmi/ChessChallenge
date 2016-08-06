from math import hypot


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

    def __init__(self):
        ChessPiece.__init__(self)
        self.symbol = 'K'

        print '>>> Buil king piece'

    def check_attack(self, pos):
        dist = hypot(self.x - pos.x, self.y - pos.y)
        if dist <= 1:
            return True
        else:
            return False


class Queen(ChessPiece):

    def __init__(self):
        ChessPiece.__init__(self)
        self.symbol = 'Q'

        print '>>> Buil Queen piece'

    def check_attack(self, pos):
        return True
