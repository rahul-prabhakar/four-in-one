import sys

from game import MazeGame
from snake.snake import SnakeGame

if (sys.argv[1] == 'snake'):
        snake = SnakeGame()
        snake.on_execute()
elif sys.argv[1] == 'maze':
        maze = MazeGame()
        maze.on_execute()