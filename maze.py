from cell import Cell
import random


class Maze:
    def __init__(
        self, x, y, num_rows, num_cols, cell_size, win=None, seed=None
    ) -> None:
        if num_rows < 2:
            raise ValueError("Maze needs at least 2 rows")
        if num_cols < 2:
            raise ValueError("Maze needs at least 2 columns")
        if cell_size < 1:
            raise ValueError("Maze cell size must be at least 1")

        random.seed(seed)

        self._x = x
        self._y = y
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size = cell_size
        self._win = win
        self._create_cells()

    def _create_cells(self):
        cells = []
        self._cells = cells
        x = self._x
        y = self._y
        size = self._cell_size
        for _ in range(self._num_rows):
            column = []
            for _ in range(self._num_cols):
                cell = Cell(x, x + size, y, y + size, self._win)
                column.append(cell)
                y += size
            cells.append(column)
            x += size
            y = self._y

        for column in cells:
            for cell in column:
                self._draw_cell(cell)

    def generate_paths(self):
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    def _break_entrance_and_exit(self):
        first_cell = self._cells[0][0]
        last_cell = self._cells[len(self._cells) - 1][len(self._cells[0]) - 1]
        first_cell.has_top_wall = False
        last_cell.has_bottom_wall = False
        self._draw_cell(first_cell)
        self._draw_cell(last_cell)

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            to_visit = []
            for cell_indices in self._adjacent_cells(i, j):
                if not self._cell_at(cell_indices).visited:
                    to_visit.append(cell_indices)
            if len(to_visit) == 0:
                self._draw_cell(current_cell)
                return
            next_cell_pos = random.choice(to_visit)
            next_i = next_cell_pos[0]
            next_j = next_cell_pos[1]
            self._break_walls_between((i, j), next_cell_pos)
            self._break_walls_r(next_i, next_j)

    def _cell_at(self, cell_pos):
        return self._cells[cell_pos[0]][cell_pos[1]]

    def _break_walls_between(self, cell_a_pos, cell_b_pos):
        cell_a = self._cell_at(cell_a_pos)
        cell_b = self._cell_at(cell_b_pos)
        if cell_a.y2 == cell_b.y1:
            cell_a.has_bottom_wall = False
            cell_b.has_top_wall = False
        elif cell_a.x2 == cell_b.x1:
            cell_a.has_right_wall = False
            cell_b.has_left_wall = False
        elif cell_a.y1 == cell_b.y2:
            cell_a.has_top_wall = False
            cell_b.has_bottom_wall = False
        elif cell_a.x1 == cell_b.x2:
            cell_a.has_left_wall = False
            cell_b.has_right_wall = False
        else:
            raise ValueError(
                f"Couldn't break walls between\n{cell_a} at {cell_a_pos} and\n{cell_b} at {cell_b_pos}"
            )

    def _adjacent_cells(self, i, j):
        adjacent_cells = []
        if i > 0:
            adjacent_cells.append((i - 1, j))
        if i < len(self._cells) - 1:
            adjacent_cells.append((i + 1, j))
        if j > 0:
            adjacent_cells.append((i, j - 1))
        if j < len(self._cells[0]) - 1:
            adjacent_cells.append((i, j + 1))
        return adjacent_cells

    def _draw_cell(self, cell):
        if self._win:
            cell.draw()
            self._win.redraw()
            self._win.pause(0.005)
