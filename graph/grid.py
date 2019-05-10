# -*- coding: utf-8 -*-
"""Basic Grid
description:
    
content:
    - SquareGrid
    - GridWithWeights

reference:
    1. https://www.redblobgames.com/pathfinding/a-star/implementation.html

author: Shin-Fu (Kelvin) Wu
latest update: 2019/05/10

"""
class SquareGrid(object):
    def __init__(self, width, height):
        """ Square Grid
        
        """
        self.width = width
        self.height = height
        self.walls = set()
    
    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height
    
    def passable(self, id):
        return id not in self.walls
    
    def neighbors(self, id):
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x + y) % 2 == 0: results.reverse() # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results

class GridWithWeights(SquareGrid):
    def __init__(self, width, height):
        """ Square Grid with Weights
        
        """
        super(GridWithWeights, self).__init__(width, height)
        self.weights = {}
    
    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)