from tkinter import Tk, BOTH, Canvas
from window import *
from drawing import *


class Cell:
    def __init__(self, x1, y1, x2, y2, win = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__win = win

    def __repr__(self):
        return f'top corner: ({self.__x1},{self.__y1}), bottom corner: ({self.__x2}, {self.__y2}) '

    def draw(self):
        if self.__win is None:
            return

        left_wall = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
        right_wall = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
        top_wall = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
        bottom_wall = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))


        if self.has_left_wall:
            self.__win.draw_line(left_wall, 'black')
        else:
            self.__win.draw_line(left_wall, 'white')

        if self.has_right_wall:
            self.__win.draw_line(right_wall, 'black')
        else:
            self.__win.draw_line(right_wall, 'white')

        if self.has_top_wall:
            self.__win.draw_line(top_wall, 'black')
        else:
            self.__win.draw_line(top_wall, 'white')

        if self.has_bottom_wall:
            self.__win.draw_line(bottom_wall, 'black')
        else:
            self.__win.draw_line(bottom_wall, 'white')

    def draw_move(self, to_cell, undo=False):
        center = Point((self.__x1+self.__x2)/2, (self.__y1+self.__y2)/2)
        to_center = Point((to_cell.__x1+to_cell.__x2)/2, (to_cell.__y1+to_cell.__y2)/2)
        line = Line(center, to_center)
        if self.__win is None:
            return
        if undo is False:
            self.__win.draw_line(line, 'red')
        else:
            self.__win.draw_line(line, 'gray')

