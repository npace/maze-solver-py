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
        self.__top_left = Point(x1, y1)
        self.__bottom_left = Point(x1, y2)
        self.__top_right = Point(x2, y1)
        self.__bottom_right = Point(x2, y2)
        self.center = Point((x1 + x2) / 2, (y1 + y2) / 2)
        self.__window = window
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall

    def draw(self):
        if self.has_left_wall:
            self.__draw_line(self.__top_left, self.__bottom_left)
        if self.has_top_wall:
            self.__draw_line(self.__top_left, self.__top_right)
        if self.has_right_wall:
            self.__draw_line(self.__top_right, self.__bottom_right)
        if self.has_bottom_wall:
            self.__draw_line(self.__bottom_left, self.__bottom_right)

    def __draw_line(self, point_a, point_b):
        self.__window.draw_line(Line(point_a, point_b), "black")

    def draw_move(self, to_cell, undo=False):
        if undo:
            color = "grey"
        else:
            color = "red"
        self.__window.draw_line(Line(self.center, to_cell.center), color)
