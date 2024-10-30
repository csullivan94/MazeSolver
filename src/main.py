from window import *
from cells import *

win = Create_window(800, 600)

for j in range(0, 600, 50):
    for i in range(0, 600, 50):

        cell = Cell(i, i, j, j, win)
        cell.draw()









win.wait_for_close()

