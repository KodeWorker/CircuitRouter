# -*- coding: utf-8 -*-
import os
import sys
import time
import matplotlib.pyplot as plt
root = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(root)

from graph.grid8d import EightDirectionGrid
from graph.duality_graph import DualityGraph
from pathfinder.astar import a_star_search
from pathfinder.util import reduce_path, reconstruct_path
from shape.Octagon import solid_octagon
from shape.OctagonLine import solid_octagon_line

if __name__ == '__main__':
    grid = DualityGraph(10000, 10000)
    p = 0.0
    
    grid.walls.add((0, 1))
    grid.walls.add((0, 2))
    grid.walls.add((0, 3))
    grid.walls.add((0, 4))
    
    start, goal = (0, 0), (0, 5)
    
    plt.figure()
    plt.scatter([pos[0] for pos in grid.walls], 
                [pos[1] for pos in grid.walls],
                color='black')
    
    t0 = time.time()
    grid.set_search(start, goal) 
    
    plt.scatter([pos[0] for pos in grid.sights], 
                [pos[1] for pos in grid.sights],
                color='orange')
    
    plt.scatter([pos[0] for pos in grid.outlines], 
                [pos[1] for pos in grid.outlines],
                color='yellow')
    
    plt.scatter([pos[0] for pos in grid.search], 
                [pos[1] for pos in grid.search],
                color='green')
    # vertex
    plt.scatter([pos[0] for pos in grid.vertex.keys()],
                [pos[1] for pos in grid.vertex.keys()], color='blue')
    # edge
    for key in grid.edge.keys():
        pt1, pt2 = key
        plt.plot([pt1[0], pt2[0]], [pt1[1], pt2[1]], color='green')
        
    came_from, cost_so_far = a_star_search(grid, start, goal, p=p)

    path = reconstruct_path(came_from, start, goal)
    path = reduce_path(path)
    for i in range(1, len(path)):
        grid.walls |= solid_octagon_line(path[i-1], path[i], 5)    
    
    

    for i in range(1, len(path)):
        plt.plot([path[i-1][0], path[i][0]],
                 [path[i-1][1], path[i][1]], color='red')