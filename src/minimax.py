import copy
from typing import Optional, Tuple

from src.board import Board
from src.utils import CROSS, EMPTY
from src.player import PlayerInterface


class Minimax(PlayerInterface):
    def __init__(self, sign: int, name: str = 'Minimax'):
        super().__init__(sign, name)

    def get_move(self, current_board: Board) -> Optional[Tuple[int, int]]:
        best_move = None
        best_score = 0
        possible_moves = current_board.get_possible_moves()

        for move in possible_moves:
            board_copy = copy.deepcopy(current_board)
            board_copy.set(move[0], move[1], self.sign)
            could_be_last = False

            for move_opponent in board_copy.get_possible_moves():
                board_copy_again = copy.deepcopy(board_copy)
                board_copy_again.set(move_opponent[0], move_opponent[1], self.opposite_sign)

                if board_copy_again.get_winner() == self.opposite_sign:
                    could_be_last = True

            if could_be_last:
                continue

            move_score = get_score(board_copy, self.sign)

            if move_score >= best_score:
                best_score = move_score
                best_move = move

        return best_move if best_move is not None else (
            possible_moves[0] if len(possible_moves) else None)


def get_wins_and_all_games(current_board: Board, player: int = CROSS) -> Tuple[int, int]:
    possible_moves = current_board.get_possible_moves()
    wins = 0
    all_settled_games = 0

    for move in possible_moves:
        board_copy = copy.deepcopy(current_board)
        board_copy.set(move[0], move[1], player)
        winner = board_copy.get_winner()

        if winner == EMPTY:
            for move_opposite in board_copy.get_possible_moves():
                board_after_opponent_move = copy.deepcopy(board_copy)
                board_after_opponent_move.set(move_opposite[0], move_opposite[1], -1 * player)
                winner_after_opponent_move = board_after_opponent_move.get_winner()

                if winner_after_opponent_move == player:
                    wins = wins + 1
                    all_settled_games = all_settled_games + 1
                elif winner_after_opponent_move == -1 * player:
                    all_settled_games = all_settled_games + 1
                else:
                    wins_recurrent, all_settled_games_recurrent = get_wins_and_all_games(
                        board_after_opponent_move, player)
                    wins = wins + wins_recurrent
                    all_settled_games = all_settled_games + all_settled_games_recurrent

        else:
            if winner == player:
                wins = wins + 1
                all_settled_games = all_settled_games + 1

            if winner == -1 * player:
                all_settled_games = all_settled_games + 1

    return wins, all_settled_games


def get_score(board: Board, player: int) -> Tuple[float, bool]:
    wins, all_games = get_wins_and_all_games(board, player)
    return (wins/all_games, True) if all_games != 0 else (0, False)


state_to_str = dict()


def print_all_possible_scores():
    _save_all_possible_scores(Board())

    with open('data.csv', 'a') as the_file:
        for line in state_to_str.values():
            the_file.write(f'{line}\n')


def _save_all_possible_scores(board: Board, player: int = CROSS):
    if len(state_to_str) % 1000 == 0:
        print(f'len(state_to_str) = {len(state_to_str)}')

    for move in board.get_possible_moves():
        board_copy = copy.deepcopy(board)
        board_copy.set(move[0], move[1], -1 * player)
        score, is_ok = get_score(board_copy, player)

        if board_copy.state in state_to_str:
            continue

        if is_ok:
            state_to_str[board_copy.state] = f'{board_copy.state_str},{score}'

        for player_move in board_copy.get_possible_moves():
            board_after_player_move = copy.deepcopy(board_copy)
            board_after_player_move.set(player_move[0], player_move[1], player)
            _save_all_possible_scores(board_after_player_move, player)
