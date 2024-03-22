from tkinter import Tk, BOTH, Canvas, IntVar, BooleanVar

color_background = "#323232"
color_wall = "black"
color_path = "red"
color_path_undo = "grey"


class Window:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

        self._root = Tk()
        self._root.title("Maze Solver")
        self._root.protocol("WM_DELETE_WINDOW", self.close)

        self._canvas = Canvas(
            master=self._root, height=height, width=width, background=color_background
        )
        self._canvas.pack()

        self._running = BooleanVar(self._root, False)

    def draw_line(self, line, fill_color):
        line.draw(self._canvas, fill_color)

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def pause(self, time):
        ms = int(time * 1000)
        var = IntVar(self._root)
        self._root.after(ms, lambda: var.set(1))
        self._root.wait_variable(var)

    def wait_for_close(self):
        self._running.set(True)
        self._root.wait_variable(self._running)

    def close(self):
        self._running.set(False)


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_a, point_b) -> None:
        self.point_a = point_a
        self.point_b = point_b

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point_a.x,
            self.point_a.y,
            self.point_b.x,
            self.point_b.y,
            fill=fill_color,
            width=2,
        )
        canvas.pack()
