from src.board import Board
from src.human import Human
from src.minimax import Minimax, print_all_possible_scores
from src.neural_network import NeuralNetwork
from src.utils import CROSS, CIRCLE


def play():
    board = Board()
    states = [board]
    iteration = 0
    player_1 = Human(CIRCLE)
    player_2 = NeuralNetwork(CROSS)
    players = [player_1, player_2]
    print(board)

    while board.get_winner() not in {CIRCLE, CROSS}:
        player = players[iteration % 2]
        print(f'############## STEP {iteration} ################')
        iteration += 1
        row_col = player.get_move(board)

        if row_col is None:
            print('NOBODY WON!')
            break

        board.set(row_col[0], row_col[1], player.sign)
        print(board)

        if board.get_winner() == CIRCLE:
            print('CIRCLE WON!')
            break
        elif board.get_winner() == CROSS:
            print('CROSS WON!')
            break

        states.append(board)


if __name__ == '__main__':
    play()
