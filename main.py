from graphics import Window
from point import Point
from line import Line
from cell import Cell


def main():
    win = Window(800, 600)

    c = Cell(win)
    c.has_left_wall = False
    c.draw(50, 50, 100, 100)

    c2 = Cell(win)
    c2.has_right_wall = False
    c2.has_left_wall = False
    c2.draw(200, 200, 250, 250)

    c3 = Cell(win)
    c3.has_top_wall = False
    c3.has_right_wall = False
    c3.has_left_wall = False
    c3.draw(300, 300, 350, 350)

    c4 = Cell(win)
    c4.has_bottom_wall = False
    c4.has_top_wall = False
    c4.draw(400, 400, 450, 450)

    c5 = Cell(win)
    c5.draw(300, 100, 350, 150)

    win.wait_for_close()



main()

