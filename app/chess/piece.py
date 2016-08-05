class ChessPiece(object):

    def __init__(self):
        self.column = 0
        self.row = 0
        self.symbol = ''

    # Checks piece can attack the specified position
    def can_attack_position(self, column, row):
        pass

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


class King(ChessPiece):

    def __init__(self):
        self.symbol = 'K'

        print '>>> Buil king piece'

    def can_attack_position(self, column, row):
        return True


class Queen(ChessPiece):

    def __init__(self):
        self.symbol = 'Q'

        print '>>> Buil Queen piece'

    def can_attack_position(self, column, row):
        return True

