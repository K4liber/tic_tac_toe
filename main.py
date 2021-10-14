from src.board import Board
from src.human import Human
from src.minimax import Minimax, print_all_possible_scores
from src.neural_network import NeuralNetwork
from src.player import PlayerInterface
from src.random import Random
from src.utils import CROSS, CIRCLE, EMPTY, DRAW


def play(board: Board, player_1: PlayerInterface, player_2: PlayerInterface) -> str:
    states = [board]
    iteration = 0

    players = [player_1, player_2]
    print(board)

    while board.get_winner() not in {CIRCLE, CROSS}:
        player = players[iteration % 2]
        print(f'############## STEP {iteration} ################')
        iteration += 1

        if len(board.get_possible_moves()) == 0:
            print('NOBODY WON!')
            return DRAW

        print(f'Player "{player.name}" move: \n')
        row_col = player.get_move(board)
        board.set(row_col[0], row_col[1], player.sign)
        print(board)

        if board.get_winner() == player_1.sign:
            print(f'Player "{player_1.name}" WON!')
            return player_1.name
        elif board.get_winner() == player_2.sign:
            print(f'Player "{player_2.name}" WON!')
            return player_2.name

        states.append(board)


if __name__ == '__main__':
    random_player = Random(CROSS)
    human_player = Human(CIRCLE)
    neural_network_player = NeuralNetwork(CROSS)
    minimax_player = Minimax(CIRCLE)

    player_1 = random_player
    player_2 = minimax_player
    wins = {
        player_1.name: 0,
        player_2.name: 0,
        DRAW: 0
    }
    games_to_play = 100

    for i in range(games_to_play):
        print(f'GAME: {i+1}/{games_to_play}')
        winner_name = play(
            board=Board(),
            player_1=player_1,
            player_2=player_2
        )
        wins[winner_name] += 1

    print(wins)
