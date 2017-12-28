# Tictactoe
Game environment for tictactoe, modeled after [Open AI's Gym](https://github.com/openai/gym).

## Example
```python
from Tictactoe import Tictactoe

env = Tictactoe()
a = env.sample()  # get available action
s2, r, d = env.step(a)  # move according to action
```