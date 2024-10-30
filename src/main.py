from window import *
from cells import *

win = Create_window(800, 600)

cell = Cell(0, 0, 50, 50 , win)
cell.draw()

win.wait_for_close()

