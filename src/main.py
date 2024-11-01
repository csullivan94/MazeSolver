from window import *
from cells import *
from maze import *

win = Create_window(800, 600)

maze = Maze(10, 10, 6, 6, 80, 80, win, 0)

maze.solve()





win.wait_for_close()

