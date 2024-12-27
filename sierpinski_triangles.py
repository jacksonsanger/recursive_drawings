import dudraw

def sierpinski(left: float, bottom: float, right: float, top: float, levels: int)->None:
    if levels == 1:
        dudraw.triangle(left, bottom, right, bottom, left + (right-left)/2, top)
        # dudraw.show()
    else:
        #draw lower left triangle
        sierpinski(left, bottom, left+(right-left)/2, bottom + (top-bottom)/2, levels - 1)
        #draw lower right triangle
        sierpinski(left+(right-left)/2, bottom, right, bottom + (top-bottom)/2, levels - 1)
        #draw upper triangle
        sierpinski(left + (right-left)/4, bottom + (top-bottom)/2, left + 3*(right-left)/4, top, levels - 1)

#main code block
dudraw.set_canvas_size(800,800)
sierpinski(0,0,1,1, 10)
dudraw.show(20000)