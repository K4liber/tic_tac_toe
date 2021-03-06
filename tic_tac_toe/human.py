from typing import Optional, Tuple

from tic_tac_toe.board import Board
from tic_tac_toe.utils import CROSS, INT_TO_SIGN
from tic_tac_toe.player import PlayerInterface


class Human(PlayerInterface):
    def __init__(self, sign: int, name: str = 'Human'):
        super().__init__(sign, name)

    def get_move(self, current_board: Board) -> Optional[Tuple[int, int]]:
        your_move = input(f'{self.name}, please enter your value ({INT_TO_SIGN[self.sign]}): ')
        row_col = int_to_move(int(your_move))

        if row_col in current_board.get_possible_moves():
            return row_col

        print('The position is already taken. Please choose the empty one.')
        return self.get_move(current_board)


def int_to_move(value: int) -> Tuple[int, int]:
    return divmod(value, 3)
