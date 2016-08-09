# -*- coding: utf-8 -*-


from chess.chess import Chess
import unittest
             


class TestBuildChess(unittest.TestCase):
    """
    `TestBuildChess()` class is unit-testing the class
    Chess().
    """

    # ///////////////////////////////////////////////////
    def setUp(self):
        params = [4, 4]
        pieces = {'King': 2, 'Queen': 1, 'Bishop': 1, 'Rook': 1, 'Knight': 1}
        params.append(pieces)
        self.chess = Chess(params)

    # ///////////////////////////////////////////////////
    def test_build_chess(self):
        """Tests validity of build chessboard"""

        self.chess.pieces_types.sort()
        self.assertEqual(self.chess.pieces_types == ['B','K', 'K','N', 'Q','R'], True)
        self.assertEqual(self.chess.number_pieces == 6, True)
    
    def test_solution_only_kings(self):
        params = [5, 5]
        pieces = {'King': 2, 'Queen': 0, 'Bishop': 0, 'Rook': 0, 'Knight': 0}
        params.append(pieces)
        self.chess = Chess(params)
        self.chess.run_game()
        self.assertEqual(self.chess.solutions == 228, True)
        
    def test_solution_only_queens(self):
        params = [5, 5]
        pieces = {'King': 0, 'Queen': 2, 'Bishop': 0, 'Rook': 0, 'Knight': 0}
        params.append(pieces)
        self.chess = Chess(params)
        self.chess.run_game()
        self.assertEqual(self.chess.solutions == 140, True)
                
    def test_solution_only_bishops(self):
        params = [5, 5]
        pieces = {'King': 0, 'Queen': 0, 'Bishop': 2, 'Rook': 0, 'Knight': 0}
        params.append(pieces)
        self.chess = Chess(params)
        self.chess.run_game()
        self.assertEqual(self.chess.solutions == 240, True)
                
    def test_solution_only_rooks(self):
        params = [5, 5]
        pieces = {'King': 0, 'Queen': 0, 'Bishop': 0, 'Rook': 2, 'Knight': 0}
        params.append(pieces)
        self.chess = Chess(params)
        self.chess.run_game()
        self.assertEqual(self.chess.solutions == 200, True)
                
    def test_solution_only_knights(self):
        params = [5, 5]
        pieces = {'King': 0, 'Queen': 0, 'Bishop': 0, 'Rook': 0, 'Knight': 2}
        params.append(pieces)
        self.chess = Chess(params)
        self.chess.run_game()
        self.assertEqual(self.chess.solutions == 252, True)
        
      def test_soution(self):
        params = [5, 5]
        pieces = {'King': 1, 'Queen': 1, 'Bishop': 1, 'Rook': 1, 'Knight': 1}
        params.append(pieces)
        self.chess = Chess(params)
        self.chess.run_game()
        self.assertEqual(self.chess.solutions == 3488, True)

if __name__ == '__main__':
    unittest.main()
