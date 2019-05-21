# -*- coding: utf-8 -*-
""" Unit Test On Grid
description:
    This is the unit test for basic grid.
content:
    - TestGrid
    - TestGrid8D
author: Shin-Fu (Kelvin) Wu
latest update: 
    - 2019/05/10
    - 2019/05/14 add TestGridDB
    - 2019/05/15 add test_case for DynamicBoundGridWithShortcuts
"""
import os
import sys
import unittest

root = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(root)
from graph.grid import GridWithWeights
from graph.grid8d import EightDirectionGrid
from graph.gridDB import DynamicBoundGrid, DynamicBoundGridWithShortcuts
from graph.duality_graph import DualityGraph

class TestGrid(unittest.TestCase):
    
    def __init__(self, methodName='runTest'):
        super(TestGrid, self).__init__(methodName)
        self.g = GridWithWeights(4, 4)
        
    def test_case1(self):
        self.assertSetEqual(set(self.g.neighbors((1,1))), set([(0, 1), (2, 1), (1, 0), (1, 2)]))
        self.assertSetEqual(set(self.g.neighbors((1,0))), set([(0, 0), (1, 1), (2, 0)]))
        self.assertSetEqual(set(self.g.neighbors((3,3))), set([(3, 2), (2, 3)]))
    
class TestGrid8D(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        super(TestGrid8D, self).__init__(methodName)
        self.g = EightDirectionGrid(4, 4)
    
    def test_case1(self):
        self.assertSetEqual(set(self.g.neighbors((1,1))), set([(2, 0), (1, 0), (0, 0), (2, 1), (0, 1), (2, 2), (1, 2), (0, 2)]))

class TestGridDB(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        super(TestGridDB, self).__init__(methodName)
        self.g1 = DynamicBoundGrid(4, 4)
        self.g1.set_search((0, 0), (3, 3))
        self.g2 = DynamicBoundGridWithShortcuts(4, 4)
        self.g2.set_search((0, 0), (3, 3))
        
    def test_case1(self):
        self.assertSetEqual(set(self.g1.neighbors((0,0))), set([(1, 0), (0, 1), (1, 1)]))
    
    def test_case2(self):
        self.assertSetEqual(set(self.g2.neighbors((0,0))), set([(1, 0), (0, 1), (1, 1)]))

class TestDualityGraph(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        super(TestDualityGraph, self).__init__(methodName)
        self.g1 = DualityGraph(4, 4)
        self.g1.set_search((0, 0), (3, 3))
    
    def test_case1(self):
        self.assertSetEqual(set(self.g1.neighbors((0,0))), set([(3, 0), (0, 3), (3, 3)]))
    
    
if __name__ == '__main__':
    unittest.main(verbosity=1)  