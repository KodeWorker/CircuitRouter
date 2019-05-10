# -*- coding: utf-8 -*-
""" Unit Test On A-star algorithm
description:
    This is the unit test for basic A*.
latest update: 2019/05/10
"""
import os
import sys
import unittest

root = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(root)
from graph.grid import GridWithWeights
from pathfinder.astar import a_star_search, reconstruct_path 

class TestAstar(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        super(TestAstar, self).__init__(methodName)
        self.g1 = GridWithWeights(4, 4)
        
    def test_case1(self):
        start = (0, 0)
        goal = (3, 3)
        came_from, cost_so_far = a_star_search(self.g1, start, goal)
        path  = reconstruct_path(came_from, start, goal)
        answer = [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 3), (3, 3)]
        self.assertEqual(path, answer)

if __name__ == '__main__':
    unittest.main(verbosity=1) 