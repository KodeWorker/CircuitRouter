# -*- coding: utf-8 -*-
"""Parallelogram Shapes
description:
    
content:
    - parallelogram_shortcut_graph
    - parallelogram_shortcuts
    - parallelogram_dynamic_bound
    - parallelogram
    - solid_parallelogram

author: Shin-Fu (Kelvin) Wu
latest update: 
    - 2019/05/14
    - 2019/05/16 add parallelogram for dynmaic bounds
    - 2019/05/20 add parallelogram_shortcut_graph
    - 2019/05/21 update pt1[0] >= pt2[0] for shape
"""
from pathfinder.metrics import euclidean_distance
from shape.Rectangle import rectangle, solid_rectangle
from shape.Line import bresenhams_line

def parallelogram_shortcut_graph(pt1, pt2):
    if pt1[1] >= pt2[1]:
        pt1, pt2 = pt2, pt1
        
    dx, dy = abs(pt1[0] - pt2[0]), abs(pt1[1] - pt2[1])
    s1, s2, s3 = set(), set(), set()
    g1 = {'vertex': {}, 'edge': {}}
    g2 = {'vertex': {}, 'edge': {}}
    g3 = {'vertex': {}, 'edge': {}}
    if dx == dy:
        pt3 = (pt1[0], pt2[1])
        pt4 = (pt2[0], pt1[1])
        l1 = bresenhams_line(pt1, pt3)
        l2 = bresenhams_line(pt3, pt2)
        l3 = bresenhams_line(pt2, pt4)
        l4 = bresenhams_line(pt4, pt1)
        
        s1 |= l1 | l2
        s2 |= bresenhams_line(pt1, pt2)
        s3 |= l3 | l4
        
        # graph
        g1['vertex'][pt1] = set([pt3])
        g1['vertex'][pt3] = set([pt2, pt1])
        g1['vertex'][pt2] = set([pt3])
        g1['edge'][(pt1, pt3)] = euclidean_distance(pt1, pt3)
        g1['edge'][(pt3, pt1)] = euclidean_distance(pt3, pt1)
        g1['edge'][(pt3, pt2)] = euclidean_distance(pt3, pt2)
        g1['edge'][(pt2, pt3)] = euclidean_distance(pt2, pt3)
        
        g2['vertex'][pt1] = set([pt2])
        g2['vertex'][pt2] = set([pt1])
        g2['edge'][(pt1, pt2)] = euclidean_distance(pt1, pt2)
        g2['edge'][(pt2, pt1)] = euclidean_distance(pt2, pt1)
        
        g3['vertex'][pt1] = set([pt4])
        g3['vertex'][pt4] = set([pt1, pt2])
        g3['vertex'][pt2] = set([pt4])
        g3['edge'][(pt1, pt4)] = euclidean_distance(pt1, pt4)
        g3['edge'][(pt4, pt1)] = euclidean_distance(pt4, pt1)
        g3['edge'][(pt4, pt2)] = euclidean_distance(pt4, pt2)
        g3['edge'][(pt2, pt4)] = euclidean_distance(pt2, pt4)
        
    elif dx > dy:
        if pt1[0] >= pt2[0]:
            pt3 = (pt1[0] - dy, pt2[1])
            pt4 = (pt2[0] + dy, pt1[1])
        else:
            pt3 = (pt1[0] + dy, pt2[1])
            pt4 = (pt2[0] - dy, pt1[1])
        l1 = bresenhams_line(pt1, pt3)
        l2 = bresenhams_line(pt3, pt2)
        l3 = bresenhams_line(pt2, pt4)
        l4 = bresenhams_line(pt4, pt1)
        s1 |= l1 | l2 
        s3 |= l3 | l4
        # graph
        g1['vertex'][pt1] = set([pt3])
        g1['vertex'][pt3] = set([pt2, pt1])
        g1['vertex'][pt2] = set([pt3])
        g1['edge'][(pt1, pt3)] = euclidean_distance(pt1, pt3)
        g1['edge'][(pt3, pt1)] = euclidean_distance(pt3, pt1)
        g1['edge'][(pt3, pt2)] = euclidean_distance(pt3, pt2)
        g1['edge'][(pt2, pt3)] = euclidean_distance(pt2, pt3)
                
        g3['vertex'][pt1] = set([pt4])
        g3['vertex'][pt4] = set([pt1, pt2])
        g3['vertex'][pt2] = set([pt4])
        g3['edge'][(pt1, pt4)] = euclidean_distance(pt1, pt4)
        g3['edge'][(pt4, pt1)] = euclidean_distance(pt4, pt1)
        g3['edge'][(pt4, pt2)] = euclidean_distance(pt4, pt2)
        g3['edge'][(pt2, pt4)] = euclidean_distance(pt2, pt4)
        
    elif dx < dy:
        pt3 = (pt1[0], pt1[1] + dy - dx)
        pt4 = (pt2[0], pt2[1] - dy + dx)
        l1 = bresenhams_line(pt1, pt3)
        l2 = bresenhams_line(pt3, pt2)
        l3 = bresenhams_line(pt2, pt4)
        l4 = bresenhams_line(pt4, pt1)
        s1 |= l1 | l2 
        s3 |= l3 | l4
        # graph
        g1['vertex'][pt1] = set([pt3])
        g1['vertex'][pt3] = set([pt2, pt1])
        g1['vertex'][pt2] = set([pt3])
        g1['edge'][(pt1, pt3)] = euclidean_distance(pt1, pt3)
        g1['edge'][(pt3, pt1)] = euclidean_distance(pt3, pt1)
        g1['edge'][(pt3, pt2)] = euclidean_distance(pt3, pt2)
        g1['edge'][(pt2, pt3)] = euclidean_distance(pt2, pt3)
                
        g3['vertex'][pt1] = set([pt4])
        g3['vertex'][pt4] = set([pt1, pt2])
        g3['vertex'][pt2] = set([pt4])
        g3['edge'][(pt1, pt4)] = euclidean_distance(pt1, pt4)
        g3['edge'][(pt4, pt1)] = euclidean_distance(pt4, pt1)
        g3['edge'][(pt4, pt2)] = euclidean_distance(pt4, pt2)
        g3['edge'][(pt2, pt4)] = euclidean_distance(pt2, pt4)
        
    return (s1, g1), (s2, g2), (s3, g3)

def parallelogram_shortcuts(pt1, pt2):
    if pt1[1] >= pt2[1]:
        pt1, pt2 = pt2, pt1
        
    dx, dy = abs(pt1[0] - pt2[0]), abs(pt1[1] - pt2[1])
    s1, s2, s3 = set(), set(), set()
    if dx == dy:
        pt3 = (pt1[0], pt2[1])
        pt4 = (pt2[0], pt1[1])
        l1 = bresenhams_line(pt1, pt3)
        l2 = bresenhams_line(pt3, pt2)
        l3 = bresenhams_line(pt2, pt4)
        l4 = bresenhams_line(pt4, pt1)
        
        s1 |= l1 | l2
        s2 |= bresenhams_line(pt1, pt2)
        s3 |= l3 | l4
        
    elif dx > dy:
        if pt1[0] >= pt2[0]:
            pt3 = (pt1[0] - dy, pt2[1])
            pt4 = (pt2[0] + dy, pt1[1])
        else:
            pt3 = (pt1[0] + dy, pt2[1])
            pt4 = (pt2[0] - dy, pt1[1])
        l1 = bresenhams_line(pt1, pt3)
        l2 = bresenhams_line(pt3, pt2)
        l3 = bresenhams_line(pt2, pt4)
        l4 = bresenhams_line(pt4, pt1)
        s1 |= l1 | l2 
        s3 |= l3 | l4
    elif dx < dy:
        pt3 = (pt1[0], pt1[1] + dy - dx)
        pt4 = (pt2[0], pt2[1] - dy + dx)
        l1 = bresenhams_line(pt1, pt3)
        l2 = bresenhams_line(pt3, pt2)
        l3 = bresenhams_line(pt2, pt4)
        l4 = bresenhams_line(pt4, pt1)
        s1 |= l1 | l2 
        s3 |= l3 | l4
        
    return s1, s2, s3

def parallelogram_dynamic_bound(pt1, pt2):
    if pt1[1] >= pt2[1]:
        pt1, pt2 = pt2, pt1
        
    dx, dy = abs(pt1[0] - pt2[0]), abs(pt1[1] - pt2[1])
    pixel = set()
    if dx == dy:
        pixel = rectangle(pt1, pt2)
        pixel |= bresenhams_line(pt1, pt2)
    elif dx > dy:
        if pt1[0] >= pt2[0]:
            pt3 = (pt1[0] - dy, pt2[1])
            pt4 = (pt2[0] + dy, pt1[1])
        else:
            pt3 = (pt1[0] + dy, pt2[1])
            pt4 = (pt2[0] - dy, pt1[1])
        l1 = bresenhams_line(pt1, pt3)
        l2 = bresenhams_line(pt3, pt2)
        l3 = bresenhams_line(pt2, pt4)
        l4 = bresenhams_line(pt4, pt1)
        pixel |= l1 | l2 | l3 | l4
    elif dx < dy:
        pt3 = (pt1[0], pt1[1] + dy - dx)
        pt4 = (pt2[0], pt2[1] - dy + dx)
        l1 = bresenhams_line(pt1, pt3)
        l2 = bresenhams_line(pt3, pt2)
        l3 = bresenhams_line(pt2, pt4)
        l4 = bresenhams_line(pt4, pt1)
        pixel |= l1 | l2 | l3 | l4
        
    return pixel

def parallelogram(pt1, pt2):
    if pt1[1] >= pt2[1]:
        pt1, pt2 = pt2, pt1
        
    dx, dy = abs(pt1[0] - pt2[0]), abs(pt1[1] - pt2[1])
    pixel = set()
    if dx == dy:
        pixel = rectangle(pt1, pt2)
    elif dx > dy:
        if pt1[0] >= pt2[0]:
            pt3 = (pt1[0] - dy, pt2[1])
            pt4 = (pt2[0] + dy, pt1[1])
        else:
            pt3 = (pt1[0] + dy, pt2[1])
            pt4 = (pt2[0] - dy, pt1[1])
        l1 = bresenhams_line(pt1, pt3)
        l2 = bresenhams_line(pt3, pt2)
        l3 = bresenhams_line(pt2, pt4)
        l4 = bresenhams_line(pt4, pt1)
        pixel |= l1 | l2 | l3 | l4
    elif dx < dy:
        pt3 = (pt1[0], pt1[1] + dy - dx)
        pt4 = (pt2[0], pt2[1] - dy + dx)
        l1 = bresenhams_line(pt1, pt3)
        l2 = bresenhams_line(pt3, pt2)
        l3 = bresenhams_line(pt2, pt4)
        l4 = bresenhams_line(pt4, pt1)
        pixel |= l1 | l2 | l3 | l4
        
    return pixel

def solid_parallelogram(pt1, pt2):
    if pt1[1] >= pt2[1]:
        pt1, pt2 = pt2, pt1
        
    dx, dy = abs(pt1[0] - pt2[0]), abs(pt1[1] - pt2[1])
    pixel = set()
    if dx == dy:
        pixel = solid_rectangle(pt1, pt2)
    elif dx > dy:
        if pt1[0] >= pt2[0]:
            pt3 = (pt1[0] - dy, pt2[1])
            pt4 = (pt2[0] + dy, pt1[1])
        else:
            pt3 = (pt1[0] + dy, pt2[1])
            pt4 = (pt2[0] - dy, pt1[1])
        l2 = bresenhams_line(pt3, pt2, True)
        l4 = bresenhams_line(pt1, pt4, True)
        for s, e in zip(l2, l4):
            pixel |= bresenhams_line(s, e)        
    elif dx < dy:
        pt3 = (pt1[0], pt1[1] + dy - dx)
        pt4 = (pt2[0], pt2[1] - dy + dx)
        l2 = bresenhams_line(pt3, pt2, True)
        l4 = bresenhams_line(pt4, pt1, True)
        for s, e in zip(l2, l4):
            pixel |= bresenhams_line(s, e)
    
    return pixel

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    
#    pt2 = (-1, -1)
#    pt1 = (8, 8)
    
    pt2 = (-1, 15)
    pt1 = (5, -1)
        
    p = parallelogram(pt1, pt2)
    sp = solid_parallelogram(pt1, pt2)
    
    plt.figure()
    plt.title('Parallelogram Shapes')
    for pos in sp:
        plt.scatter(pos[0], pos[1], color='blue')
    for pos in p:
        plt.scatter(pos[0]+0.1, pos[1]+0.1, color='red')
    plt.savefig('parallelogram.png', dpi=200)
    plt.close()
    