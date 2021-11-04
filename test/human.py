import unittest

from tic_tac_toe.human import Human, int_to_move
from tic_tac_toe.utils import CROSS


class HumanTest(unittest.TestCase):
    def setUp(self) -> None:
        self.human = Human(CROSS, 'Human')

    def test_int_to_move(self):
        self.assertEqual(int_to_move(0), (0, 0))
        self.assertEqual(int_to_move(1), (0, 1))
        self.assertEqual(int_to_move(2), (0, 2))
        self.assertEqual(int_to_move(3), (1, 0))
        self.assertEqual(int_to_move(4), (1, 1))
        self.assertEqual(int_to_move(5), (1, 2))
        self.assertEqual(int_to_move(6), (2, 0))
        self.assertEqual(int_to_move(7), (2, 1))
        self.assertEqual(int_to_move(8), (2, 2))
