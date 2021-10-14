import random
from typing import Optional, Tuple

from src.board import Board
from src.player import PlayerInterface


class Random(PlayerInterface):
    def __init__(self, sign: int, name: str = 'Random'):
        super().__init__(sign, name)

    def get_move(self, current_board: Board) -> Optional[Tuple[int, int]]:
        possible_moves = current_board.get_possible_moves()

        if len(possible_moves) == 0:
            return None

        return random.choice(possible_moves)
