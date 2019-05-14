# -*- coding: utf-8 -*-

import os
import sys
import time
import matplotlib.pyplot as plt
root = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(root)

from graph.grid8d import EightDirectionGrid
from graph.gridDB import DynamicBoundGrid
from pathfinder.astar import a_star_search
from pathfinder.util import reduce_path, reconstruct_path
from shape.Octagon import octagon

if __name__ == '__main__':
    grid1 = EightDirectionGrid(10000, 10000)
    grid2 = DynamicBoundGrid(10000, 10000)
    p = 0.5

    for pos in octagon(10, 1000, 25):
        grid1.walls.add(pos)
        grid2.walls.add(pos)
    
    start1, goal1 = (0, 0), (200, 3050)
    start2, goal2 = (10, 0), (200, 3000)
    start3, goal3 = (20, 0), (200, 2950)
    
    t0 = time.time()    
    
    came_from, cost_so_far = a_star_search(grid1, start1, goal1, p=p)
    path = reconstruct_path(came_from, start1, goal1)
    for pos in path:
        grid1.walls.add(pos)
    path1 = reduce_path(path)
    
    came_from, cost_so_far = a_star_search(grid1, start2, goal2, p=p)
    path = reconstruct_path(came_from, start2, goal2)
    for pos in path:
        grid1.walls.add(pos)
    path2 = reduce_path(path)
    
    came_from, cost_so_far = a_star_search(grid1, start3, goal3, p=p)
    path = reconstruct_path(came_from, start3, goal3)
    for pos in path:
        grid1.walls.add(pos)
    path3 = reduce_path(path)
    
    print("Grid 1 Time Elapsed: {:.4f} sec.".format(time.time() - t0))
    
    t0 = time.time()    
    
    grid2.set_search(start1, goal1)
    came_from, cost_so_far = a_star_search(grid2, start1, goal1, p=p)
    path = reconstruct_path(came_from, start1, goal1)
    for pos in path:
        grid2.walls.add(pos)
    path1_ = reduce_path(path)
    
    grid2.set_search(start2, goal2)
    came_from, cost_so_far = a_star_search(grid2, start2, goal2, p=p)
    path = reconstruct_path(came_from, start2, goal2)
    for pos in path:
        grid2.walls.add(pos)
    path2_ = reduce_path(path)
    
    grid2.set_search(start3, goal3)
    came_from, cost_so_far = a_star_search(grid2, start3, goal3, p=p)
    path = reconstruct_path(came_from, start3, goal3)
    for pos in path:
        grid2.walls.add(pos)
    path3_ = reduce_path(path)
    
    print("Grid 2 Time Elapsed: {:.4f} sec.".format(time.time() - t0))
    
    plt.figure()
    for i in range(1, len(path1)):
        plt.plot([path1[i-1][0], path1[i][0]],
                 [path1[i-1][1], path1[i][1]], color='red')
    for i in range(1, len(path2)):
        plt.plot([path2[i-1][0], path2[i][0]],
                 [path2[i-1][1], path2[i][1]], color='red')
    for i in range(1, len(path3)):
        plt.plot([path3[i-1][0], path3[i][0]],
                 [path3[i-1][1], path3[i][1]], color='red')
        
    for i in range(1, len(path1_)):
        plt.plot([path1_[i-1][0]+0.5, path1_[i][0]+0.5],
                 [path1_[i-1][1]+0.5, path1_[i][1]+0.5], color='green')
    for i in range(1, len(path2_)):
        plt.plot([path2_[i-1][0]+0.5, path2_[i][0]+0.5],
                 [path2_[i-1][1]+0.5, path2_[i][1]+0.5], color='green')
    for i in range(1, len(path3_)):
        plt.plot([path3_[i-1][0]+0.5, path3_[i][0]+0.5],
                 [path3_[i-1][1]+0.5, path3_[i][1]+0.5], color='green')