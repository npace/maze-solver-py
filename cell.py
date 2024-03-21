from graphics import Window, Line, Point


class Cell:
    def __init__(
        self,
        x1,
        x2,
        y1,
        y2,
        window,
        has_left_wall=True,
        has_right_wall=True,
        has_top_wall=True,
        has_bottom_wall=True,
    ) -> None:
        self._top_left = Point(x1, y1)
        self._bottom_left = Point(x1, y2)
        self._top_right = Point(x2, y1)
        self._bottom_right = Point(x2, y2)
        self.center = Point((x1 + x2) / 2, (y1 + y2) / 2)
        self._window = window
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall

    def draw(self):
        if self.has_left_wall:
            self._draw_line(self._top_left, self._bottom_left)
        if self.has_top_wall:
            self._draw_line(self._top_left, self._top_right)
        if self.has_right_wall:
            self._draw_line(self._top_right, self._bottom_right)
        if self.has_bottom_wall:
            self._draw_line(self._bottom_left, self._bottom_right)

    def _draw_line(self, point_a, point_b):
        self._window.draw_line(Line(point_a, point_b), "black")

    def draw_move(self, to_cell, undo=False):
        if undo:
            color = "grey"
        else:
            color = "red"
        self._window.draw_line(Line(self.center, to_cell.center), color)
