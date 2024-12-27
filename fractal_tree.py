import dudraw
from random import random
from math import cos, sin, radians

def end_point(start_x:float, start_y:float, length:float, angle:float):
    end_x = start_x + length * cos(radians(angle))
    end_y = start_y + length * sin(radians(angle))
    return (end_x, end_y)

def draw_recursive_tree(x: float, y: float, length: float,thickness: float, angle: float, n: int):
    end = end_point(x, y, length, angle)
    if n == 0:
        dudraw.set_pen_color_rgb(241, 156, 187)
        dudraw.filled_circle(end[0], end[1], length/3)
    else:
        dudraw.set_pen_width(thickness)
        dudraw.set_pen_color_rgb(175, 110, 77) #brown
        dudraw.line(x, y, end[0], end[1])
        draw_recursive_tree(end[0], end[1], length * (0.6 + random() * 0.4 - 0.2), thickness * 0.73, angle + 45 + random()*25, n -1)
        draw_recursive_tree(end[0], end[1], length * (0.6 + random() * 0.4 - 0.2), thickness * 0.73, angle - 45 - random()*25, n - 1)
        draw_recursive_tree(end[0], end[1], length * (0.6 + random() * 0.4 - 0.2), thickness * 0.73, angle + 60 + random()*25, n - 1)
        draw_recursive_tree(end[0], end[1], length * (0.6 + random() * 0.4 - 0.2), thickness * 0.73, angle - 60 - random()*25, n - 1)
draw_recursive_tree(0.5, 0, 0.25, 0.0175, 90, 8)
dudraw.show(float('inf'))