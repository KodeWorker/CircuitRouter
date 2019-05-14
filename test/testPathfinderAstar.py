# -*- coding: utf-8 -*-
""" Unit Test On A-star algorithm
description:
    This is the unit test for A* algorithms.
content:
    - TestAstar
    - TestMAstar
author: Shin-Fu (Kelvin) Wu
latest update: 
    - 2019/05/10
    - 2019/05/14 add test cases for DynamicBoundGrid
"""
import os
import sys
import unittest

root = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(root)
from graph.grid import GridWithWeights
from graph.grid8d import EightDirectionGrid
from graph.gridDB import DynamicBoundGrid
from pathfinder.astar import a_star_search
from pathfinder.multiastar import multiple_a_star_search
from pathfinder.util import reconstruct_path

class TestAstar(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        super(TestAstar, self).__init__(methodName)
        self.g1 = GridWithWeights(4, 4)
        self.g2 = EightDirectionGrid(4, 4)
        self.g3 = DynamicBoundGrid(4, 4)
        
    def test_case1(self):
        start = (0, 0)
        goal = (3, 3)
        came_from, cost_so_far = a_star_search(self.g1, start, goal)
        path  = reconstruct_path(came_from, start, goal)
        answer = [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 3), (3, 3)]
        self.assertEqual(path, answer)

    def test_case2(self):
        start = (0, 0)
        goal = (3, 3)
        came_from, cost_so_far = a_star_search(self.g2, start, goal)
        path  = reconstruct_path(came_from, start, goal)
        answer = [(0, 0), (1, 1), (2, 2), (3, 3)]
        self.assertEqual(path, answer)
    
    def test_case3(self):
        start = (0, 0)
        goal = (3, 3)
        self.g3.set_search(start, goal)
        came_from, cost_so_far = a_star_search(self.g3, start, goal)
        path  = reconstruct_path(came_from, start, goal)
        answer = [(0, 0), (1, 1), (2, 2), (3, 3)]
        self.assertEqual(path, answer)

class TestMAstar(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        super(TestMAstar, self).__init__(methodName)
        self.g1 = GridWithWeights(4, 4)
        self.g2 = EightDirectionGrid(4, 4)
        self.g3 = DynamicBoundGrid(4, 4)
    
    def test_case1(self):
        segment = [(0, 0), (1, 2), (3, 3)]
        path = multiple_a_star_search(self.g1, segment)
        answer = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (3, 3)]
        self.assertEqual(path, answer)
    
    def test_case2(self):
        segment = [(0, 0), (1, 2), (3, 3)]
        path = multiple_a_star_search(self.g2, segment)
        answer = [(0, 0), (0, 1), (1, 2), (2, 2), (3, 3)]
        self.assertEqual(path, answer)
    
    def test_case3(self):
        segment = [(0, 0), (1, 2), (3, 3)]
        path = multiple_a_star_search(self.g3, segment)
        answer = [(0, 0), (0, 1), (1, 2), (2, 2), (3, 3)]
        self.assertEqual(path, answer)
    

if __name__ == '__main__':
    unittest.main(verbosity=1) 