# -*- coding: utf-8 -*-

"""
`chess` generate the chessboard and initiate the game
"""


# ///////////////////////////////////////////////////
# Python packages
from itertools import product
from copy import copy
import logging
import math

# ---------------------------------------------------

# ///////////////////////////////////////////////////
# My modules
from piece import King
from piece import Queen
from piece import Rook
from piece import Bishop
from piece import Knight
# ---------------------------------------------------

# ///////////////////////////////////////////////////

LOG_FILENAME = 'chess.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)
logging.debug('')


class Chess(object):
    """ Chess class """
    def __init__(self, params):
        self.chess_output = []
        self.solutions = 0
        self.width = params[0]
        self.height = params[1]
        self.dict_pieces = params[2]
        self.number_pieces = reduce(lambda x, y: x+y, params[2].values())
        # Create all pieces objects
        self.pieces = self.__create_pieces(params[2])
        self.pieces_types = [i.get_symbol() for i in self.pieces]
        print self.pieces_types
        self.chessboard = Chessboard(self.width, self.height)

    def __create_pieces(self, pieces_dict):
        """ Create pieces """
        kings_list = [King() for _ in xrange(pieces_dict['King'])]
        queens_list = [Queen() for _ in xrange(pieces_dict['Queen'])]
        rook_list = [Rook() for _ in xrange(pieces_dict['Rook'])]
        bishop_list = [Bishop() for _ in xrange(pieces_dict['Bishop'])]
        knight_list = [Knight() for _ in xrange(pieces_dict['Knight'])]
        pieces = list()
        pieces.extend(kings_list)
        pieces.extend(queens_list)
        pieces.extend(rook_list)
        pieces.extend(bishop_list)
        pieces.extend(knight_list)
        return pieces

    def print_solution_chessboard(self):
        pass

    def run_game(self):
        """ Initiate the Chessboard and starts the game """
        self.populate(self.pieces, self.chessboard)
        duplication = [math.factorial(x) for x in self.dict_pieces.values()]
        self.solutions = (self.solutions)/reduce(lambda x, y: x*y, duplication)
        self.print_solution_chessboard()

    def populate(self, pieces, chessboard):
        """
        Initiate the Chessboard and starts the game

        Keyword arguments:
        pieces -- the pieces that are not put on the chessboard
        chessboard -- the chessboard
        """

        waiting_pieces = copy(pieces)
        logging.debug("Start Populate")
        logging.debug("with parameters:{0}{1}".format(pieces, chessboard))
        logging.debug('#####################################################')
        chessboard.print_logs('')
        logging.debug('#####################################################')
        p = pieces[0]
        logging.debug("--------------------------------")
        logging.debug(">>>>>>>> piece".format(p.pos(), p))

        if not chessboard.empty_squares:
                pass
        else:
            # Check all possible mouvments for a piece
            for s in copy(chessboard.empty_squares):
                logging.debug(">>>>square {0}".format(s.coordinates()))
                # move the piece in the chessboard
                p.deplace_piece(s)
                logging.debug(">>>>>>>> piece".format(p.pos(), p))

                if chessboard.can_put_on(p):
                    # Update chesseBoard
                    chessboard.allocated(p)
                    # Check if all pieces are in Board
                    _leng = len(chessboard.allocated_pieces)
                    if _leng == len(self.pieces):
                        logging.debug("Solution")
                        print "---------Possible Solution-----------"
                        solution_list = []
                        for i in chessboard.allocated_pieces:
                            print i.pos(), i.get_symbol()
                            solution_list.append(i.pos())
                        solution_list.sort()
                        self.chess_output.append(solution_list)
                        self.solutions += 1

                        print "------------------------------"

                    else:
                        # fix the piece in the Chessboard
                        # populate with pieces except in the board
                        logging.debug("run recursive Populate")
                        if p in waiting_pieces:
                            waiting_pieces.remove(p)
                        self.populate(waiting_pieces, chessboard)

                    # Remove the piece from the Chessboard
                    # and range to the next empty square
                    logging.debug("remove from chessboard")
                    logging.debug("removed piece position:{0}{1}"
                                  .format(p.pos(), p))
                    chessboard.remove_piece(p)

                else:
                    logging.debug("can attack !!")
                    continue

            logging.debug("---------------END_S--------------------*")


class Chessboard():
    """
    The chessboard class, manages and saves pieces moves and positions
    """

    # ///////////////////////////////////////////////////
    def __init__(self, x, y):
        """
        Attributes:
        `board`            -- All squares that formed the Chessboard.
        `allocated_squares`-- Squares reserved by pieces and their attack area.
        `allocated_pieces` -- The piece put on the ChessBoard.
        `empty_squares`    -- The current empty squares in the Chessboard
        """
        list_of_board = list(product(range(1, x+1), range(1, y+1)))
        self.board = [Square(x[0], x[1]) for x in list_of_board]
        print ">>> Chess Board", len(list_of_board)
        self.allocated_squares = list()
        self.empty_squares = copy(self.board)
        self.allocated_pieces = list()

    def __update_allocated_squares(self, piece):
        """
        Updates piece positions on the chessboard
        """
        # Allocated piece square in the board
        for s in self.board:
            if s.coordinates() == piece.pos():
                self.allocated_squares.append(s)
                self.empty_squares.remove(s)
        # Allocated all square can be attacked
        for square in copy(self.empty_squares):
            if piece.check_attack(square):
                # print "piece {0} can attack {1} >>>".
                # format(piece.pos(),square.coordinates())
                self.allocated_squares.append(square)
                self.empty_squares.remove(square)

    def allocated(self, piece):
        """
        Updates the Chessboard after every piece's movement
        """
        if piece not in self.allocated_pieces:
            self.allocated_pieces.append(piece)
        self.__update_allocated_squares(piece)

    def remove_piece(self, piece):
        """Removes a piece from the chessboard"""

        logging.debug("Remove piece {0} from ChessBoard {1}".
                      format(piece.pos(), self))
        self.allocated_pieces.remove(piece)
        self.allocated_squares = list()
        self.empty_squares = copy(self.board)
        new_pieces_list = copy(self.allocated_pieces)
        for new_p in new_pieces_list:
            self.allocated(new_p)

    def can_put_on(self, piece):
        """
        Checks whether the piece can attack
        other pieces in the Chessboard
        """
        test = True
        if self.allocated_pieces:
            for new_p in self.allocated_pieces:
                if new_p.pos() != piece.pos() and piece.check_attack(new_p):
                    test = False
                    break
        return test

    def print_logs(self, msg=''):
        """
        print message logs about the parameters of
        the current Chessboard
        """
        logging.debug('###########################################')
        logging.debug(" {0}chessboard allocated_squares:".format(msg))
        self.__print_squares(self.allocated_squares)
        logging.debug("{0} chessboard empty_squares:".format(msg))
        self.__print_squares(self.empty_squares)
        logging.debug("{0} chessboard allocated Pieces:".format(msg))
        self.__print_squares(self.allocated_pieces)

    def __print_squares(self, list_input):
        if list_input and str(list_input[0].__class__) == "chess.chess.Square":
            logging.debug([i.coordinates()for i in list_input]),
        else:
            logging.debug([i.pos()for i in list_input]),


class Square():
    """
    Represents a position on the Board
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_allocated = None

    def coordinates(self):
        return (self.x, self.y)

    def allocate(self, piece):
        self.is_allocated = piece
