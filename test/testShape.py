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
    - TestParallelogram
author: Shin-Fu (Kelvin) Wu
latest update: 
    - 2019/05/13
    - 2019/05/14 add TestParallelogram
    - 2019/05/22 add test case for parallelogram_shortcuts and parallelogram_shortcut_graph
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
from shape.Parallelogram import (parallelogram, solid_parallelogram,
                                 parallelogram_dynamic_bound,
                                 parallelogram_shortcuts,
                                 parallelogram_shortcut_graph)

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

class TestParallelogram(unittest.TestCase):
    
    def __init__(self, methodName='runTest'):
        super(TestParallelogram, self).__init__(methodName)
        
    def test_case1(self):
        pt1 = (-1, -1)
        pt2 = (5, 2)
        p = parallelogram(pt1, pt2)
        answer = set([(3, 2), (0, 0), (3, 0), (1, -1), (2, -1), (-1, -1), 
                      (4, 2), (4, 1), (2, 2), (0, -1), (5, 2), (1, 1)])
        self.assertEqual(p, answer)
    
    def test_case2(self):
        pt1 = (-1, -1)
        pt2 = (5, 2)
        sp = solid_parallelogram(pt1, pt2)
        answer = set([(3, 2), (0, 0), (3, 1), (3, 0), (5, 2), (4, 2), (2, 2),
                      (2, 1), (2, 0), (4, 1), (2, -1), (-1, -1), (0, -1), 
                      (1, 0), (1, -1), (1, 1)])
        self.assertEqual(sp, answer)
    
    def test_case3(self):
        pt1 = (-1, -1)
        pt2 = (5, 5)
        pdb = parallelogram_dynamic_bound(pt1, pt2)
        answer = set([(-1, 4), (-1, 0), (-1, 5), (5, 1), (2, 5), (1, -1), 
                      (4, -1), (-1, 1), (5, 5), (3, 3), (4, 4), (1, 5), (5, 0),
                      (-1, -1), (2, 2), (1, 1), (5, -1), (5, 4), (0, 0), 
                      (4, 5), (2, -1), (-1, 2), (0, 5), (3, 5), (5, 3), (-1, 3),
                      (3, -1), (0, -1), (5, 2)])
        self.assertEqual(pdb, answer)
    
    def test_case4(self):
        pt1 = (-1, -1)
        pt2 = (5, 5)
        s1, s2, s3 = parallelogram_shortcuts(pt1, pt2)
        ans1 = set([(-1, 1), (-1, 0), (-1, 3), (-1, 2), (5, 5), (1, 5), (0, 5),
                    (-1, 5), (-1, -1), (4, 5), (-1, 4), (2, 5), (3, 5)])
        ans2 = set([(0, 0), (3, 3), (-1, -1), (5, 5), (4, 4), (2, 2), (1, 1)])
        ans3 = set([(5, -1), (5, 4), (5, 5), (5, 2), (2, -1), (3, -1), (5, 0),
                    (-1, -1), (5, 1), (0, -1), (1, -1), (4, -1), (5, 3)])
        self.assertEqual(s1, ans1)
        self.assertEqual(s2, ans2)
        self.assertEqual(s3, ans3)
    
    def test_case5(self):
        pt1 = (-1, -1)
        pt2 = (5, 5)
        p1, p2, p3 = parallelogram_shortcut_graph(pt1, pt2)
        s1, g1 = p1
        s2, g2 = p2
        s3, g3 = p3
        ans1 = set([(-1, 1), (-1, 0), (-1, 3), (-1, 2), (5, 5), (1, 5), (0, 5),
                    (-1, 5), (-1, -1), (4, 5), (-1, 4), (2, 5), (3, 5)])
        ans2 = set([(0, 0), (3, 3), (-1, -1), (5, 5), (4, 4), (2, 2), (1, 1)])
        ans3 = set([(5, -1), (5, 4), (5, 5), (5, 2), (2, -1), (3, -1), (5, 0),
                    (-1, -1), (5, 1), (0, -1), (1, -1), (4, -1), (5, 3)])
        self.assertEqual(s1, ans1)
        self.assertEqual(s2, ans2)
        self.assertEqual(s3, ans3)
        
        ans4 = {'edge': {((5, 5), (-1, 5)): 6.0, ((-1, -1), (-1, 5)): 6.0, 
                         ((-1, 5), (-1, -1)): 6.0, ((-1, 5), (5, 5)): 6.0}, 
                'vertex': {(5, 5): set([(-1, 5)]), (-1, 5): set([(5, 5), (-1, -1)]),
                           (-1, -1): set([(-1, 5)])}}
        ans5 = {'edge': {((5, 5), (-1, -1)): 8.48528137423857, 
                         ((-1, -1), (5, 5)): 8.48528137423857},
                'vertex': {(5, 5): set([(-1, -1)]), (-1, -1): set([(5, 5)])}}
        ans6 = {'edge': {((5, -1), (5, 5)): 6.0, ((-1, -1), (5, -1)): 6.0,
                         ((5, 5), (5, -1)): 6.0, ((5, -1), (-1, -1)): 6.0},
                'vertex': {(5, -1): set([(5, 5), (-1, -1)]), 
                           (5, 5): set([(5, -1)]), (-1, -1): set([(5, -1)])}}
        self.assertEqual(g1, ans4)
        self.assertEqual(g2, ans5)
        self.assertEqual(g3, ans6)
        
if __name__ == '__main__':
    unittest.main(verbosity=1)  