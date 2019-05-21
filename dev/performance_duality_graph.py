# -*- coding: utf-8 -*-
import os
import sys
import time
import matplotlib.pyplot as plt
root = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(root)

from graph.grid8d import EightDirectionGrid
from graph.daulity_graph import DualityGraph
from pathfinder.astar import a_star_search
from pathfinder.util import reduce_path, reconstruct_path
from shape.Octagon import solid_octagon
from shape.OctagonLine import solid_octagon_line

if __name__ == '__main__':
    grid1 = EightDirectionGrid(10000, 10000)
    grid2 = DualityGraph(10000, 10000)
    p = 0.0
        
#    for pos in solid_octagon(510, 1000, 20):
#        grid1.walls.add(pos)
#        grid2.walls.add(pos)
        
#    start1, goal1 = (0, 500), (600, 5100)
#    start2, goal2 = (10, 500), (600, 5200)
#    start3, goal3 = (20, 500), (600, 5300)
    
    for pos in solid_octagon_line((550, 500), (550, 5500), 20):
        grid1.walls.add(pos)
        grid2.walls.add(pos)
    
    start1, goal1 = (500, 500), (600, 5100)
    start2, goal2 = (510, 500), (600, 5200)
    start3, goal3 = (520, 500), (600, 5300)
    
    plt.figure()
    plt.scatter([pos[0] for pos in grid2.walls], 
                [pos[1] for pos in grid2.walls],
                color='black')
    
#    t0 = time.time()
#    print('1')
#    came_from, cost_so_far = a_star_search(grid1, start1, goal1, p=p)
#    path = reconstruct_path(came_from, start1, goal1)
#    path1 = reduce_path(path)
#    for i in range(1, len(path1)):
#        grid1.walls |= solid_octagon_line(path1[i-1], path1[i], 5)
#    print('2')
#    came_from, cost_so_far = a_star_search(grid1, start2, goal2, p=p)
#    path = reconstruct_path(came_from, start2, goal2)
#    path2 = reduce_path(path)
#    for i in range(1, len(path2)):
#        grid1.walls |= solid_octagon_line(path2[i-1], path2[i], 5)
#    print('3')
#    came_from, cost_so_far = a_star_search(grid1, start3, goal3, p=p)
#    path = reconstruct_path(came_from, start3, goal3)
#    path3 = reduce_path(path)
#    for i in range(1, len(path3)):
#        grid1.walls |= solid_octagon_line(path3[i-1], path3[i], 5)
#        
#    print("Grid 1 Time Elapsed: {:.4f} sec.".format(time.time() - t0))
    
    t0 = time.time()    
    print('4')
    grid2.set_search(start1, goal1)
    
    t1 = time.time()
    came_from, cost_so_far = a_star_search(grid2, start1, goal1, p=p)
    ts1 = time.time() - t1
    path = reconstruct_path(came_from, start1, goal1)
    path1_ = reduce_path(path)
    for i in range(1, len(path1_)):
        grid2.walls |= solid_octagon_line(path1_[i-1], path1_[i], 5)
    print('5')
    grid2.set_search(start2, goal2)
    t2 = time.time()
    came_from, cost_so_far = a_star_search(grid2, start2, goal2, p=p)
    ts2 = time.time() - t2
    path = reconstruct_path(came_from, start2, goal2)
    path2_ = reduce_path(path)
    for i in range(1, len(path2_)):
        grid2.walls |= solid_octagon_line(path2_[i-1], path2_[i], 5)    
    print('6')
    grid2.set_search(start3, goal3)
    t3 = time.time()
    came_from, cost_so_far = a_star_search(grid2, start3, goal3, p=p)
    ts3 = time.time() - t3
    path = reconstruct_path(came_from, start3, goal3)
    path3_ = reduce_path(path)
    for i in range(1, len(path3_)):
        grid2.walls |= solid_octagon_line(path3_[i-1], path3_[i], 5)
        
    print("Grid 2 Time Elapsed: {:.4f} sec.".format(time.time() - t0))
#    print("Grid 2 Search Time: {:.4f} sec.".format(ts1+ts2+ts3))
    
    plt.scatter([pos[0] for pos in grid2.sights], 
                [pos[1] for pos in grid2.sights],
                color='orange')
    
    plt.scatter([pos[0] for pos in grid2.outlines], 
                [pos[1] for pos in grid2.outlines],
                color='yellow')
    
#    plt.scatter([pos[0] for pos in grid2.search], 
#                [pos[1] for pos in grid2.search],
#                color='orange')
    
#    plt.scatter([pos[0] for pos in grid2.outlines], 
#                [pos[1] for pos in grid2.outlines],
#                color='yellow')
    
#    for i in range(1, len(path1)):
#        plt.plot([path1[i-1][0], path1[i][0]],
#                 [path1[i-1][1], path1[i][1]], color='red')
#    for i in range(1, len(path2)):
#        plt.plot([path2[i-1][0], path2[i][0]],
#                 [path2[i-1][1], path2[i][1]], color='red')
#    for i in range(1, len(path3)):
#        plt.plot([path3[i-1][0], path3[i][0]],
#                 [path3[i-1][1], path3[i][1]], color='red')
    
    # walls
#    plt.scatter([pos[0] for pos in grid2.walls],
#            [pos[1] for pos in grid2.walls], color='black')
    # vertex
    plt.scatter([pos[0] for pos in grid2.vertex.keys()],
                [pos[1] for pos in grid2.vertex.keys()], color='blue')
    # edge
    for key in grid2.edge.keys():
        pt1, pt2 = key
        plt.plot([pt1[0], pt2[0]], [pt1[1], pt2[1]], color='green')
        
    # outlines
#    plt.scatter([p[0] for p in grid2.outlines],
#                [p[1] for p in grid2.outlines], color='orange')
#    plt.scatter([pos[0]+0.1 for pos in grid2.expands],
#                [pos[1]+0.1 for pos in grid2.expands], color='gray')
    
    for i in range(1, len(path1_)):
        plt.plot([path1_[i-1][0], path1_[i][0]],
                 [path1_[i-1][1], path1_[i][1]], color='red')
    for i in range(1, len(path2_)):
        plt.plot([path2_[i-1][0], path2_[i][0]],
                 [path2_[i-1][1], path2_[i][1]], color='red')
    for i in range(1, len(path3_)):
        plt.plot([path3_[i-1][0], path3_[i][0]],
                 [path3_[i-1][1], path3_[i][1]], color='red')