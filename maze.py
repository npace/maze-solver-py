from cell import Cell


class Maze:
    def __init__(self, x, y, num_rows, num_cols, cell_size, win=None) -> None:
        if num_rows < 2:
            raise ValueError("Maze needs at least 2 rows")
        if num_cols < 2:
            raise ValueError("Maze needs at least 2 columns")
        if cell_size < 1:
            raise ValueError("Maze cell size must be at least 1")
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

        self._break_entrance_and_exit()

        if self._win:
            for column in cells:
                for cell in column:
                    self._draw_cell(cell)

    def _break_entrance_and_exit(self):
        first_cell = self._cells[0][0]
        last_cell = self._cells[len(self._cells) - 1][len(self._cells[0]) - 1]
        first_cell.has_top_wall = False
        last_cell.has_bottom_wall = False

    def _draw_cell(self, cell):
        cell.draw()
        self._win.redraw()
        self._win.pause(0.025)
