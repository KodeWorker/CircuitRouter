# -*- coding: utf-8 -*-
"""Utility Functions
description:
    
content:
    - PriorityQueue
    - reconstruct_path
    - is_within_line
    - is_in_path
    - reduce_path

author: Shin-Fu (Kelvin) Wu
latest update: 
    - 2019/05/13
    - 2019/05/14 reorganized
    - 2019/05/17 add is_within_line
"""
# -*- coding: utf-8 -*-
import heapq

class PriorityQueue(object):
    def __init__(self):
        """ Queue with priority
        In ref. 1, it shows the reason why using a prioty queue to store the costs 
        of calculated vertices.
        """
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]

def reconstruct_path(came_from, start, goal):
    """Reconstruct Path
    Reconstruct a path from search result.
    """
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]        
    path.append(start) # optional
    path.reverse() # optional
    return path

def is_within_line(P1, P2, P3):
    if P1[0]<=P2[0]<=P3[0] and P1[1]<=P2[1]<=P3[1]:
        return True
    elif P3[0]<=P2[0]<=P1[0] and P3[1]<=P2[1]<=P1[1]:
        return True
    else:
        return False

  
def is_in_line(P1, P2, P3):
    """Is in line
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
        if is_in_line(path[ind], path[ind-1], path[ind-2]):
            reduced_path[-1] = path[ind]
        else:
            reduced_path.append(path[ind])
        ind += 1                            
    if reduced_path[-1] != path[-1]:
        reduced_path.append(path[-1])    
    return reduced_path