from math import fabs
import random
import numpy as np

class Tictactoe(object):
    """
    https://github.com/Zeta36/pytorch-es-tic-tac-toe
    """

    def __init__(self):
        self.board = np.zeros(9)
        self.done = False

    def _check_valid_move(self, action):
        return self.board[action] == 0

    def available_actions(self):
        """actions available to player.
        """
        return [p for p, v in enumerate(self.board) if v == 0]

    def sample(self):
        available_positions = self.available_actions()
        return random.choice(available_positions)

    def step(self, action):
        # pass if game is completed
        if self.done:
            reward = 0
            return self.board, reward, self.done

        # illegal move: occupied spot
        if not self._check_valid_move(action):
            reward = 0
            return self.board, reward, self.done

        # player makes move
        else:
            self.board[action] = 1

        # 3 outcomes: draw, player wins, computer's turn
        if self._is_draw():
            self.done = True
            print "draw"
            reward = 0.00001
            return self.board, reward, self.done
        elif self._is_win():
            self.done = True
            reward = 10
            return self.board, reward, self.done

        # not the terminal state, so computer's turn
        else:
            move = self.sample()
            self.board[move] = -1

            # computer wins
            if self._is_win():
                self.done = True
                reward = -5
                return self.board, reward, self.done
            # draw
            if self._is_draw():
                self.done = True
                reward = 0.00001
                return self.board, reward, self.done

        # game continues
        return self.board, 0, False

    def render(self):
        obs = self.board
        obs = ["X" if (p == 1) else p for p in obs]
        obs = ["O" if (p == -1) else p for p in obs]
        obs = ["-" if (p == 0) else p for p in obs]
        for row in np.array(obs).reshape(3, 3):
            print row

    def _is_draw(self):
        """ check if game ended in a draw.
        """
        if 0 not in self.board and not self._is_win():
            return True
        else:
            return False

    def _is_win(self):
            # check rows
            board = self.board.reshape(3, 3)
            for row in range(3):
                if fabs(np.sum(board[row])) == 3:
                    return True

            # check rows
            transpose_board = board.transpose()
            for column in range(3):
                if fabs(np.sum(transpose_board[column])) == 3:
                    return True

            # 2,4,6 and 0,4,8 cases
            if fabs(self.board[2] + self.board[4] + self.board[6]) == 3:
                return True

            if fabs(self.board[0] + self.board[4] + self.board[8]) == 3:
                return True

            return False