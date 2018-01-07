from math import fabs
import random
import numpy as np

class Tictactoe(object):
    
    def __init__(self, move_penalty=0, draw_penalty=0):
        self.board = np.zeros(9)
        self.done = False
        self.reward = {"draw_penalty": draw_penalty,
                        "white_win": 1,
                        "black_win": -1,
                        "move_penalty": move_penalty}

    def _is_valid_move(self, action):
        return self.board[action] == 0

    def available_actions(self):
        """actions available to player.
        """
        return [p for p, v in enumerate(self.board) if v == 0]

    def sample(self):
        return random.choice(self.available_actions())
    
    def step(self, action):
        
        if self.done or not self._is_valid_move(action):
            reward = 0
            return self.board, reward, self.done
        
        self.board[action] = 1
        
        if self._is_draw():
            self.done = True
            return self.board, self.reward['draw_penalty'], self.done
        elif self._is_win():
            self.done = True
            return self.board, self.reward['white_win'], self.done
        else:
            move = self.sample()
            self.board[move] = -1

            if self._is_win():
                self.done = True
                return self.board, self.reward['black_win'], self.done
            if self._is_draw():
                self.done = True
                return self.board, self.reward['draw_penalty'], self.done

        # game continues
        return self.board, self.reward['move_penalty'], self.done

    def render(self):
        obs = self.board
        obs = ["X" if (p == 1) else p for p in obs]
        obs = ["O" if (p == -1) else p for p in obs]
        obs = ["-" if (p == 0) else p for p in obs]
        for row in np.array(obs).reshape(3, 3):
            print (row)

    def _is_draw(self):
        """ check if game ended in a draw.
        """
        if (0 not in self.board) and not self._is_win():
            return True
        else:
            return False

    def _is_win(self):
        # check rows
        board = self.board.reshape(3, 3)
        for row in range(3):
            if fabs(np.sum(board[row])) == 3:
                return True

        # check cols
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
