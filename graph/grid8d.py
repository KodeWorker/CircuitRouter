# -*- coding: utf-8 -*-
"""8-direction Grid
description:
    
content:
    - EightDirectionGrid

author: Shin-Fu (Kelvin) Wu
latest update: 
    - 2019/05/10
    - 2019/05/14 update cost function
"""
from math import sqrt
from grid import GridWithWeights

class EightDirectionGrid(GridWithWeights):
    def __init__(self, width, height):
        super(EightDirectionGrid, self).__init__(width, height)
    
    def cost(self, from_node, to_node):
        return self.weights.get(to_node, sqrt(pow((from_node[0] - to_node[0]), 2) + pow((from_node[1] - to_node[1]), 2)))
    
    def neighbors(self, id):
        (x, y) = id
        results = [(x-1, y+1), (x, y+1), (x+1, y+1),
                   (x-1, y  ),           (x+1, y),
                   (x-1, y-1), (x, y-1), (x+1, y-1)]
        if (x + y) % 2 == 0: results.reverse() # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        
        pop = []
        for result in results:
            if result == (x-1, y+1):
                if not self.passable((x-1, y  )) and not self.passable((x, y+1)):
                    pop.append(result)
            elif result == (x+1, y+1):
                if not self.passable((x+1, y)) and not self.passable((x, y+1)):
                    pop.append(result)
            elif result == (x-1, y-1):
                if not self.passable((x-1, y  )) and not self.passable((x, y-1)):
                    pop.append(result)
            elif result == (x+1, y-1):
                if not self.passable((x+1, y)) and not self.passable((x, y-1)):
                    pop.append(result)
        for p in pop:
            results.remove(p)            
        
        return results