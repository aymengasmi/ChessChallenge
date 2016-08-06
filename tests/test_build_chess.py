# -*- coding: utf-8 -*-


from app.chess.chess import Chess
import unittest


class TestBuildChess(unittest.TestCase):
    """
    `TestBuildChess()` class is unit-testing the class
    Chess().
    """

    # ///////////////////////////////////////////////////
    def setUp(self):
        params = [4, 4]
        pieces = {'King': 2, 'Queen': 1, 'Bishop': 0, 'Rook': 0, 'Knight': 0}
        params.append(pieces)
        self.chess = Chess(params)

    # ///////////////////////////////////////////////////
    def test_solve(self):
        """Tests validity of solution"""
        self.assertEqual(self.chess.pieces_types == ['K', 'K', 'Q'], True)
        self.assertEqual(self.chess.number_pieces == 3, True)
#       self.assertEqual(self.chess.solutions == 1, True)
       

if __name__ == '__main__':
    unittest.main()
    
