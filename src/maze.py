from tkinter import Tk, BOTH, Canvas
import time
from cells import *
import random


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None, seed = None):
        if seed is None:
            random.seed()
        else:
            random.seed(seed)
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = self._create_cells()
        if len(self._cells) > 0:
            self._break_entrance_and_exit()
            self.visited_cells = self._break_walls_r(0,0)
            self._reset_cells_visited()




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

    def _break_walls_r(self, cell_position_col, cell_position_row):

        current = (cell_position_col, cell_position_row)
        self._cells[cell_position_col][cell_position_row].visited = True
        while True:
            to_visit = []
            adjacent_cells = self.find_adjacent(cell_position_col, cell_position_row)
            possible_cells = []
            for cell in adjacent_cells:
                if cell not in to_visit and self._cells[cell[0]][cell[1]].visited is False:
                    possible_cells.append(cell)
            if len(possible_cells) == 0:
                break
            next_cell = random.choice(possible_cells)
            self.break_wall(current[0], current[1], next_cell[0], next_cell[1])
            if self.win is not None:
                self._animate()
            self._break_walls_r(next_cell[0], next_cell[1])



    def break_wall(self, cur_col, cur_row, next_col, next_row):
        if cur_col == next_col:
            if cur_row < next_row:
                self._cells[cur_col][cur_row].has_bottom_wall = False
                self._cells[next_col][next_row].has_top_wall = False
            if cur_row > next_row:
                self._cells[cur_col][cur_row].has_top_wall = False
                self._cells[next_col][next_row].has_bottom_wall = False
        elif cur_col < next_col:
            self._cells[cur_col][cur_row].has_right_wall = False
            self._cells[next_col][next_row].has_left_wall = False
        else:
            self._cells[cur_col][cur_row].has_left_wall = False
            self._cells[next_col][next_row].has_right_wall = False
        if self.win is not None:
            self._cells[cur_col][cur_row].draw()
            self._cells[next_col][next_row].draw()

    def find_adjacent(self, cell_position_col, cell_position_row):
        adjacent_cells = []

        if cell_position_col > 0:
            adjacent_cells.append((cell_position_col - 1, cell_position_row))
        if cell_position_col < self.num_cols -1:
                adjacent_cells.append((cell_position_col + 1, cell_position_row))
        if cell_position_row > 0:
            adjacent_cells.append((cell_position_col, cell_position_row - 1))
        if cell_position_row < self.num_rows - 1:
            adjacent_cells.append((cell_position_col, cell_position_row + 1))

        return adjacent_cells

    def _reset_cells_visited(self):
        for column in self._cells:
            for cell in column:
                cell.visited = False

    def solve(self):
        pass


    def _solve_r(self, cur_col, cur_row):
        pass










