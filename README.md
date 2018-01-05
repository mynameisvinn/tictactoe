# Tictactoe
Game environment for tictactoe, modeled after [Open AI's Gym](https://github.com/openai/gym).

It is a simple toy model to explore policy gradients, value networks, and minimax. 

## Example
```python
from Tictactoe import Tictactoe

env = Tictactoe()
a = env.sample()  # get available action
s2, r, d = env.step(a)  # move according to action
```
You can visualize board state with render():
```python
env.render()

['X' '-' 'O']
['O' 'X' 'X']
['-' 'O' '-']
```
