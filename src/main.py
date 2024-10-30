from window import *

win = Create_window(800, 600)
point_a = Point(100,150)
point_b = Point(400, 50)
point_c = Point(700, 150)
line = Line(point_a, point_b, point_c)
line2 = Line(Point(700, 150), Point(100, 150), Point(100, 500), Point(700, 500), Point(700, 150))
win.draw_line(line, 'black')
win.draw_line(line2, 'red')
win.wait_for_close()

