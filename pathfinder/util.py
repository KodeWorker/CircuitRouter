# -*- coding: utf-8 -*-
"""Utility Functions
description:
    
content:
    - is_in_path
    - reduce_path

author: Shin-Fu (Kelvin) Wu
latest update: 2019/05/13
"""
# -*- coding: utf-8 -*-

def is_in_path(P1, P2, P3):
    """Is in path
    Check if the points are in the same line.
    """
    a = (P2[0] - P1[0]) * (P3[1] - P2[1])
    b = (P2[1] - P1[1]) * (P3[0] - P2[0])    
    if a - b == 0:
        return True
    else:
        return False
    
def reduce_path(path):
    """Reduce Path
    Reduce all the locations in a path into turning points.
    """
    reduced_path = [path[0], path[1]]    
    ind = 2
    while ind < len(path):
        if is_in_path(path[ind], path[ind-1], path[ind-2]):
            reduced_path[-1] = path[ind]
        else:
            reduced_path.append(path[ind])
        ind += 1                            
    if reduced_path[-1] != path[-1]:
        reduced_path.append(path[-1])    
    return reduced_path