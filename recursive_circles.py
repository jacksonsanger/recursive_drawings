import dudraw

def draw_circles(x: float, y: float, r: float, n: int)->None:
    if n == 0:
        return
    else:
        draw_circles(x + r, y, r/2, n-1)
        draw_circles(x -r, y, r/2, n-1)
        draw_circles(x, y + r, r/2, n-1)
        draw_circles(x, y -r, r/2, n-1)
        dudraw.circle(x, y, r)
        # dudraw.show(500)

draw_circles(0.5, 0.5, 0.2, 6)
dudraw.show(200000)