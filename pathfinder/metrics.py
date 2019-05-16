# -*- coding: utf-8 -*-
"""Metrics for distance
description:
    
content:
    - manhattan_distance
    - diagonal_distance
    - euclidean_distance

reference:
    1. http://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html

author: Shin-Fu (Kelvin) Wu
latest update: 
    - 2019/05/16
"""
from math import sqrt

def manhattan_distance(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)
    
def diagonal_distance(a, b, D=1, D2=1):
    """ Diagonal Distance
    In ref. 1, it shows that on a square grid that allows 8 directions of 
    movement, use Diagonal distance.
    """
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])
    return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)

def euclidean_distance(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2) )