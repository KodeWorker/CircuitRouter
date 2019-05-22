# -*- coding: utf-8 -*-
"""Basic A-star Algorithm
description:
    
content:
    - multiple_a_star_search

author: Shin-Fu (Kelvin) Wu
latest update: 
    - 2019/05/10
    - 2019/05/14 add support for DynamicBoundGrid
    - 2019/05/22 add support for DenseGraph and DualityGraph
"""
import os
import sys
root = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(root)

from graph.gridDB import DynamicBoundGrid, DynamicBoundGridWithShortcuts
from graph.transform import DenseGraph
from graph.duality_graph import DualityGraph
from pathfinder.astar import a_star_search, diagonal_distance
from pathfinder.util import reconstruct_path

SUPPORT_SET = set([DynamicBoundGrid, DynamicBoundGridWithShortcuts, DenseGraph,
                   DualityGraph])

def multiple_a_star_search(graph, segment, heuristic=diagonal_distance, p=0):
    path = []
    for i in range(1, len(segment)):
        start = segment[i-1]
        goal = segment[i]
        if type(graph) in SUPPORT_SET:
            graph.set_search(start, goal)
        came_from, cost_so_far = a_star_search(graph, start, goal, heuristic, p)
        temp_path = reconstruct_path(came_from, start, goal)
        if i != len(segment) - 1:
            path += temp_path[:-1]
        else:
            path += temp_path
    return path