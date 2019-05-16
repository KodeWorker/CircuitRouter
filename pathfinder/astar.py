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
latest update: 
    - 2019/05/10
    - 2019/05/16 reorganized
"""
from pathfinder.util import PriorityQueue
from pathfinder.metrics import diagonal_distance

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
