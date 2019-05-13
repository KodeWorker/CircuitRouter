# -*- coding: utf-8 -*-
"""Rectangle Shapes
description:
    
content:
    - rectangle    
    - solid_rectangle
    - diagonal_rectangle
    - solid_diagonal_rectangle

author: Shin-Fu (Kelvin) Wu
latest update: 2019/05/10
"""
from math import ceil
from Line import bresenhams_line

def rectangle(lb, tr):
    pixel = set()
    
    for x in range(int(ceil(lb[0])), int(ceil(tr[0]))+1):
        pixel.add((x, int(ceil(lb[1]))))
        pixel.add((x, int(ceil(tr[1]))))
    
    for y in range(int(ceil(lb[1])), int(ceil(tr[1]))+1):
        pixel.add((int(ceil(lb[0])), y))
        pixel.add((int(ceil(tr[0])), y))
    
    return pixel

def solid_rectangle(lb, tr):
    pixel = set()
    
    for x in range(int(ceil(lb[0])), int(ceil(tr[0]))+1):
        for y in range(int(ceil(lb[1])), int(ceil(tr[1]))+1):
            pixel.add((x, y))
    
    return pixel

def diagonal_rectangle(lpt, tpt):
    pixel = set()
    dx = abs(lpt[0] - tpt[0])
    dy = abs(lpt[1] - tpt[1])
    a = float(dy - dx) / 2
    if tpt[0] - lpt[0] >= 0:
        p1 = lpt
        p2 = (lpt[0]+int(ceil(dx+a)), lpt[1]+int(ceil(dx+a)))
        p3 = tpt
        p4 = (tpt[0]-int(ceil(dx+a)), tpt[1]-int(ceil(dx+a)))
        l1 = bresenhams_line(p1, p2)
        l2 = bresenhams_line(p2, p3)
        l3 = bresenhams_line(p3, p4)
        l4 = bresenhams_line(p4, p1)
        pixel |= l1 | l2 | l3 | l4
    else:
        p1 = lpt
        p2 = (lpt[0]-int(ceil(dx+a)), lpt[1]+int(ceil(dx+a)))
        p3 = tpt
        p4 = (tpt[0]+int(ceil(dx+a)), tpt[1]-int(ceil(dx+a)))
        l1 = bresenhams_line(p1, p2)
        l2 = bresenhams_line(p2, p3)
        l3 = bresenhams_line(p3, p4)
        l4 = bresenhams_line(p4, p1)
        pixel |= l1 | l2 | l3 | l4
    return pixel

def solid_diagonal_rectangle(lpt, tpt):
    pixel = set()
    dx = abs(lpt[0] - tpt[0])
    dy = abs(lpt[1] - tpt[1])
    a = float(dy - dx) / 2
    if tpt[0] - lpt[0] >= 0:
        p1 = lpt
        p11 = (p1[0], p1[1]+1)
        p2 = (lpt[0]+int(ceil(dx+a)), lpt[1]+int(ceil(dx+a)))
        p22 = (p2[0]-1, p2[1])
        p3 = tpt
        p33 = (p3[0], p3[1]-1)
        p4 = (tpt[0]-int(ceil(dx+a)), tpt[1]-int(ceil(dx+a)))
        p44 = (p4[0]+1, p4[1])
        
        l1 = bresenhams_line(p1, p2, True)
        l2 = bresenhams_line(p4, p3, True)
        l11 = bresenhams_line(p11, p22, True)
        l22 = bresenhams_line(p44, p33, True)
        
        for s, g in zip(l1, l2):
            pixel |= bresenhams_line(s, g)
        for s, g in zip(l11, l22):
            pixel |= bresenhams_line(s, g)
            
    else:
        p1 = lpt
        p11 = (p1[0], p1[1]+1)
        p2 = (lpt[0]-int(ceil(dx+a)), lpt[1]+int(ceil(dx+a)))
        p22 = (p2[0]+1, p2[1])
        p3 = tpt
        p33 = (p3[0], p3[1]-1)
        p4 = (tpt[0]+int(ceil(dx+a)), tpt[1]-int(ceil(dx+a)))
        p44 = (p4[0]-1, p4[1])
        
        l1 = bresenhams_line(p1, p2, True)
        l2 = bresenhams_line(p4, p3, True)
        l11 = bresenhams_line(p11, p22, True)
        l22 = bresenhams_line(p44, p33, True)
        
        for s, g in zip(l1, l2):
            pixel |= bresenhams_line(s, g)
        for s, g in zip(l11, l22):
            pixel |= bresenhams_line(s, g)    
    return pixel
   
if __name__ == '__main__':
    import matplotlib.pyplot as plt
    
    rect = rectangle((-3,-2), (4, 6))
    s = solid_rectangle((-3,-2), (4, 6))        
    plt.figure()
    plt.title('Rectangle Shapes')
    for pos in s:
        plt.scatter(pos[0], pos[1], color='blue')
    for pos in rect:
        plt.scatter(pos[0]+0.1, pos[1]+0.1, color='red')
    plt.savefig('rectangle.png', dpi=200)
    plt.close()
            
    rect = diagonal_rectangle((0,0), (0, 40))
    s = solid_diagonal_rectangle((0,0), (0, 40))
    plt.figure()
    plt.title('Diagonal Rectangle Shapes')
    for pos in s:
        plt.scatter(pos[0], pos[1], color='blue')
    for pos in rect:
        plt.scatter(pos[0]+0.1, pos[1]+0.1, color='red')
    plt.savefig('diagonal_rectangle.png', dpi=200)
    plt.close()
    