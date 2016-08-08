import time
import sys
from chess.chess import Chess


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        params = sys.argv[1]
    else:
        params = [3, 3]

    pieces = {'King': 2, 'Queen': 0, 'Bishop': 0, 'Rook': 0, 'Knight': 0}
    params.append(pieces)

    start = time.time()
    # Define Chessboard through defined params
    chess = Chess(params)
    # Run solution
    chess.run_game()
    end = time.time()
    solutions = chess.solutions
    print "Number of solutions: " + str(solutions)
    print "Time (sec): " + str(end - start)
