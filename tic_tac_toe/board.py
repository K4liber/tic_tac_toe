import copy
import random
from typing import Optional, List, Tuple

import numpy as np
from numpy import ndarray

from tic_tac_toe.utils import CROSS, CIRCLE, EMPTY, INT_TO_SIGN


class Board:
    def __init__(self, matrix: Optional[ndarray] = None):
        self._matrix = matrix if matrix else np.zeros((3, 3), np.int8)

    def __str__(self):
        m = self._matrix
        board_str = f'{INT_TO_SIGN[m[0, 0]]} | {INT_TO_SIGN[m[0, 1]]} | {INT_TO_SIGN[m[0, 2]]}\n'
        board_str += '---------\n'
        board_str += f'{INT_TO_SIGN[m[1, 0]]} | {INT_TO_SIGN[m[1, 1]]} | {INT_TO_SIGN[m[1, 2]]}\n'
        board_str += '---------\n'
        board_str += f'{INT_TO_SIGN[m[2, 0]]} | {INT_TO_SIGN[m[2, 1]]} | {INT_TO_SIGN[m[2, 2]]}\n'
        return board_str

    @property
    def state_str(self):
        return ','.join([str(el) for el in self.state])

    @property
    def state(self) -> Tuple[int]:
        return tuple(self._matrix.flat)

    def get_possible_moves(self) -> List[Tuple[int, int]]:
        rows, cols = np.where(self._matrix == 0)
        return [(rows[i], cols[i]) for i in range(len(rows))]

    def get_random_move(self) -> Optional[Tuple[int, int]]:
        possible_moves = self.get_possible_moves()
        return random.sample(possible_moves, 1)[0]

    def set(self, row: int, col: int, value: int) -> Optional['Board']:
        if value not in {CROSS, CIRCLE} or self._matrix[row, col] in {CROSS, CIRCLE}:
            raise ValueError('Cannot put it here!')

        previous_state = copy.deepcopy(self)
        self._matrix[row, col] = value
        return previous_state

    def get_winner(self) -> int:
        for i in range(3):
            if abs(sum(self._matrix[:, i])) == 3:
                return int(sum(self._matrix[:, i])/3)

            if abs(sum(self._matrix[i, :])) == 3:
                return int(sum(self._matrix[i, :])/3)

        if abs(self._matrix[0, 0] + self._matrix[1, 1] + self._matrix[2, 2]) == 3:
            return int(self._matrix[0, 0])

        if abs(self._matrix[2, 0] + self._matrix[1, 1] + self._matrix[0, 2]) == 3:
            return int(self._matrix[2, 0])

        return EMPTY
