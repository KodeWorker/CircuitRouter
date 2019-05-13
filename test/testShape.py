# -*- coding: utf-8 -*-
""" Unit Test On Shapes
description:
    This is the unit test for shapess.
content:
    - TestLine
    - TestCircle
    - TestOctagon
    - TestRectangle
    - TestOctagonLine
author: Shin-Fu (Kelvin) Wu
latest update: 2019/05/13
"""

import os
import sys
import unittest

root = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(root)
from shape.Line import bresenhams_line
from shape.Circle import bresenhams_circle
from shape.Octagon import octagon, solid_octagon
from shape.Rectangle import (rectangle, solid_rectangle, diagonal_rectangle,
                             solid_diagonal_rectangle)
from shape.OctagonLine import octagon_line, solid_octagon_line

class TestLine(unittest.TestCase):
    
    def __init__(self, methodName='runTest'):
        super(TestLine, self).__init__(methodName)
        
    def test_case1(self):
        start = (0, 0)
        end = (4, 3)
        line = bresenhams_line(start, end)
        answer = set([(4, 3), (3, 2), (0, 0), (1, 1), (2, 1)])
        self.assertEqual(line, answer)

class TestCircle(unittest.TestCase):
    
    def __init__(self, methodName='runTest'):
        super(TestCircle, self).__init__(methodName)
        
    def test_case1(self):
        xc, yc, r = 0, 0, 4
        circle = bresenhams_circle(xc, yc, r)
        answer = set([(-2, 3), (3, 2), (-4, -1), (-3, -2), (-4, 0), (2, -3), 
                      (1, 4), (-1, -4), (-2, -3), (-4, 1), (3, -2), (1, -4), 
                      (0, 4), (2, 3), (-1, 4), (4, 0), (4, 1), (4, -1), 
                      (-3, 2), (0, -4)])
        self.assertEqual(circle, answer)

class TestOctagon(unittest.TestCase):
    
    def __init__(self, methodName='runTest'):
        super(TestOctagon, self).__init__(methodName)
    
    def test_case1(self):
        xc, yc, r = 0, 0, 4
        o = octagon(xc, yc , r)
        answer = set([(2, -4), (-3, 3), (-1, 4), (-4, 2), (3, -3), (4, -1),
                      (4, 0), (3, 3), (-2, -4), (4, -2), (0, 4), (-3, -3), 
                      (4, 1), (0, -4), (1, 4), (1, -4), (-4, 0), (4, 2), 
                      (-4, -1), (-4, -2), (-1, -4), (-4, 1), (-2, 4), (2, 4)])
        self.assertEqual(o, answer)
    
    def test_case2(self):
        xc, yc, r = 0, 0, 4
        so = solid_octagon(xc, yc , r)
        answer = set([(2, -1), (1, 3), (-2, 0), (-3, -2), (2, -3), (-4, 0),
                      (-2, 4), (-2, -3), (-4, 2), (0, 0), (3, -1), (2, -2),
                      (4, 2), (0, 3), (2, 0), (1, -2), (4, -2), (-1, 0), 
                      (1, 2), (-2, 3), (-2, 1), (3, 1), (3, 3), (-2, -4),
                      (1, -1), (2, -4), (3, 0), (4, -1), (-3, -1), (-3, 2),
                      (-3, -3), (-1, -1), (1, -3), (4, 0), (4, 1), (1, 1),
                      (0, -4), (3, 2), (-1, 2), (3, -3), (2, 2), (-1, -2),
                      (-2, 2), (-1, 1), (1, 4), (-2, -1), (-3, 1), (2, 1),
                      (2, 3), (-1, -3), (1, -4), (-1, 4), (0, 4), (1, 0),
                      (0, -3), (-4, -1), (0, 1), (-4, -2), (-1, 3), (0, -1),
                      (-2, -2), (3, -2), (2, 4), (-1, -4), (-3, 3), (-3, 0),
                      (-4, 1), (0, -2), (0, 2)])
        self.assertEqual(so, answer)

class TestRectangle(unittest.TestCase):
    
    def __init__(self, methodName='runTest'):
        super(TestRectangle, self).__init__(methodName)
    
    def test_case1(self):
        lb, tr = (-1, -2), (2, 2)
        rect = rectangle(lb, tr)
        answer = set([(1, 2), (-1, 1), (2, -2), (-1, 0), (-1, -1), (-1, 2), 
                      (2, 2), (2, 1), (2, 0), (2, -1), (-1, -2), (0, -2), 
                      (1, -2), (0, 2)])
        self.assertEqual(rect, answer)
    
    def test_case2(self):
        lb, tr = (-1, -2), (2, 2)
        rect = solid_rectangle(lb, tr)
        answer = set([(0, 1), (0, -1), (-1, 1), (0, 0), (-1, 0), (2, -1),
                      (1, -1), (-1, 2), (1, 2), (-1, -2), (2, 1), (1, 1), 
                      (2, 0), (2, -2), (-1, -1), (0, -2), (1, 0), (1, -2),
                      (0, 2), (2, 2)])
        self.assertEqual(rect, answer)
    
    def test_case3(self):
        lpt, tpt = (-1, -1), (2, 3)
        rect = diagonal_rectangle(lpt, tpt)
        answer = set([(0, 1), (1, 2), (0, 0), (3, 3), (-1, -1), (2, 2), (2, 3),
                      (-2, -1), (1, 1), (-1, 0)])
        self.assertEqual(rect, answer)
    
    def test_case4(self):
        lpt, tpt = (-1, -1), (2, 3)
        rect = solid_diagonal_rectangle(lpt, tpt)
        answer = set([(0, 1), (1, 2), (0, 0), (-1, 0), (2, 2), (-1, -1), 
                      (2, 3), (-2, -1), (1, 1), (3, 3)])
        self.assertEqual(rect, answer)

class TestOctagonLine(unittest.TestCase):
    
    def __init__(self, methodName='runTest'):
        super(TestOctagonLine, self).__init__(methodName)

    def test_case1(self):
        start = (0, 0)
        end = (8, 8)
        r = 2
        ol = octagon_line(start, end, r)
        answer = set([(6, 9), (-2, 0), (3, 0), (4, 7), (2, 1), (0, 3), (8, 5),
                      (2, 5), (5, 8), (1, 2), (10, 8), (-2, 1), (6, 7), 
                      (10, 7), (1, -2), (7, 6), (8, 10), (6, 3), (3, 6), 
                      (-2, -1), (8, 6), (4, 1), (10, 9), (-1, 2), (7, 10), 
                      (2, -1), (1, 4), (9, 10), (8, 7), (1, 0), (9, 6), (0, 1),
                      (6, 8), (5, 2), (-1, -2), (7, 4), (2, 0), (0, -2), 
                      (7, 8), (0, 2)])
        self.assertEqual(ol, answer)
    
    def test_case2(self):
        start = (0, 0)
        end = (8, 8)
        r = 2
        sl = solid_octagon_line(start, end, r)
        answer = set([(6, 9), (1, 3), (-1, 0), (3, 0), (9, 8), (2, 5), (8, 5),
                      (5, 8), (-2, 0), (10, 8), (6, 7), (5, 5), (10, 7), 
                      (7, 6), (8, 10), (7, 9), (1, 1), (3, 2), (7, 10), (4, 5),
                      (-1, -2), (-2, -1), (1, 4), (7, 5), (2, 3), (8, 7), 
                      (4, 2), (9, 6), (6, 5), (5, 3), (0, 1), (6, 8), (3, 1), 
                      (-1, -1), (7, 8), (2, 4), (4, 7), (6, 6), (5, 6), (7, 7), 
                      (2, 1), (1, -2), (8, 9), (0, 0), (0, 3), (1, 2), (-2, 1), 
                      (3, 3), (1, -1), (4, 4), (6, 3), (3, 6), (2, 2), (8, 6), 
                      (4, 1), (10, 9), (9, 7), (6, 4), (5, 4), (2, -1), 
                      (-1, 2), (-1, 1), (9, 9), (9, 10), (0, -1), (1, 0), 
                      (3, 5), (4, 6), (3, 4), (5, 7), (7, 4), (2, 0), (8, 8), 
                      (4, 3), (0, -2), (5, 2), (0, 2)])
        self.assertEqual(sl, answer)
        
if __name__ == '__main__':
    unittest.main(verbosity=1)  