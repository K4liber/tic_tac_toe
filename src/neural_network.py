import copy
from typing import Optional, Tuple

import numpy as np
import pandas as pd

from src.board import Board
from src.player import PlayerInterface

from keras.models import Sequential
from keras.layers import Dense


class NeuralNetwork(PlayerInterface):
    _MODEL_FILE = 'model.pickle'

    def __init__(self, sign: int, name: str = 'Minimax'):
        super().__init__(sign, name)
        self._model = Sequential()
        self._model.add(Dense(9, input_dim=9, activation='relu'))
        self._model.add(Dense(12, activation='relu'))
        self._model.add(Dense(1, activation='sigmoid'))
        self._model.compile(loss='binary_crossentropy', optimizer='adam', metrics='MeanSquaredError')
        df = pd.read_csv('data.csv', delimiter=',')
        x = df.iloc[:, 0:9]
        y = df.iloc[:, 9]
        self._model.fit(x, y, epochs=150, batch_size=10)

    def _get_score(self, board: Board) -> float:
        return self._model.predict(np.array(board.state).reshape(-1, 9))

    def get_move(self, current_board: Board) -> Optional[Tuple[int, int]]:
        lowest_score = 1000
        best_move = None

        for move in current_board.get_possible_moves():
            board_copy = copy.deepcopy(current_board)
            board_copy.set(move[0], move[1], self.opposite_sign)
            move_score = self._get_score(board_copy)

            if move_score < lowest_score:
                lowest_score = move_score
                best_move = move

        return best_move
