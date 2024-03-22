from graphics import (
    Line,
    Point,
    color_background,
    color_wall,
    color_path,
    color_path_undo,
)


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
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
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
        self.visited = False

    def draw(self):
        self._draw_line(self._top_left, self._bottom_left, self.has_left_wall)
        self._draw_line(self._top_left, self._top_right, self.has_top_wall)
        self._draw_line(self._top_right, self._bottom_right, self.has_right_wall)
        self._draw_line(self._bottom_left, self._bottom_right, self.has_bottom_wall)

    def _draw_line(self, point_a, point_b, draw):
        if self._window:
            color = color_wall
            if not draw:
                color = color_background
            self._window.draw_line(Line(point_a, point_b), color)

    def draw_move(self, to_cell, undo=False):
        if self._window:
            color = color_path
            if undo:
                color = color_path_undo
            self._window.draw_line(Line(self.center, to_cell.center), color)

    def is_above(self, other_cell):
        return self.y2 == other_cell.y1

    def is_left_of(self, other_cell):
        return self.x2 == other_cell.x1

    def is_below(self, other_cell):
        return self.y1 == other_cell.y2

    def is_right_of(self, other_cell):
        return self.x1 == other_cell.x2

    def __repr__(self):
        walls = []
        if self.has_left_wall:
            walls.append("Left")
        if self.has_top_wall:
            walls.append("Top")
        if self.has_right_wall:
            walls.append("Right")
        if self.has_bottom_wall:
            walls.append("Bottom")

        return f"Cell([x1: {self.x1}, y1: {self.y1}], [x2: {self.x2}, y2: {self.y2}]) with walls: [{','.join(walls)}]"
