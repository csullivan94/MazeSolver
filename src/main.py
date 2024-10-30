from window import *

win = Create_window(800, 600)
point_a = Point(0,0)
point_b = Point(800, 600)
line = Line(point_a, point_b)
win.draw_line(line, 'black')
win.wait_for_close()


