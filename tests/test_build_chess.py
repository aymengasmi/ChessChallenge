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
        self.assertEqual(self.chess.pieces_types == ['K', 'K', 'Q'], True)
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

if __name__ == '__main__':
    unittest.main()
