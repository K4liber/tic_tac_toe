import copy
import os
import pickle
from typing import Optional, Tuple

import numpy as np
import pandas as pd

from tic_tac_toe.board import Board
from tic_tac_toe.player import PlayerInterface

from keras.models import Sequential
from keras.layers import Dense


class NeuralNetwork(PlayerInterface):
    _MODEL_FILE = 'weights_14_10_cross.pickle'

    def __init__(self, sign: int, name: str = 'Neural Network'):
        super().__init__(sign, name)
        self._model = Sequential()
        self._model.add(Dense(14, input_dim=9, activation='relu'))
        self._model.add(Dense(10, activation='relu'))
        self._model.add(Dense(1, activation='sigmoid'))
        self._model.compile(loss='binary_crossentropy', optimizer='adam', metrics='MeanSquaredError')

        if os.path.isfile(NeuralNetwork._MODEL_FILE):
            with open(NeuralNetwork._MODEL_FILE, 'rb') as weights_pickle:
                weights = pickle.load(weights_pickle)
                self._model.set_weights(weights)
        else:
            df = pd.read_csv('data_cross.csv', delimiter=',')
            x = df.iloc[:, 0:9]
            y = df.iloc[:, 9]
            self._model.fit(x, y, epochs=300, batch_size=20)
            weights = self._model.get_weights()

            with open(NeuralNetwork._MODEL_FILE, 'wb') as weights_pickle:
                pickle.dump(weights, weights_pickle)

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
