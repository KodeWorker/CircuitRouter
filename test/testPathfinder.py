# -*- coding: utf-8 -*-
""" Unit Test On A-star algorithm
description:
    This is the unit test for A* algorithms.
content:
    - TestAstar
    - TestMAstar
    - TestUtil
    - TestMetrics
author: Shin-Fu (Kelvin) Wu
latest update: 
    - 2019/05/10
    - 2019/05/14 add test cases for DynamicBoundGrid
    - 2019/05/22 merge testPathfinderUtil.py, add TestMetrics, add test cases
    for transform and DualityGraph
"""
import os
import sys
import unittest
from math import sqrt

root = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(root)
from graph.grid import GridWithWeights
from graph.grid8d import EightDirectionGrid
from graph.gridDB import DynamicBoundGrid, DynamicBoundGridWithShortcuts
from graph.transform import DenseGraph
from graph.duality_graph import DualityGraph
from pathfinder.astar import a_star_search
from pathfinder.multiastar import multiple_a_star_search
from pathfinder.util import reconstruct_path
from pathfinder.util import reduce_path
from pathfinder.metrics import (manhattan_distance, euclidean_distance, 
                                diagonal_distance)

class TestAstar(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        super(TestAstar, self).__init__(methodName)
        self.g1 = GridWithWeights(4, 4)
        self.g2 = EightDirectionGrid(4, 4)
        self.g3 = DynamicBoundGrid(4, 4)
        self.g4 = DynamicBoundGridWithShortcuts(4, 4)
        self.g5 = DenseGraph(self.g4)
        self.g6 = DualityGraph(4, 4)
        
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
    
    def test_case4(self):
        start = (0, 0)
        goal = (3, 3)
        self.g4.set_search(start, goal)
        came_from, cost_so_far = a_star_search(self.g4, start, goal)
        path  = reconstruct_path(came_from, start, goal)
        answer = [(0, 0), (1, 1), (2, 2), (3, 3)]
        self.assertEqual(path, answer)
    
    def test_case5(self):
        start = (0, 0)
        goal = (3, 3)
        self.g5.set_search(start, goal)
        came_from, cost_so_far = a_star_search(self.g5, start, goal)
        path  = reconstruct_path(came_from, start, goal)
        answer = [(0, 0), (1, 1), (2, 2), (3, 3)]
        self.assertEqual(path, answer)
    
    def test_case6(self):
        start = (0, 0)
        goal = (3, 3)
        self.g6.set_search(start, goal)
        came_from, cost_so_far = a_star_search(self.g6, start, goal)
        path  = reconstruct_path(came_from, start, goal)
        answer = [(0, 0), (3, 3)]
        self.assertEqual(path, answer)
    
class TestMAstar(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        super(TestMAstar, self).__init__(methodName)
        self.g1 = GridWithWeights(4, 4)
        self.g2 = EightDirectionGrid(4, 4)
        self.g3 = DynamicBoundGrid(4, 4)
        self.g4 = DynamicBoundGridWithShortcuts(4, 4)
        self.g5 = DenseGraph(self.g4)
        self.g6 = DualityGraph(4, 4)
        
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
    
    def test_case4(self):
        segment = [(0, 0), (1, 2), (3, 3)]
        path = multiple_a_star_search(self.g4, segment)
        answer = [(0, 0), (0, 1), (1, 2), (2, 2), (3, 3)]
        self.assertEqual(path, answer)
    
    def test_case5(self):
        segment = [(0, 0), (1, 2), (3, 3)]
        path = multiple_a_star_search(self.g5, segment)
        answer = [(0, 0), (0, 1), (1, 2), (2, 2), (3, 3)]
        self.assertEqual(path, answer)
    
    def test_case6(self):
        segment = [(0, 0), (1, 2), (3, 3)]
        path = multiple_a_star_search(self.g6, segment)
        answer = [(0, 0), (0, 1), (1, 2), (2, 2), (3, 3)]
        self.assertEqual(path, answer)

class TestUtil(unittest.TestCase):
    
    def __init__(self, methodName='runTest'):
        super(TestUtil, self).__init__(methodName)
        
    def test_case1(self):
        path = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 3), (5, 3), (6, 4), (7, 5)]
        reduced_path = reduce_path(path)
        answer = [(0, 0), (3, 3), (5, 3), (7, 5)]
        self.assertEqual(reduced_path, answer)

class TestMetrics(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        super(TestMetrics, self).__init__(methodName)
        
    def test_case1(self):
        start = (0, 0)
        end = (5, 3)
        
        distance = manhattan_distance(start, end)
        self.assertEqual(distance, 8)
    
    def test_case2(self):
        start = (0, 0)
        end = (5, 3)
        
        distance = euclidean_distance(start, end)
        self.assertEqual(distance, sqrt(pow(5, 2) + pow(3, 2)))
    
    def test_case3(self):
        start = (0, 0)
        end = (5, 3)
        
        distance = diagonal_distance(start, end)
        self.assertEqual(distance, 5)

if __name__ == '__main__':
    unittest.main(verbosity=1) 