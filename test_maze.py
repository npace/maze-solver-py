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

    def test_entrance_exit_walls(self):
        maze = Maze(0, 0, 2, 2, 10)

        maze.generate_paths()

        first_cell = maze._cells[0][0]
        last_cell = maze._cells[1][1]
        self.assertEqual(first_cell.has_top_wall, False)
        self.assertEqual(first_cell.has_left_wall, True)
        self.assertEqual(last_cell.has_bottom_wall, False)
        self.assertEqual(last_cell.has_right_wall, True)

    def test_adjacent_cells(self):
        maze = Maze(0, 0, 3, 3, 10)

        adjacent_of_center = maze._adjacent_cells(1, 1)
        self.assertEqual(
            [
                (0, 1),
                (2, 1),
                (1, 0),
                (1, 2),
            ],
            adjacent_of_center,
        )

        adjacent_of_top_left = maze._adjacent_cells(0, 0)
        self.assertEqual(
            [
                (1, 0),
                (0, 1),
            ],
            adjacent_of_top_left,
        )

        adjacent_of_bottom_right = maze._adjacent_cells(2, 2)
        self.assertEqual([(1, 2), (2, 1)], adjacent_of_bottom_right)

    def test_break_wall_between_invalid_indices(self):
        maze = Maze(0, 0, 2, 2, 10)

        with self.assertRaises(IndexError):
            maze._break_walls_between((-1, -1), (3, 3))

        with self.assertRaises(ValueError):
            maze._break_walls_between((1, 1), (1, 1))

    def test_break_walls_between(self):
        maze = Maze(0, 0, 2, 2, 10)
        self._assertWallsBreak(
            maze,
            (0, 0),
            (0, 1),
            lambda c1: c1.has_bottom_wall,
            lambda c2: c2.has_top_wall,
        )

        maze = Maze(0, 0, 2, 2, 10)
        self._assertWallsBreak(
            maze,
            (0, 0),
            (1, 0),
            lambda c1: c1.has_right_wall,
            lambda c2: c2.has_left_wall,
        )

        maze = Maze(0, 0, 2, 2, 10)
        self._assertWallsBreak(
            maze,
            (1, 0),
            (1, 1),
            lambda c1: c1.has_bottom_wall,
            lambda c2: c2.has_top_wall,
        )

        maze = Maze(0, 0, 2, 2, 10)
        self._assertWallsBreak(
            maze,
            (0, 1),
            (1, 1),
            lambda c1: c1.has_right_wall,
            lambda c2: c2.has_left_wall,
        )

    def _assertWallsBreak(self, maze, pos_a, pos_b, get_wall_a, get_wall_b):
        cell_a = maze._cell_at(pos_a)
        cell_b = maze._cell_at(pos_b)
        self.assertEqual(get_wall_a(cell_a), True)
        self.assertEqual(get_wall_b(cell_b), True)

        maze._break_walls_between(pos_a, pos_b)

        self.assertEqual(get_wall_a(cell_a), False)
        self.assertEqual(get_wall_b(cell_b), False)

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
