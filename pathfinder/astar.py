# -*- coding: utf-8 -*-
"""Basic A-star Algorithm
description:
    
content:
    - PriorityQueue
    - manhattan_distance
    - diagonal_distance
    - a_star_algorithm
    - reconstruct_path
    - is_in_path
    - reduce_path

reference:
    1. https://www.redblobgames.com/pathfinding/a-star/implementation.html
    2. http://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html

author: Shin-Fu (Kelvin) Wu
latest update: 2019/05/10
"""
from math import sqrt
from util import PriorityQueue

def manhattan_distance(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)
    
def diagonal_distance(a, b, D=1, D2=1):
    """ Diagonal Distance
    In ref. 2, it shows that on a square grid that allows 8 directions of 
    movement, use Diagonal distance.
    """
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])
    return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)

def euclidean_distance(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2) )

def a_star_search(graph, start, goal, heuristic=diagonal_distance, p=0.0):
    """A-star Search
    This function is the basic A* algorithm with a tie-breaking parameter.
    The default value of p is set to 0 (no tie-breaking). 
    """
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + (1.0 + p)*heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current
                         
    return came_from, cost_so_far
