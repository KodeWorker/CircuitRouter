# -*- coding: utf-8 -*-
"""8-direction Grid with Dynamic Bounds
description:
        
content:
    - DynamicBoundGrid
    - DynamicBoundGridWithShortcuts
    
reference:
    1. https://www.geeksforgeeks.org/find-if-there-is-a-path-between-two-vertices-in-a-given-graph/
author: Shin-Fu (Kelvin) Wu
latest update: 
    - 2019/05/14
    - 2019/05/15 calculate search at set_search (reduce A* time) and 
    add DynamicBoundGridWithShortcuts
"""
import os
import sys
root = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(root)

from graph.grid8d import EightDirectionGrid
from shape.Parallelogram import parallelogram_dynamic_bound

class DynamicBoundGrid(EightDirectionGrid):
    def __init__(self, width, height):
        super(DynamicBoundGrid, self).__init__(width, height)
        self.sights = set()
        self.expands = set()
        self.search = set()
        self.outlines = set()
        
    def in_search(self, pos):
        return pos in self.search
    
    def set_search(self, pt1, pt2):
        self.expands.clear()
        self.outlines.clear()
        self.sights = parallelogram_dynamic_bound(pt1, pt2)
        if True:
            self.blocks_in_sights = self.sights & self.walls
            self.sights -= self.blocks_in_sights
            self.expands = self.get_expands()
            self.outlines = self.get_outlines()
        self.search = self.sights | self.outlines
        
    def get_expands(self):
        visited = {}
        
        for block in self.blocks_in_sights:
            
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
        candidates = list(filter(self.in_bounds, candidates))
        candidates = [candidate for candidate in candidates if candidate in self.walls]
        
        return candidates
    
    def get_outlines(self):
        outlines = set()
        for pos in self.expands:
            outlines |= set(self.obstacle_outlines(pos))
        return outlines
    
    def obstacle_outlines(self, pos):
        (x, y) = pos
        if pos in self.walls:
            candidates = self.outline_candidates(pos)
            if (x + y) % 2 == 0: candidates.reverse() # aesthetics
            candidates = list(filter(self.in_bounds, candidates))
            candidates = list(filter(self.passable, candidates))
        else:
            raise ValueError('Current position is not obstacle')
        return candidates
    
    def outline_candidates(self, pos):
        x, y = pos
        candidates = [(x, y+1), (x-1, y  ), (x+1, y), (x, y-1)]
        return candidates
    
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
        candidates = list(filter(self.in_search, candidates))
        candidates = list(filter(self.passable, candidates))
        
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

class DynamicBoundGridWithShortcuts(DynamicBoundGrid):
    def __init__(self, width, height):
        super(DynamicBoundGridWithShortcuts, self).__init__(width, height)
        self.shortcuts = set()
    
    def set_search(self, pt1, pt2):
        self.expands.clear()
        self.outlines.clear()  
        self.shortcuts.clear()
        self.sights = parallelogram_dynamic_bound(pt1, pt2)
        if True:
            self.blocks_in_sights = self.sights & self.walls
            self.sights -= self.blocks_in_sights
            self.expands = self.get_expands()
            self.outlines = self.get_outlines()        
        self.add_shortcuts_in_sights(pt1, pt2)
        
        self.search = self.sights | self.outlines | self.shortcuts
        
    def add_shortcuts_in_sights(self, pt1, pt2):
        outlines_for_shortcut = self.outlines - self.sights
        for outline in outlines_for_shortcut:
            candidates = self.get_candidates(outline)
            candidates = list(filter(self.passable, candidates))
            candidates = set(candidates) - self.outlines
            if len(candidates) >= 4:
                self.shortcuts |= parallelogram_dynamic_bound(pt1, outline) | parallelogram_dynamic_bound(outline, pt2)