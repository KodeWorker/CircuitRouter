# -*- coding: utf-8 -*-
"""Parallelogram Shapes
description:
    
content:
    - parallelogram
    - solid_parallelogram

author: Shin-Fu (Kelvin) Wu
latest update: 2019/05/14
"""
from Rectangle import rectangle, solid_rectangle
from Line import bresenhams_line

def parallelogram(pt1, pt2):
    if pt1[1] >= pt2[1]:
        pt1, pt2 = pt2, pt1
        
    dx, dy = abs(pt1[0] - pt2[0]), abs(pt1[1] - pt2[1])
    pixel = set()
    if dx == dy:
        pixel = rectangle(pt1, pt2)
    elif dx > dy:
        pt3 = (pt1[0] + dy, pt2[1])
        pt4 = (pt2[0] - dy, pt1[1])
        l1 = bresenhams_line(pt1, pt3)
        l2 = bresenhams_line(pt3, pt2)
        l3 = bresenhams_line(pt2, pt4)
        l4 = bresenhams_line(pt4, pt1)
        pixel |= l1 | l2 | l3 | l4
    elif dx < dy:
        pt3 = (pt1[0], pt1[1] + dy - dx)
        pt4 = (pt2[0], pt2[1] - dy + dx)
        l1 = bresenhams_line(pt1, pt3)
        l2 = bresenhams_line(pt3, pt2)
        l3 = bresenhams_line(pt2, pt4)
        l4 = bresenhams_line(pt4, pt1)
        pixel |= l1 | l2 | l3 | l4
        
    return pixel

def solid_parallelogram(pt1, pt2):
    if pt1[1] >= pt2[1]:
        pt1, pt2 = pt2, pt1
        
    dx, dy = abs(pt1[0] - pt2[0]), abs(pt1[1] - pt2[1])
    pixel = set()
    if dx == dy:
        pixel = solid_rectangle(pt1, pt2)
    elif dx > dy:
        pt3 = (pt1[0] + dy, pt2[1])
        pt4 = (pt2[0] - dy, pt1[1])
        l2 = bresenhams_line(pt3, pt2, True)
        l4 = bresenhams_line(pt1, pt4, True)
        for s, e in zip(l2, l4):
            pixel |= bresenhams_line(s, e)        
    elif dx < dy:
        pt3 = (pt1[0], pt1[1] + dy - dx)
        pt4 = (pt2[0], pt2[1] - dy + dx)
        l2 = bresenhams_line(pt3, pt2, True)
        l4 = bresenhams_line(pt4, pt1, True)
        for s, e in zip(l2, l4):
            pixel |= bresenhams_line(s, e)
    
    return pixel

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    
#    pt2 = (-1, -1)
#    pt1 = (8, 8)
    
    pt2 = (-1, 15)
    pt1 = (5, -1)
        
    p = parallelogram(pt1, pt2)
    sp = solid_parallelogram(pt1, pt2)
    
    plt.figure()
    plt.title('Parallelogram Shapes')
    for pos in sp:
        plt.scatter(pos[0], pos[1], color='blue')
    for pos in p:
        plt.scatter(pos[0]+0.1, pos[1]+0.1, color='red')
    plt.savefig('parallelogram.png', dpi=200)
    plt.close()
    