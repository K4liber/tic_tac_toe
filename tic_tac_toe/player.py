import abc
from typing import Optional, Tuple

from tic_tac_toe.board import Board


class PlayerInterface:
    def __init__(self, sign: int, name: str):
        self._sign = sign
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @property
    def sign(self) -> int:
        return self._sign

    @property
    def opposite_sign(self):
        return -1 * self._sign

    @abc.abstractmethod
    def get_move(self, current_board: Board) -> Optional[Tuple[int, int]]:
        pass