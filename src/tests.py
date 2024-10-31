import unittest
from maze import *

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_none(self):
        num_cols = 0
        num_rows = 0
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            0,
        )

    def test_maze_break_start_and_end(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_left_wall,
            False
        )

    def test_find_adjacent_top_left(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1.find_adjacent(0, 0),
            [(1, 0), (0, 1)]
        )

    def test_find_adjacent(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1.find_adjacent(1, 2),
            [(0, 2), (2, 2), (1,1), (1, 3)]
        )

    def test_find_adjacent_bottom_row(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1.find_adjacent(1, 10),
            [(0, 10), (2, 10), (1,9)]
        )

    def test_reset_cells_visited(self):
        m1 = Maze(0, 0, 5, 5, 10, 10)
        for column in m1._cells:
            for cell in column:
                self.assertEqual(
                    cell.visited,
                    False
                )



if __name__ == "__main__":
    unittest.main()
