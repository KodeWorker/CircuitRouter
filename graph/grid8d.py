# -*- coding: utf-8 -*-
"""8-direction Grid
description:
    
content:
    - EightDirectionGrid

author: Shin-Fu (Kelvin) Wu
latest update: 2019/05/10

"""
from grid import GridWithWeights

class EightDirectionGrid(GridWithWeights):
    def __init__(self, width, height):
        super(EightDirectionGrid, self).__init__(width, height)
    
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