# -*- coding: utf-8 -*-
""" Unit Test On Pathfinder Utility Functions
description:
    This is the unit test for pathfinder utility functions.
content:
    - TestUtil
author: Shin-Fu (Kelvin) Wu
latest update: 2019/05/13
"""
import os
import sys
import unittest

root = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(root)
from pathfinder.util import reduce_path

class TestUtil(unittest.TestCase):
    
    def __init__(self, methodName='runTest'):
        super(TestUtil, self).__init__(methodName)
        
    def test_case1(self):
        path = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 3), (5, 3), (6, 4), (7, 5)]
        reduced_path = reduce_path(path)
        answer = [(0, 0), (3, 3), (5, 3), (7, 5)]
        self.assertEqual(reduced_path, answer)

if __name__ == '__main__':
    unittest.main(verbosity=1)