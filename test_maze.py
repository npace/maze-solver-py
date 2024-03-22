import unittest

from maze import Maze


class MazeTest(unittest.TestCase):
    def test_maze_cells(self):
        cols = 12
        rows = 10
        maze = Maze(0, 0, rows, cols, 10)

        self.assertEqual(len(maze._cells), rows)
        for i in range(rows):
            self.assertEqual(len(maze._cells[i]), cols)

    def test_invalid_constructor_input(self):
        with self.assertRaises(ValueError):
            Maze(0, 0, 1, 10, 10)
        with self.assertRaises(ValueError):
            Maze(0, 0, 10, 1, 10)
        with self.assertRaises(ValueError):
            Maze(0, 0, 10, 10, 0)

    def test_cell_positions(self):
        cols = 3
        rows = 3
        maze = Maze(10, 10, rows, cols, 10)

        self._assertCellPosition(maze._cells[0][0], 10, 10, 20, 20)
        self._assertCellPosition(maze._cells[0][1], 10, 20, 20, 30)
        self._assertCellPosition(maze._cells[0][2], 10, 30, 20, 40)
        self._assertCellPosition(maze._cells[1][0], 20, 10, 30, 20)
        self._assertCellPosition(maze._cells[1][1], 20, 20, 30, 30)
        self._assertCellPosition(maze._cells[1][2], 20, 30, 30, 40)
        self._assertCellPosition(maze._cells[2][0], 30, 10, 40, 20)
        self._assertCellPosition(maze._cells[2][1], 30, 20, 40, 30)
        self._assertCellPosition(maze._cells[2][2], 30, 30, 40, 40)

    def _assertCellPosition(self, cell, x1, y1, x2, y2):
        self.assertEqual(cell.x1, x1)
        self.assertEqual(cell.y1, y1)
        self.assertEqual(cell.x2, x2)
        self.assertEqual(cell.y2, y2)
