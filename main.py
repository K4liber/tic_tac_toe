from src.board import Board
from src.human import Human
from src.minimax import Minimax, print_all_possible_scores
from src.neural_network import NeuralNetwork
from src.random import Random
from src.utils import CROSS, CIRCLE


def play():
    board = Board()
    states = [board]
    iteration = 0
    player_1 = NeuralNetwork(CROSS)
    player_2 = Random(CIRCLE)  # Human(CIRCLE)
    players = [player_1, player_2]
    print(board)

    while board.get_winner() not in {CIRCLE, CROSS}:
        player = players[iteration % 2]
        print(f'############## STEP {iteration} ################')
        iteration += 1

        if len(board.get_possible_moves()) == 0:
            print('NOBODY WON!')
            break

        print(f'Player "{player.name}" move: \n')
        row_col = player.get_move(board)
        board.set(row_col[0], row_col[1], player.sign)
        print(board)

        if board.get_winner() == player_1.sign:
            print(f'Player "{player_1.name}" WON!')
            break
        elif board.get_winner() == player_2.sign:
            print(f'Player "{player_2.name}" WON!')
            break

        states.append(board)


if __name__ == '__main__':
    play()
