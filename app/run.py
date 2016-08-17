# -*- coding: utf-8 -*-

import time
import sys
import argparse

from chess.chess import Chess


parser = argparse.ArgumentParser(description='chess challenge')
parser.add_argument('-m', action="store", dest="width", default=0, type=int)
parser.add_argument('-n', action="store", dest="height", default=0, type=int)
parser.add_argument('-k', action="store", dest="kings", default=0, type=int)
parser.add_argument('-q', action="store", dest="queens", default=0, type=int)
parser.add_argument('-b', action="store", dest="bishops", default=0, type=int)
parser.add_argument('-r', action="store", dest="rooks", default=0, type=int)
parser.add_argument('-kt', action="store", dest="knights", default=0, type=int)
args = parser.parse_args()


if __name__ == "__main__":
    params = []
    pieces = {'Queen': 0, 'King': 0, 'Bishop': 0,  'Rook': 0, 'Knight': 0}

    if len(sys.argv) >= 2:
        print args
        params.append(args.width)
        params.append(args.height)
        pieces['Queen'] = args.queens
        pieces['King'] = args.kings
        pieces['Bishop'] = args.bishops
        pieces['Rook'] = args.rooks
        pieces['Knight'] = args.knights

    else:
        print "No command line arguments"
        params = [7, 7]
        pieces = {'Queen': 2, 'King': 2, 'Bishop': 2,  'Rook': 0, 'Knight': 1}

    params.append(pieces)

    # Define Chessboard through defined params
    chess = Chess(params)
    # Run solution
    start = time.time()
    chess.run_game()
    end = time.time()

    solutions = chess.solutions
    print "Number of solutions: " + str(solutions)
    print "Time (sec): " + str(end - start)
