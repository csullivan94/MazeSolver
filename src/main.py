from window import *
from cells import *

win = Create_window(800, 600)

cell1 = Cell(0, 0, 50, 50, win)
cell2 = Cell(100, 100, 150, 150, win)

cell1.draw()
cell2.draw()

cell1.draw_move(cell2)








win.wait_for_close()

