# -*- coding: utf-8 -*-
from math import ceil

def putpixel(x, y, pixel):
    pixel.add((int(ceil(x)), int(ceil(y))))

def drawCircle(xc, yc, x, y, pixel):
    putpixel(xc+x, yc+y, pixel)
    putpixel(xc-x, yc+y, pixel)
    putpixel(xc+x, yc-y, pixel)
    putpixel(xc-x, yc-y, pixel)
    putpixel(xc+y, yc+x, pixel)
    putpixel(xc-y, yc+x, pixel)
    putpixel(xc+y, yc-x, pixel)
    putpixel(xc-y, yc-x, pixel)
    
def bresenhams_circle(xc, yc, r):
    x = r
    y = 0
    dx = 1 - 2*r
    dy = 1
    de = 0
    pixel = set()
    while x >= y:
        drawCircle(xc, yc, x, y, pixel)
        y += 1
        de += dy
        dy += 2
        if (2 * de + dx > 0):
            x -= 1
            de += dx
            dy += 2    
    return pixel