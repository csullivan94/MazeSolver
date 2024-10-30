from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, *args):
        self.points = args


    def draw(self, canvas, fill_colour):
        points = []
        for point in self.points:
            points.append(point.x)
            points.append(point.y)
        canvas.create_line(*points, fill=fill_colour, width=3)
