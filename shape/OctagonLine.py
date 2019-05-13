# -*- coding: utf-8 -*-
"""Octagon Line
description:
    
content:
    - octagon_line
    - solid_octagon_line

author: Shin-Fu (Kelvin) Wu
latest update: 
    - 2019/05/10
    - 2019/05/13
"""
from math import ceil, sqrt
from Octagon import octagon, solid_octagon
from Rectangle import (rectangle, diagonal_rectangle, solid_rectangle,
                       solid_diagonal_rectangle)

def octagon_line(start, goal, r, is_with_start=True, is_with_goal=True):
    pixel = set()
    a = int(ceil(r*sqrt(2)/(2+sqrt(2))))
    r = int(ceil(r))
    
    dx = abs(start[0] - goal[0])
    dy = abs(start[1] - goal[1])
    if dx == dy:
        # Diagonal                
        if start[1] >= goal[1]:
            if start[0] >= goal[0]:
                pt1 = (goal[0] + r, goal[1] - a)
                pt2 = (start[0] - r, start[1] + a)
            else:
                pt1 = (goal[0] - r, goal[1] - a)
                pt2 = (start[0] + r, start[1] + a) 
        else:
            if start[0] >= goal[0]:
                pt1 = (start[0] - r, start[1] - a)
                pt2 = (goal[0] + r, goal[1] + a)
            else:
                pt1 = (start[0] + r, start[1] - a)
                pt2 = (goal[0] - r, goal[1] + a)            
        
        rect = diagonal_rectangle(pt1, pt2)
        pixel |= rect
    elif dx == 0 and dy != 0:
        # Vertical
        pt1y = min(start[1], goal[1])
        pt2y = max(start[1], goal[1])
        rect = rectangle((start[0]-r, pt1y+a), (start[1]+r, pt2y-a))
        pixel |= rect
    elif dy == 0 and dx != 0:        
        # Horizontal
        pt1x = min(start[0], goal[0])
        pt2x = max(start[0], goal[0])
        rect = rectangle((pt1x+a, start[1]-r), (pt2x-a, start[1]+r))
        pixel |= rect
    else:
        raise ValueError("Not a valid line statement")
    
    if is_with_start:
        oct1 = octagon(start[0], start[1], r)
    else:
        oct1 = set()
    if is_with_goal:
        oct2 = octagon(goal[0], goal[1], r)
    else:
        oct2 = set()
    pixel |= oct1 | oct2
    
    return pixel

def solid_octagon_line(start, goal, r, is_with_start=True, is_with_goal=True):
    pixel = set()
    a = int(ceil(r*sqrt(2)/(2+sqrt(2))))
    r = int(ceil(r))
    
    dx = abs(start[0] - goal[0])
    dy = abs(start[1] - goal[1])
    if dx == dy:
        # Diagonal        
        if start[1] >= goal[1]:
            if start[0] >= goal[0]:
                pt1 = (goal[0] + r, goal[1] - a)
                pt2 = (start[0] - r, start[1] + a)
            else:
                pt1 = (goal[0] - r, goal[1] - a)
                pt2 = (start[0] + r, start[1] + a) 
        else:
            if start[0] >= goal[0]:
                pt1 = (start[0] - r, start[1] - a)
                pt2 = (goal[0] + r, goal[1] + a)
            else:
                pt1 = (start[0] + r, start[1] - a)
                pt2 = (goal[0] - r, goal[1] + a)
                
        rect = solid_diagonal_rectangle(pt1, pt2)
        pixel |= rect
    elif dx == 0 and dy != 0:
        # Vertical
        pt1y = min(start[1], goal[1])
        pt2y = max(start[1], goal[1])
        rect = solid_rectangle((start[0]-r, pt1y+a), (start[1]+r, pt2y-a))
        pixel |= rect
    elif dy == 0 and dx != 0:        
        # Horizontal
        pt1x = min(start[0], goal[0])
        pt2x = max(start[0], goal[0])
        rect = solid_rectangle((pt1x+a, start[1]-r), (pt2x-a, start[1]+r))
        pixel |= rect
    else:
        raise ValueError("Not a valid line statement")
    
    if is_with_start:
        oct1 = solid_octagon(start[0], start[1], r)
    else:
        oct1 = set()
    if is_with_goal:
        oct2 = solid_octagon(goal[0], goal[1], r)
    else:
        oct2 = set()
    pixel |= oct1 | oct2
    
    return pixel

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    r=8
    start = (0, 0)
    goal = (30, 0)
    ol1 = octagon_line(start, goal, r)
    start = (0, 0)
    goal = (0, 30)
    ol2 = octagon_line(start, goal, r)    
    start = (0, 0)
    goal = (30, 30)
    ol3 = octagon_line(start, goal, r)
    
    start = (0, 0)
    goal = (30, 0)
    sl1 = solid_octagon_line(start, goal, r)
    start = (0, 0)
    goal = (0, 30)
    sl2 = solid_octagon_line(start, goal, r)    
    start = (0, 0)
    goal = (30, 30)
    sl3 = solid_octagon_line(start, goal, r)
    
    plt.figure()
    plt.title('Octagon Line')
    for pos in sl1:
        plt.scatter(pos[0], pos[1], color='blue')
    for pos in sl2:
        plt.scatter(pos[0], pos[1], color='blue')
    for pos in sl3:
        plt.scatter(pos[0], pos[1], color='blue')
        
    for pos in ol1:
        plt.scatter(pos[0]+0.1, pos[1]+0.1, color='red')
    for pos in ol2:
        plt.scatter(pos[0]+0.1, pos[1]+0.1, color='red')
    for pos in ol3:
        plt.scatter(pos[0]+0.1, pos[1]+0.1, color='red')        
    plt.savefig('octagon_line.png', dpi=200)
    plt.close()
    
    
    