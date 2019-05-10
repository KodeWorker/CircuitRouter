# -*- coding: utf-8 -*-

def bresenhams_line(start, end, isList=False):
    if isList:
        line = []
    else:
        line = set()
        
    steep = abs(end[1] - start[1]) > abs(end[0] - start[0])
    if steep:
        start = (start[1], start[0])
        end = (end[1], end[0])
    if start[0] > end[0]:
        start, end = end, start
    dx = end[0] - start[0]
    dy = abs(end[1] - start[1])
    error = dx / 2
    y = start[1]
    if start[1] < end[1]:
        step = 1
    else:
        step = -1
        
    for x in range(start[0], end[0]+1):
        if steep:
            if isList:
                line.append((y, x))
            else:
                line.add((y, x))
        else:
            if isList:
                line.append((x, y))
            else:
                line.add((x, y))
        error -= dy
        if error < 0:
            y += step
            error += dx    
    return line