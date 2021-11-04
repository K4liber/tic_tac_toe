import random
from typing import Optional, Tuple

from tic_tac_toe.board import Board
from tic_tac_toe.player import PlayerInterface


class Random(PlayerInterface):
    def __init__(self, sign: int, name: str = 'Random'):
        super().__init__(sign, name)

    def get_move(self, current_board: Board) -> Optional[Tuple[int, int]]:
        possible_moves = current_board.get_possible_moves()

        if len(possible_moves) == 0:
            return None

        return random.choice(possible_moves)
