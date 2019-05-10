# -*- coding: utf-8 -*-
"""Octagon Shapes
description:
    
content:
    - putpixel
    - octagon
    - solid_octagon

author: Shin-Fu (Kelvin) Wu
latest update: 2019/05/10
"""
from math import ceil, sqrt
from Circle import putpixel

def octagon(xc, yc, r):
    
    a = int(ceil(r*sqrt(2)/(2+sqrt(2))))
    r = int(ceil(r))    
    pixel = set()
    
    for x in range(xc-a, xc+a+1):
        putpixel(x, yc-r, pixel)
        putpixel(x, yc+r, pixel)

    for y in range(yc-a, yc+a+1):
        putpixel(xc-r, y, pixel)
        putpixel(xc+r, y, pixel)
    
    x, y = xc+a, yc-r
    while (x != xc+r and y!= yc-a):
        putpixel(x, y, pixel)
        x+=1
        y+=1
        
    x, y = xc+a, yc+r
    while (x != xc+r and y!= yc+a):
        putpixel(x, y, pixel)
        x+=1
        y-=1
    
    x, y = xc-a, yc-r
    while (x != xc-r and y!= yc-a):
        putpixel(x, y, pixel)
        x-=1
        y+=1
        
    x, y = xc-a, yc+r
    while (x != xc-r and y!= yc+a):
        putpixel(x, y, pixel)
        x-=1
        y-=1
    
    return pixel

def solid_octagon(xc, yc, r):
    
    a = int(ceil(r*sqrt(2)/(2+sqrt(2))))
    r = int(ceil(r))    
    pixel = set()
    
    for x in range(xc-a, xc+a+1):
        for y in range(yc-r, yc+r+1):
            putpixel(x, y, pixel)

    for y in range(yc-a, yc+a+1):
        for x in range(xc-r, xc+r+1):
            putpixel(x, y, pixel)
    
    x, y = xc+a, yc-r
    while (x != xc+r and y!= yc-a):
        for yy in range(y, yc-a+1):
            putpixel(x, yy, pixel)
        x+=1
        y+=1
        
    x, y = xc+a, yc+r
    while (x != xc+r and y!= yc+a):
        for yy in range(yc+a, y+1):
            putpixel(x, yy, pixel)
        x+=1
        y-=1
    
    x, y = xc-a, yc-r
    while (x != xc-r and y!= yc-a):
        for yy in range(y, yc-a+1):
            putpixel(x, yy, pixel)
        x-=1
        y+=1
        
    x, y = xc-a, yc+r
    while (x != xc-r and y!= yc+a):
        for yy in range(yc+a, y+1):
            putpixel(x, yy, pixel)
        x-=1
        y-=1
    
    return pixel

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    r=10
    s = solid_octagon(0, 0, r)
    o = octagon(0, 0, r)
    plt.figure()
    plt.title('Octagon Shapes')
    for pos in s:
        plt.scatter(pos[0], pos[1], color='blue')
    for pos in o:
        plt.scatter(pos[0]+0.1, pos[1]+0.1, color='red')
    plt.savefig('octagon.png', dpi=200)
    plt.close()
    