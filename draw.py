from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    slope = (y1-y0)/(x0-x1)
    if 0 < slope < 1:
        x = x0
        y = y0
        A = y1 - y0
        B = -(x1 - x0)
        d = 2(A) + B
        while x < x1:
            plot(screen, color, x, y)
            if d > 0:
                y = y + 1
                d = d + 2(B)
            x = x + 1
            d = d + 2(A)
    if 1 < slope:
        x = x0
        y = y0
        A = y1 - y0
        B = -(x1 - x0)
        d = A + 2(B)
        while y < y1:
            plot(screen, color, x, y)
            if d < 0:
                x = x + 1
                d = d + 2(A)
            y = y + 1
            d = d + 2(B)
    if -1 > slope:
        x = x0
        y = y0
        A = y1 - y0
        B = -(x1 - x0)
        d = A + 2(B)
        while y < y1:
            plot(screen, color, x, y)
            if d < 0:
                x = x - 1
                d = d - 2(A)
            y = y + 1
            d = d + 2(B)
    if -1 <  slope < 0:
        x = x0
        y = y0
        A = y1 - y0
        B = -(x1 - x0)
        d = B - 2(A)
        while x > x1:
            plot(screen, color, x, y)
            if d > 0:
                y = y + 1
                d = d + 2(B)
            x = x - 1
            d = d - 2(A)
