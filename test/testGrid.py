# -*- coding: utf-8 -*-

""" Unit Test On Grid
description:
    This is the unit test for basic grid.
latest update: 2019/05/10
"""
import os
import sys
import unittest

root = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(root)
from graph.grid import GridWithWeights

class TestGrid(unittest.TestCase):
    
    def __init__(self, methodName='runTest'):
        super(TestGrid, self).__init__(methodName)
        self.g1 = GridWithWeights(4, 4)
        self.g2 = GridWithWeights(4, 4)
        
    def test_case1(self):
        self.assertSetEqual(set(self.g1.neighbors((1,1))), set([(0, 1), (2, 1), (1, 0), (1, 2)]))
        self.assertSetEqual(set(self.g1.neighbors((1,0))), set([(0, 0), (1, 1), (2, 0)]))
        self.assertSetEqual(set(self.g1.neighbors((3,3))), set([(3, 2), (2, 3)]))
    
    def test_case2(self):
        self.assertSetEqual(set(self.g2.neighbors((1,1))), set([(0, 1), (2, 1), (1, 0), (1, 2)]))
        self.assertSetEqual(set(self.g2.neighbors((1,0))), set([(0, 0), (1, 1), (2, 0)]))
        self.assertSetEqual(set(self.g2.neighbors((3,3))), set([(3, 2), (2, 3)]))

if __name__ == '__main__':
    unittest.main(verbosity=1)  