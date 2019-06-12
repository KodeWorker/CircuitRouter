# -*- coding: utf-8 -*-
import os
import sys
root = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(root)

import os
import math
import json
import shutil                                                                                      
import warnings
from graph.duality_graph import DualityGraph
from pathfinder.astar import a_star_search
from pathfinder.util import reconstruct_path

class TwoStageGraph(DualityGraph):
    def __init__(self, width, height, step, celldir=None):
        super(TwoStageGraph, self).__init__(width, height)
        self.width_s1 = width
        self.height_s1 = height
        self.step = step
        self.celldir = celldir
        self.init_graph()
    
    def init_graph(self):
        self.walls_s1 = set()
        self.walls_s2 = set()
        self.width_s2 = int(math.ceil(self.width_s1/float(self.step)))
        self.height_s2 = int(math.ceil(self.height_s1/float(self.step)))
        # init file system
        if not self.celldir:
            try:
                shutil.rmtree('.cell')
            except:
                warnings.warn('No existing .cell folder!')
            self.celldir = '.cell'
        os.makedirs(self.celldir)
        
        for x in range(self.width_s2):
            for y in range(self.height_s2):
                with open(os.path.join(self.celldir, '.x{}y{}'.format(x, y)), 'wb') as writeFile:
                    json.dump(list(), writeFile)
    
    def add_wall(self, pos):
        if self.in_bounds(pos):
            sec = self.get_s2_section(pos)
            filename = '.x{}y{}'.format(sec[0], sec[1])
            with open(os.path.join(self.celldir, filename), 'rb') as readFile:
                set_ = set(json.load(readFile))
            set_.add(pos)
            with open(os.path.join(self.celldir, filename), 'wb') as writeFile:
                json.dump(list(set_), writeFile)
            self.walls_s2.add(sec)
    
    def add_walls(self, pos_set):
        sec_dict = {}
        for pos in pos_set:
            sec = self.get_s2_section(pos)
            sec_set = sec_dict.get(sec, set())
            sec_set.add(pos)
            sec_dict[sec] = sec_set
            
        for sec in sec_dict.keys():
            filename = '.x{}y{}'.format(sec[0], sec[1])
            with open(os.path.join(self.celldir, filename), 'rb') as readFile:
                list_ = json.load(readFile)
                set_ = set([tuple(l) for l in list_])
            set_ |= sec_dict[sec]
            with open(os.path.join(self.celldir, filename), 'wb') as writeFile:
                json.dump(list(set_), writeFile)
            self.walls_s2.add(sec)
    
    def get_s2_section(self, pos):
        x = int(math.floor(pos[0]/float(self.step)))
        y = int(math.floor(pos[1]/float(self.step)))
        return (x, y)
    
    def load_section(self, sec):
        filename = '.x{}y{}'.format(sec[0], sec[1])
        with open(os.path.join(self.celldir, filename), 'rb') as readFile:
            list_ = json.load(readFile)
        self.walls_s1 |= set([tuple(l) for l in list_])
    
    def in_sections(self, sec):
        (x, y) = sec
        return 0 <= x < self.width_s2 and 0 <= y < self.height_s2
    
    def preload(self, start, end):
        self.walls.clear()
        start_sec = self.get_s2_section(start)
        end_sec = self.get_s2_section(end)
        self.walls |= self.walls_s2 - set([start_sec, end_sec])
        self.set_search(start_sec, end_sec)
        came_from, cost_so_far = a_star_search(self, start_sec, end_sec)
        path_sec = reconstruct_path(came_from, start_sec, end_sec)
        
        blocks = []
        for sec in path_sec:
            if self.in_sections(sec):
                blocks += self.get_candidates(sec)
        blocks = set(blocks) & self.walls_s2
        
        visited = {}
        expand = set()
        for block in blocks:
            expand |= self.bfs_blocks(block, visited)
        self.walls.clear()
        
        for sec in expand:
            self.load_section(sec)
        self.walls = self.walls_s1
        
if __name__ == '__main__':
    from shape.OctagonLine import solid_octagon_line
    import matplotlib.pyplot as plt
    
    graph = TwoStageGraph(10000, 10000, 100)
    
    print('*')
    blocks = solid_octagon_line((550, 500), (550, 5500), 20)
    print(len(blocks))
#    for pos in solid_octagon_line((550, 500), (550, 5500), 20):
#        graph.add_wall(pos)
    graph.add_walls(solid_octagon_line((550, 500), (550, 5500), 20))        
    print('**')
    start, end = (500, 500), (600, 5100)
    
    graph.preload(start, end)
    graph.set_search(start, end)
    print(len(graph.walls))
    
    came_from, cost_so_far = a_star_search(graph, start, end)
    path = reconstruct_path(came_from, start, end)
    
    plt.figure()
    plt.scatter([pos[0] for pos in blocks], [pos[1] for pos in blocks], color='black')
    plt.scatter([pos[0] for pos in graph.walls], [pos[1] for pos in graph.walls], color='orange')
    for i in range(1, len(path)):
        plt.plot([path[i-1][0], path[i][0]],
                 [path[i-1][1], path[i][1]], color='red')