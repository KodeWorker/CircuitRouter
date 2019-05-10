# -*- coding: utf-8 -*-
""" Unit Test On Multiple A-star algorithm
description:
    This is the unit test for multiple A*.
author: Shin-Fu (Kelvin) Wu
latest update: 2019/05/10
"""
import os
import sys
import unittest

root = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(root)
from graph.grid8d import EightDirectionGrid
from pathfinder.multiastar import multiple_a_star_search 

class TestAstar(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        super(TestAstar, self).__init__(methodName)
        self.g = EightDirectionGrid(4, 4)
        
    def test_case1(self):
        segment = [(0, 0), (1, 2), (3, 3)]
        path = multiple_a_star_search(self.g, segment)
        answer = [(0, 0), (0, 1), (1, 2), (2, 2), (3, 3)]
        self.assertEqual(path, answer)
        
if __name__ == '__main__':
    unittest.main(verbosity=1) 