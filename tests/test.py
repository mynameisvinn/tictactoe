import unittest
import numpy as np
from Tictactoe import Tictactoe

class TictactoeTest(unittest.TestCase):

    def setUp(self):  # capitalization matters - https://docs.python.org/2/library/unittest.html#unittest.TestCase.setUp
        self.env = Tictactoe()

    def test_draw(self):
        self.env.board = np.array([1,1,1,0,0,0,0,0,0])
        assert self.env._is_win() is True

        self.env.board = np.array([-1,-1,-1,0,0,0,0,0,0])
        assert self.env._is_win() is True

        self.env.board = np.array([1,0,0,1,0,0,1,0,0])
        assert self.env._is_win() is True

        self.env.board = np.array([1,0,0,0,1,0,0,0,1])
        assert self.env._is_win() is True

    def test_available_actions(self):
        self.env.board = np.array([1,0,0,0,0,0,0,0,0])
        actions = self.env.available_actions()
        assert 0 not in actions

        self.env.board = np.array([1,1,1,1,1,1,1,1,0])
        actions = self.env.available_actions()
        assert 8 in actions

    def test_check(self):
        # taking an action in an occupied spot should result 0 rewards
        self.env.board = np.array([1,0,0,0,0,0,0,0,0])
        assert self.env.step(0)[1] == 0
        assert self.env.step(0)[2] == False

    def test_is_win(self):
        pass

if __name__ == "__main__":
    unittest.main()