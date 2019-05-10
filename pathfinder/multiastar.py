# -*- coding: utf-8 -*-
"""Basic A-star Algorithm
description:
    
content:
    - multiple_a_star_search

author: Shin-Fu (Kelvin) Wu
latest update: 2019/05/10
"""
from astar import a_star_search, reconstruct_path, diagonal_distance

def multiple_a_star_search(graph, segment, heuristic=diagonal_distance, p=0):
    path = []
    for i in range(1, len(segment)):
        start = segment[i-1]
        goal = segment[i]
        came_from, cost_so_far = a_star_search(graph, start, goal, heuristic, p)
        temp_path = reconstruct_path(came_from, start, goal)
        if i != len(segment) - 1:
            path += temp_path[:-1]
        else:
            path += temp_path
    return path