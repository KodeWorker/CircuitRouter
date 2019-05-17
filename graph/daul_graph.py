# -*- coding: utf-8 -*-
"""Duality Graph
description:
        
content:
    - DualGraph
    
reference:
author: Shin-Fu (Kelvin) Wu
latest update: 2019/05/17
"""
import os
import sys
from copy import deepcopy
root = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(root)

from graph.grid8d import EightDirectionGrid
from shape.Parallelogram import parallelogram_dynamic_bound, parallelogram_shortcuts
from pathfinder.metrics import euclidean_distance
from pathfinder.util import is_in_line, is_within_line

class DualGraph(EightDirectionGrid):
    
    def __init__(self, width, height):
        super(DualGraph, self).__init__(width, height)
        self.sights = set()
        self.vertex = {}
        self.edge = {}
    
    def set_search(self, start, end):
        self.start = start
        self.end = end
        
        self.get_sights()
        self.get_block_in_sights()
        self.get_expands()
        
    def get_expands(self):
        self.iso_group = self.get_iso_group()
        self.group_expand()
    
    def group_expand(self):
        self.iso_graph = {}
        for num in self.iso_group.keys():
            group = self.iso_group[num]
            expand = self.bfs_blocks(list(group)[0])
            outline = self.get_outline(expand)
            d
            print(len(outline))
            #!
    
    def get_directed_outline()
    
            
    def get_outline(self, expand):
        outline = set()
        for pos in expand:
            outline |= set(self.obstacle_outlines(pos))
        return outline
    
    def obstacle_outlines(self, pos):
        candidates = self.outline_candidates(pos)
        candidates = list(filter(self.in_bounds, candidates))
        candidates = list(filter(self.passable, candidates))
        return candidates
    
    def outline_candidates(self, pos):
        x, y = pos
        candidates = [(x, y+1), (x-1, y  ), (x+1, y), (x, y-1)]
        return candidates
    
    def bfs_blocks(self, block):
        visited = {}        
        
        queue = []
        queue.append(block)
        visited[block] = True
        
        while queue:
            
            current = queue.pop(0)
            
            if len(self.adjacent_blocks(current, self.walls)) == 0:
                break
            
            for neighbor in self.adjacent_blocks(current, self.walls):
                if visited.get(neighbor, False) == False:
                    queue.append(neighbor)
                    visited[neighbor] = True
                        
        return set(visited.keys())
    
    def get_iso_group(self):
        visited = {pos:False for pos in self.block_in_sights}        
        queue = []
        temp = set()
        
        item = list(self.block_in_sights)[0]
        queue = [item]
        visited[item] = True
        temp.add(item)
        
        groups = {}
        key = 0
        
        while queue:
            current = queue.pop(0)
                        
            if len([pos for pos in set(self.adjacent_blocks(current, self.block_in_sights)) if not visited[pos]]) == 0:
                groups[key] = deepcopy(temp)
                key += 1
                temp.clear()
                try: 
                    item = visited.keys()[visited.values().index(False)]
                    current = item
                    visited[item] = True
                    temp.add(item)
                except:
                    break
            
            for neighbor in set(self.adjacent_blocks(current, self.block_in_sights)):
                if visited[neighbor] == False:
                    queue.append(neighbor)
                    temp.add(neighbor)
                    visited[neighbor] = True
                    
        return groups
    
    def adjacent_blocks(self, pos, blocks):
        candidates = self.get_candidates(pos)
        candidates = list(filter(self.in_bounds, candidates))
        candidates = set(candidates) & blocks
        return candidates
    
    def get_block_in_sights(self):        
        self.block_in_sights = self.sights & self.walls
        
        # duality
        self.merge_nodes = set()
        
        for pos in self.block_in_sights:
            self.merge_nodes |= (set(self.get_candidates(pos)) - self.walls) & self.sights
        self.merge_nodes -= set(self.vertex.keys())
        
        ## new vertex around blocks
        add_edge = deepcopy(self.edge)
        rm_pair = set()
        for node in self.merge_nodes:
            for pair in self.edge.keys():
                if is_in_line(pair[0], node, pair[1]) and \
                is_within_line(pair[0], node, pair[1]):
                    self.vertex[node] = set(pair)
                    self.vertex[pair[0]].add(node) 
                    self.vertex[pair[1]].add(node) 
                    add_edge[(node, pair[0])] = euclidean_distance(node, pair[0])
                    add_edge[(pair[0], node)] = euclidean_distance(node, pair[0])
                    rm_pair.add(pair)
        self.edge = add_edge
        for pair in rm_pair:
            self.remove_edge(pair)
        ## delete blocked vertex
        rm_vertex = set(self.vertex.keys()) & self.block_in_sights
        for vertex in rm_vertex:
            self.remove_vertex(vertex)
        ## delete blocked edge
        rm_pair = set()
        checknodes = self.block_in_sights - set(self.vertex.keys())
        for node in checknodes:
            for pair in self.edge.keys():
                if is_in_line(pair[0], node, pair[1]) and \
                is_within_line(pair[0], node, pair[1]):
                    rm_pair.add(pair)
                    
        for pair in rm_pair:
            self.remove_edge(pair)
                    
    def remove_vertex(self, vertex):
        rm_pair = set()
        for node in self.vertex[vertex]:
            rm_pair.add((vertex, node))
            rm_pair.add((node, vertex))
        for pair in rm_pair:
            self.remove_edge(pair)
        self.vertex.pop(vertex)
    
    def remove_edge(self, pair):
        v1, v2 = pair
        self.edge.pop(pair)
        try:
            self.vertex[v1].remove(v2)
        except:
            pass
        try:
            self.vertex[v2].remove(v1)
        except:
            pass
    
    def get_sights(self):
        self.sights = parallelogram_dynamic_bound(self.start, self.end)
        
        # duality
        if self.start[1] >= self.end[1]:
            pt1, pt2 = self.end, self.start
        else:
            pt1, pt2 = self.start, self.end
            
        dx, dy = abs(pt1[0] - pt2[0]), abs(pt1[1] - pt2[1])
        if dx == dy:
            v1 = pt1
            v2 = (pt1[0], pt1[1] + dy)
            v3 = pt2
            v4 = (pt2[0], pt2[1] - dy)            
        elif dx > dy:
            v1 = pt1
            v2 = (pt2[0] - dx, pt2[1])
            v3 = pt2
            v4 = (pt1[0] + dx, pt1[1])
        elif dx < dy:
            v1 = pt1
            v2 = (pt1[0], pt2[1] - dx)
            v3 = pt2
            v4 = (pt2[0], pt1[1] + dx)
        self.vertex[v1] = set([v2, v4])
        self.vertex[v2] = set([v1, v3])
        self.vertex[v3] = set([v2, v4])
        self.vertex[v4] = set([v3, v1])
        
        for v1 in self.vertex.keys():
            for v2 in self.vertex[v1]:
                self.edge[(v1, v2)] = euclidean_distance(v1, v2)
    
    def get_candidates(self, pos):
        x, y = pos
        candidates = [(x-1, y+1), (x, y+1), (x+1, y+1),
                      (x-1, y  ),           (x+1, y),
                      (x-1, y-1), (x, y-1), (x+1, y-1)]
        return candidates
    
if __name__ == '__main__':
    import matplotlib.pyplot as plt
    
    dg = DualGraph(1000, 1000)
    
    for x in range(9, 12):
        for y in range(4, 7):
            dg.walls.add((x, y))  
    
    for x in range(13, 16):
        dg.walls.add((x, 4))
    dg.walls.add((13, 5))
    
#    dg.set_search((10, 0), (13, 8))
    dg.set_search((10, 0), (13, 15))
    
    plt.figure()
    # walls
    plt.scatter([p[0] for p in dg.walls],
                [p[1] for p in dg.walls], color='black')
    # vertex
    plt.scatter([p[0] for p in dg.vertex.keys()],
                [p[1] for p in dg.vertex.keys()], color='blue')
    # edge
    for key in dg.edge.keys():
        pt1, pt2 = key
        plt.plot([pt1[0], pt2[0]], [pt1[1], pt2[1]], color='green')