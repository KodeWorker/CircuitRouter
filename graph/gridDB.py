# -*- coding: utf-8 -*-
"""8-direction Grid with Dynamic Bounds
description:
    
content:
    - DynamicBoundGrid
    
reference:
    1. https://www.geeksforgeeks.org/find-if-there-is-a-path-between-two-vertices-in-a-given-graph/

author: Shin-Fu (Kelvin) Wu
latest update: 2019/05/14

"""

import os
import sys
#import time
root = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(root)

from grid8d import EightDirectionGrid
from shape.Parallelogram import parallelogram

class DynamicBoundGrid(EightDirectionGrid):
    def __init__(self, width, height):
        super(DynamicBoundGrid, self).__init__(width, height)
        self.sights = set()
        self.expands = set()
        self.outlines = set()
        
    def in_search(self, pos):
        return pos in self.sights | self.outlines
    
    def set_search(self, pt1, pt2):
        self.expands.clear()
        self.outlines.clear()        
        self.sights = parallelogram(pt1, pt2)
#        print(len(self.sights))
#        if not self.is_reachable(pt1, pt2):
        if True:
            # generate expand set
            block_in_sights = self.sights & self.walls
#            self.expands = self.expand_blocks(block_in_sights)
            self.expands = self.get_expands(block_in_sights)
            self.outlines = self.get_outlines()
    
    def get_expands(self, block_in_sights):
        visited = {}            
        for block in block_in_sights:
            
            if visited.get(block, False):
                continue
            
            queue = []            
            queue.append(block)
            visited[block] = True
            
            while queue:
                
                current = queue.pop(0)
                
                if len(self.block_neighbors(current, visited)) == 0:
                    break
                
                for neighbor in self.block_neighbors(current, visited):
                    if visited.get(neighbor, False) == False:
                        queue.append(neighbor)
                        visited[neighbor] = True
                        
        return set(visited.keys())
        
    def block_neighbors(self, pos, visited):
        
        (x, y) = pos
        candidates = self.get_candidates(pos)
        if (x + y) % 2 == 0: candidates.reverse() # aesthetics
        candidates = filter(self.in_bounds, candidates)
        candidates = [candidate for candidate in candidates if candidate in self.walls]
        
        return candidates
    
    def get_outlines(self):
#        t0 = time.time()
        outlines = set()
        for pos in self.expands:
            outlines |= set(self.obstacle_outlines(pos))
#        print("outline time elapsed: {:.4f} sec.".format(time.time() - t0))
        return outlines
    
#    def expand_blocks(self, block_in_sights):
##        t0 = time.time()
#        expand = set()
#        for block in block_in_sights :            
#            if block not in expand:
#                expand |= self.block_expand(block, self.expands)
##        print("expansion time elapsed: {:.4f} sec.".format(time.time() - t0))
#        return expand
#      
#    def block_expand(self, pt, expand=set()):
#        if pt not in expand and pt in self.walls:            
#            expand.add(pt)
#            for candidate in self.get_candidates(pt):
#                self.block_expand(candidate, expand)
#        return expand    
    
    def is_reachable(self, start, end): 
        # Mark all the vertices as not visited 
        visited = {}
   
        # Create a queue for BFS 
        queue=[] 
   
        # Mark the source node as visited and enqueue it 
        queue.append(start) 
        visited[start] = True
   
        while queue: 
  
            #Dequeue a vertex from queue  
            current = queue.pop(0) 
              
            # If this adjacent node is the destination node, 
            # then return true 
            if current == end: 
                 return True
  
            #  Else, continue to do BFS 
            for neighbor in self.neighbors(current): 
                if visited.get(neighbor, False) == False: 
                    queue.append(neighbor) 
                    visited[neighbor] = True
        # If BFS is complete without visited d 
        return False
    
    def get_candidates(self, pos):
        x, y = pos
        candidates = [(x-1, y+1), (x, y+1), (x+1, y+1),
                      (x-1, y  ),           (x+1, y),
                      (x-1, y-1), (x, y-1), (x+1, y-1)]
        return candidates
        
    def neighbors(self, pos):
        (x, y) = pos
        candidates = self.get_candidates(pos)
        if (x + y) % 2 == 0: candidates.reverse() # aesthetics
        candidates = filter(self.in_search, candidates)
        candidates = filter(self.passable, candidates)
        
        pop = set()
        for candidate in candidates:
            if candidate == (x-1, y+1):
                if not self.passable((x-1, y  )) and not self.passable((x, y+1)):
                    pop.add(candidate)
            elif candidate == (x+1, y+1):
                if not self.passable((x+1, y)) and not self.passable((x, y+1)):
                    pop.add(candidate)
            elif candidate == (x-1, y-1):
                if not self.passable((x-1, y  )) and not self.passable((x, y-1)):
                    pop.add(candidate)
            elif candidate == (x+1, y-1):
                if not self.passable((x+1, y)) and not self.passable((x, y-1)):
                    pop.add(candidate)
        for p in pop:
            candidates.remove(p)            
        
        return candidates
    
    def obstacle_outlines(self, pos):
        (x, y) = pos
        if pos in self.walls:
            candidates = self.get_candidates(pos)
            if (x + y) % 2 == 0: candidates.reverse() # aesthetics
            candidates = filter(self.in_bounds, candidates)
            candidates = filter(self.passable, candidates)
        else:
            raise ValueError('Current position is not obstacle')
        return candidates
    
if __name__ == '__main__':
#    import matplotlib.pyplot as plt
    
    grid = DynamicBoundGrid(10000, 10000)
    
    
    for y in range(0 , 3000):
        grid.walls.add((15, y))

    grid.set_search((0, 0), (200, 3000))
    
#    plt.figure()
#    for pos in grid.sights:
#        plt.scatter(pos[0], pos[1], color='orange')
#    for pos in grid.walls:
#        plt.scatter(pos[0], pos[1], color='black')
#    for pos in grid.outlines:
#        plt.scatter(pos[0]+0.1, pos[1]+0.1, color='green')