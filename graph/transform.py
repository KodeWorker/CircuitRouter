# -*- coding: utf-8 -*-
"""Graph Transformation
description:
        
content:
    - DenseGraph
    
reference:
    
author: Shin-Fu (Kelvin) Wu
latest update: 2019/05/16
"""
from copy import deepcopy
from graph.gridDB import DynamicBoundGrid, DynamicBoundGridWithShortcuts
from pathfinder.util import is_in_line
from pathfinder.metrics import euclidean_distance

class DenseGraph(object):

    def __init__(self, graph):
        if type(graph) != DynamicBoundGrid and \
        type(graph) != DynamicBoundGridWithShortcuts:
            raise TypeError("{} may not be supported".format(type(graph)))
        self.graph = graph
            
    def constract(self):
        self.vertex = self.get_vertex()
        self.edge = self.get_edge()
    
    def get_edge(self):
        edge = {}
        for v1 in self.vertex.keys():
            for v2 in self.vertex[v1]:
                d = euclidean_distance(v1, v2)
                edge[(v1, v2)] = d
                edge[(v2, v1)] = d
        return edge
    
    def get_vertex(self):
        
        queue = []
        visited = {}
        came_from = {} 
        go_to = {}
        
        queue.append(self.graph.start)
        visited[self.graph.start] = True   
        
        while queue:
            
            current = queue.pop(0)            
            
            if len(self.graph.neighbors(current)) == 0:
                break
            
            go_to[current] = set([neighbor for neighbor in self.graph.neighbors(current)])
                                          
            for neighbor in self.graph.neighbors(current):
                if visited.get(neighbor, False) == False:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    cfrom = came_from.get(neighbor, set())
                    cfrom.add(current)
                    came_from[neighbor] = cfrom
        
        vertex = deepcopy(go_to)
        for current in go_to.keys():
            if len(vertex[current]) == 2:
                v1, v2 = list(vertex[current])[0], list(vertex[current])[1]
                if is_in_line(v1, current, v2):
                    vertex[v1].remove(current)
                    vertex[v1].add(v2)
                    vertex[v2].remove(current)
                    vertex[v2].add(v1)
                    vertex.pop(current) 
            elif len(vertex[current]) == 1:
                v = list(vertex[current])[0]
                vertex[v].remove(current)
                vertex.pop(current) 
                
        return vertex
    
    def neighbors(self, pos):
        return self.vertex[pos]
    
    def cost(self, from_node, to_node):
        return self.edge[(from_node, to_node)]
                    
    def set_search(self, start, end):
        self.graph.set_search(start, end)
        self.constract()
        
if __name__ == '__main__':
    
    grid = DynamicBoundGridWithShortcuts(500, 500)    
    
    start, end = ((0,0), (5, 12))
    graph = DenseGraph(grid)
    graph.set_search(start, end)
    