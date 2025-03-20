from line import Line
from point import Point

class Cell():
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = None
        self.__x2 = None
        self.__y1 = None
        self.__y2 = None
        self.__win = win


    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        if self.has_left_wall:
            left_line = Line(Point(x1, y1), Point(x1, y2))
            self.__win.draw_line(left_line)
        if self.has_top_wall:
            top_line = Line(Point(x1, y1), Point(x2, y1))
            self.__win.draw_line(top_line)
        if self.has_right_wall:
            right_line = Line(Point(x2, y1), Point(x2, y2))
            self.__win.draw_line(right_line)
        if self.has_bottom_wall:
            bottom_line = Line(Point(x1, y2), Point(x2, y2))
            self.__win.draw_line(bottom_line)

    def get_center(self):
        center_x = self.__x1 + (self.__x2 - self.__x1) / 2
        center_y = self.__y1 + (self.__y2 - self.__y) / 2
        #returns the x and y coordinates of the center of the cell
        return Point(center_x,center_y)

    def draw_move(self, to_cell, undo=False):
        #get cell center as Point
        center = self.get_center()
        
        #create the line as a variable
        line = Line(center, to_cell.get_center())
        if undo==False:
            #draw red line
            self.__win.draw_line(line, "red")
            

        else:
            #draw gray line
            self.__win.draw_line(line, "gray")