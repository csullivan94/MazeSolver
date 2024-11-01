from window import *
from cells import *
from maze import *

win = Create_window(850, 850)

maze = Maze(10, 10, 10, 10, 80, 80, win )

maze.solve()





win.wait_for_close()

