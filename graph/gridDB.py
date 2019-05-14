# -*- coding: utf-8 -*-
"""8-direction Grid with Dynamic Bounds
description:
    
content:
    - DynamicBoundGrid

author: Shin-Fu (Kelvin) Wu
latest update: 2019/05/14

"""

import os
import sys
root = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(root)

from grid8d import EightDirectionGrid
from shape.Parallelogram import solid_parallelogram

class DynamicBoundGrid(EightDirectionGrid):
    def __init__(self, width, height):
        super(DynamicBoundGrid, self).__init__(width, height)
        self.sight = set()
        self.outlines = set()
        
    def in_search(self, pos):
        return pos in self.sights | self.outlines
    
    def set_search(self, pt1, pt2):
        self.sights = solid_parallelogram(pt1, pt2)
        if self.is_sight_blocked(pt1, pt2):
            # generate expand set
            block_in_sights = self.sights & self.walls
            expand = self.expand_blocks(block_in_sights)
            self.outlines = self.get_outlines(expand)
    
    def get_outlines(self, expand):
        outlines = set()
        for pos in expand:
            outlines |= set(self.obstacle_outlines(pos))
        return outlines
    
    def expand_blocks(self, block_in_sights):        
        expand = set()
        for block in block_in_sights :
            if block not in expand:
                expand |= self.block_expand(block)
        return expand
        
    def is_sight_blocked(self, pt1, pt2):
        flood = self.flood_fill(pt1)
        return pt2 not in flood
    
    def block_expand(self, pt, expand=set()):
        if pt not in expand and pt in self.walls:
            expand.add(pt)
            for candidate in self.get_candidates(pt):
                self.block_expand(candidate, expand)
        return expand
    
    def flood_fill(self, pt, flood=set()):
        if pt not in flood and pt not in self.walls:
            flood.add(pt)
            for neighbor in self.neighbors(pt):
                self.flood_fill(neighbor, flood)
        return flood
    
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
    import matplotlib.pyplot as plt
    
    grid = DynamicBoundGrid(100, 100)
    
    grid.walls.add((2,4))
    grid.walls.add((2,3))
    grid.walls.add((2,2))
    grid.walls.add((2,1))
    
    grid.walls.add((0,2))
    
    grid.set_search((0, 0), (3, 5))
    
    plt.figure()
    for pos in grid.sights:
        plt.scatter(pos[0], pos[1], color='orange')
    for pos in grid.walls:
        plt.scatter(pos[0], pos[1], color='black')
    for pos in grid.outlines:
        plt.scatter(pos[0]+0.1, pos[1]+0.1, color='green')