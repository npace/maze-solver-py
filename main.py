from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)

    maze = Maze(12, 18, 26, 19, 30, win)
    maze.generate_paths()
    maze.solve()

    win.wait_for_close()


if __name__ == "__main__":
    main()
