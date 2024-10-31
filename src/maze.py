from tkinter import Tk, BOTH, Canvas
import time
from cells import *

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = self._create_cells()
        self._break_entrance_and_exit()



    def _create_cells(self):

        cells = []
        i = 0
        for row in range(self.num_cols):
            col = self._draw_cell(self.x1 + i, self.y1, self.x1 + self.cell_size_x + i, self.y1 + self.cell_size_y)
            cells.append(col)
            i += self.cell_size_x

        return cells


    def _draw_cell(self, x1, y1, x2, y2):
        cols = []
        i = 0
        for col in range(self.num_rows):
            cell = Cell(x1, (y1 + i), x1 + self.cell_size_x, (y1 + i) + self.cell_size_y, self.win)
            cols.append(cell)
            i += self.cell_size_y
            if self.win is not None:
                cell.draw()
                self._animate()
        return cols

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        if len(self._cells) == 0 or len(self._cells[0]) == 0:
            return
        start = self._cells[0][0]
        start.has_left_wall = False
        if self.win is not None:
            start.draw()
        finish = self._cells[-1][-1]
        finish.has_bottom_wall = False
        if self.win is not None:
            finish.draw()












