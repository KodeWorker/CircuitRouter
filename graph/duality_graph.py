# -*- coding: utf-8 -*-
"""Duality Graph
description:
        
content:
    - DualityGraph
    
reference:
author: Shin-Fu (Kelvin) Wu
latest update: 
    - 2019/05/17
    - 2019/05/20 generate outline graph in DualityGraph
    - 2019/05/21 generate shortcuts in DualityGraph, fix bugs in get_sights
"""
import os
import sys
from copy import deepcopy
root = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(root)

from graph.grid8d import EightDirectionGrid
from shape.Parallelogram import parallelogram_dynamic_bound, parallelogram_shortcut_graph
from pathfinder.metrics import euclidean_distance
from pathfinder.util import is_in_line, is_within_line

class DualityGraph(EightDirectionGrid):
    
    def __init__(self, width, height):
        super(DualityGraph, self).__init__(width, height)
        self.sights = set()
        self.expands = set()
        self.outlines = set()
        self.shortcuts = set()
        
        self.vertex = {}
        self.edge = {}
    
    def set_search(self, start, end):
        self.sights.clear()
        self.expands.clear()
        self.outlines.clear()
        self.shortcuts.clear()
        
        self.vertex.clear()
        self.edge.clear()
        
        self.start = start
        self.end = end
        
        self.get_sights()
        self.get_block_in_sights()
        self.get_expands()
        self.get_shortcuts()
        self.search = self.sights | self.outlines | self.shortcuts
        
    def get_shortcuts(self):
        for v in set(self.vertex.keys()) - set(self.shortcut_vertex_exclude.keys()):
            for pair in parallelogram_shortcut_graph(v , self.end) + parallelogram_shortcut_graph(self.start , v):
                if not pair[0] & self.walls and pair[0]:
                    self.shortcuts |= pair[0]
                    vertex = pair[1]['vertex']
                    edge = pair[1]['edge']
                    self.merge_vertex(vertex)
                    self.merge_edge(edge)
        
    def get_expands(self):
        if self.block_in_sights:
            self.iso_group = self.get_iso_group()
            self.group_expand()
    
    def group_expand(self):
        expand_visited = {}
#        outline_visited = {}
        for num in self.iso_group.keys():
            group = self.iso_group[num]
            expand = self.bfs_blocks(list(group)[0], expand_visited)
            self.expands |= expand
            
#            outline = self.get_outline(expand)
#            self.outlines |= outline
#            
#            vertex, edge = self.get_directed_outline(outline, outline_visited)
#            
#            self.merge_vertex(vertex)
#            self.merge_edge(edge)
        
        self.outlines = self.get_outline(self.expands)
        vertex, edge = self.get_directed_outline(self.outlines)
        
        self.merge_vertex(vertex)
        self.merge_edge(edge)
    
    def merge_vertex(self, vertex):
        intersect = set(self.vertex.keys()) & set(vertex.keys())
        interdict = {key: self.vertex[key] | vertex[key] for key in intersect}
        self.vertex.update(vertex)        
        self.vertex.update(interdict)
    
    def merge_edge(self, edge):
        self.edge.update(edge)
    
    def get_directed_outline(self, outline):
        
        vertex = {}
        edge = {}
        visited = {}
        
        came_from = {}
        go_to = {}
                
        fork_queue = list(self.merge_nodes & outline)
        
        while fork_queue:
            
            fork = fork_queue.pop(0)
            visited[fork] = True
            fork_nodes = [pos for pos in self.adjacent_blocks(fork, outline) 
            if not visited.get(pos, False)]
            
            # daulity
            fork_from = came_from.get(fork, None)
            if fork_from:
                vertex[fork] = set(fork_nodes) | set([fork_from])
            else:
                vertex[fork] = set(fork_nodes)
            
            for fork_node in fork_nodes:                
                vertex[fork_node] = set([fork])              
                d = euclidean_distance(fork, fork_node)
                edge[(fork, fork_node)] = d
                edge[(fork_node, fork)] = d
            
            # possible loops
            for connected in self.adjacent_blocks(fork, outline):
                if visited.get(connected, False) or connected in self.merge_nodes:
                    
                    nSet = vertex.get(fork, set())
                    nSet.add(connected)
                    vertex[fork] = nSet
                    
                    nSet = vertex.get(connected, set())
                    nSet.add(fork)
                    vertex[connected] = nSet
                    
                    d = euclidean_distance(fork, connected)
                    edge[(fork, connected)] = d
                    edge[(connected, fork)] = d
            
            while fork_nodes:
                
                current = fork_nodes.pop(0)                
                came_from[current] = fork
                
                search_queue = []
                search_queue.append(current)
                visited[current] = True
                
                while search_queue:
                    
                    node = search_queue.pop(0)
                        
                    if len([pos for pos in self.adjacent_blocks(node, outline)
                    if not visited.get(pos, False) and pos not in self.merge_nodes]) == 0:
                        
                        # daulity                        
                        # end of branch
                        nSet = vertex.get(node, set())
                        nSet.add(came_from[node])
                        vertex[node] = nSet                       
                        vertex[came_from[node]].add(node)
                        
                        d = euclidean_distance(node, came_from[node])
                        edge[(node, came_from[node])] = d
                        edge[(came_from[node], node)] = d

                        # possible loops
                        for connected in self.adjacent_blocks(node, outline):
                            if visited.get(connected, False) or connected in self.merge_nodes:
                                
                                nSet = vertex.get(node, set())
                                nSet.add(connected)
                                vertex[node] = nSet
                                
                                nSet = vertex.get(connected, set())
                                nSet.add(node)
                                vertex[connected] = nSet
                                
                                d = euclidean_distance(node, connected)
                                edge[(node, connected)] = d
                                edge[(connected, node)] = d
                        break
                    
                    if len([pos for pos in self.adjacent_blocks(node, outline)
                    if not visited.get(pos, False)]) > 1 and node not in self.merge_nodes:
                        fork_queue.append(node)
                        
                        # daulity
                        vertex[node] = set([came_from[node]])                        
                        vertex[came_from[node]].add(node)
                        
                        d = euclidean_distance(node, came_from[node])
                        edge[(node, came_from[node])] = d
                        edge[(came_from[node], node)] = d
                        break
                    else:
                        
                        for next_node in self.adjacent_blocks(node, outline):
                            if not visited.get(next_node, False):
                                search_queue.append(next_node)
                                came_from[next_node] = node
                                go_to[node] = next_node
                                visited[next_node] = True
                                
                                # daulity
                                if not is_in_line(came_from[node], node, go_to[node]):
                                    
                                    vertex[node] = set([came_from[node]])
                                    vertex[came_from[node]].add(node)
                                    
                                    d = euclidean_distance(came_from[node], node)
                                    edge[(came_from[node], node)] = d
                                    edge[(node, came_from[node])] = d

                                else:                                    
                                    if node == current:
                                        vertex[came_from[node]].remove(node)
                                        vertex.pop(node)
                                    came_from[go_to[node]] = came_from[node]
                                    go_to[came_from[node]] = go_to[node]
                                    
        return vertex, edge
         
    def get_outline(self, expand):
        outline = set()
        for pos in expand:
            outline |= set(self.obstacle_outlines(pos))
        return outline
    
    def obstacle_outlines(self, pos):
        candidates = self.outline_candidates(pos)
        candidates = list(filter(self.in_bounds, candidates))
        candidates = list(filter(self.passable, candidates))
        return candidates
    
    def outline_candidates(self, pos):
        x, y = pos
        candidates = [(x, y+1), (x-1, y  ), (x+1, y), (x, y-1)]
        return candidates
    
    def bfs_blocks(self, block, visited):
#        visited = {}        
        
        queue = []
        queue.append(block)
        visited[block] = True
        
        while queue:
            
            current = queue.pop(0)
            
            for neighbor in self.adjacent_blocks(current, self.walls):
                if not visited.get(neighbor, False):
                    queue.append(neighbor)
                    visited[neighbor] = True
                        
        return set(visited.keys())
    
    def get_iso_group(self):
        groups = {}
        g_key = 0
        
        visited = {}
        queue = []
        temp = set()
        
        blocks = list(self.block_in_sights)
        init = blocks.pop(0)
        queue.append(init)
        visited[init] = True
        temp.add(init)
        
        while blocks or queue:
            while queue:
                current = queue.pop(0)
                                    
                for block in self.adjacent_blocks(current, self.block_in_sights):
                    if not visited.get(block, False):
                        queue.append(block)
                        visited[block] = True
                        temp.add(block)
                        blocks.remove(block)
            
            groups[g_key] = deepcopy(temp)
            temp.clear()
            g_key += 1
            if not blocks:
                break
            else:
                # prepare next queue
                init = blocks.pop(0)
                queue.append(init)
                visited[init] = True
                temp.add(init)
                
        return groups
    
    def adjacent_blocks(self, pos, blocks):
        candidates = self.get_candidates(pos)
        candidates = list(filter(self.in_bounds, candidates))
        candidates = set(candidates) & blocks
        return candidates
    
    def get_block_in_sights(self):        
        self.block_in_sights = self.sights & self.walls
        self.sights -= self.walls
        
        # duality
        self.merge_nodes = set()
        
        for pos in self.block_in_sights:
            self.merge_nodes |= (set(self.adjacent_blocks(pos, self.sights)) - self.block_in_sights)
        self.merge_nodes -= set(self.vertex.keys())
        
        ## new vertex around blocks
        #! bugs
        add_edge = deepcopy(self.edge)
        rm_pair = set()
        
        for pair in self.edge.keys():
            
            nodes_in_edge = set()
            
            for node in self.merge_nodes:
                
                if is_in_line(pair[0], node, pair[1]) and \
                is_within_line(pair[0], node, pair[1]):
                    self.vertex[node] = set(pair)
                    self.vertex[pair[0]].add(node) 
                    self.vertex[pair[1]].add(node)
                    d = euclidean_distance(node, pair[0])
                    add_edge[(node, pair[0])] = d
                    add_edge[(pair[0], node)] = d
                    rm_pair.add(pair)
                    nodes_in_edge.add(node)
            
                for n1 in nodes_in_edge:
                    for n2 in [pos for pos in nodes_in_edge if pos != n1]:
                        self.vertex[n1].add(n2)
                        self.vertex[n2].add(n1)
                        d = euclidean_distance(n1, n2)
                        add_edge[(n1, n2)] = d
                        add_edge[(n2, n1)] = d
                
        self.edge = add_edge
        
        for pair in rm_pair:
            self.remove_edge(pair)
        ## delete blocked vertex
        rm_vertex = set(self.vertex.keys()) & self.block_in_sights
        for vertex in rm_vertex:
            self.remove_vertex(vertex)
        ## delete blocked edge
        rm_pair = set()
        checknodes = self.block_in_sights - set(self.vertex.keys())
        for node in checknodes:
            for pair in self.edge.keys():
                if is_in_line(pair[0], node, pair[1]) and \
                is_within_line(pair[0], node, pair[1]):
                    rm_pair.add(pair)
                    
        for pair in rm_pair:
            self.remove_edge(pair)
                    
    def remove_vertex(self, vertex):
        rm_pair = set()
        for node in self.vertex[vertex]:
            rm_pair.add((vertex, node))
            rm_pair.add((node, vertex))
        for pair in rm_pair:
            self.remove_edge(pair)
        self.vertex.pop(vertex)
    
    def remove_edge(self, pair):
        v1, v2 = pair
        self.edge.pop(pair)
        try:
            self.vertex[v1].remove(v2)
        except:
            pass
        try:
            self.vertex[v2].remove(v1)
        except:
            pass
    
    def get_sights(self):
        self.sights = parallelogram_dynamic_bound(self.start, self.end)
        
        # duality
        if self.start[1] >= self.end[1]:
            pt1, pt2 = self.end, self.start
        else:
            pt1, pt2 = self.start, self.end
            
        dx, dy = abs(pt1[0] - pt2[0]), abs(pt1[1] - pt2[1])
        if dx == dy:
            v1 = pt1
            v2 = (pt1[0], pt1[1] + dy)
            v3 = pt2
            v4 = (pt2[0], pt2[1] - dy)            
        elif dx > dy:
            v1 = pt1
            v2 = (pt2[0] - dx, pt2[1])
            v3 = pt2
            v4 = (pt1[0] + dx, pt1[1])
        elif dx < dy:
            v1 = pt1
            v2 = (pt1[0], pt2[1] - dx)
            v3 = pt2
            v4 = (pt2[0], pt1[1] + dx)
        if dx == dy:
            self.vertex[v1] = set([v2, v4, v3])
            self.vertex[v2] = set([v1, v3])
            self.vertex[v3] = set([v2, v4, v1])
            self.vertex[v4] = set([v3, v1])
        else:
            self.vertex[v1] = set([v2, v4])
            self.vertex[v2] = set([v1, v3])
            self.vertex[v3] = set([v2, v4])
            self.vertex[v4] = set([v3, v1])
        
        for v1 in self.vertex.keys():
            for v2 in self.vertex[v1]:
                self.edge[(v1, v2)] = euclidean_distance(v1, v2)
        
        self.shortcut_vertex_exclude = deepcopy(self.vertex)
    
    def get_candidates(self, pos):
        x, y = pos
        candidates = [(x-1, y+1), (x, y+1), (x+1, y+1),
                      (x-1, y  ),           (x+1, y),
                      (x-1, y-1), (x, y-1), (x+1, y-1)]
        return candidates
    
    def neighbors(self, pos):
        return self.vertex[pos]
    
    def cost(self, from_node, to_node):
        return self.edge[(from_node, to_node)]
    
if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from shape.OctagonLine import solid_octagon_line
    from pathfinder.astar import a_star_search
    from pathfinder.util import reduce_path, reconstruct_path
    dg = DualityGraph(1000, 1000)

#    for pos in solid_octagon_line((6, 2), (15, 11), 1):
#        dg.walls.add(pos)    
    
#    for pos in solid_octagon_line((5, 8), (15, 8), 1):
#        dg.walls.add(pos)
#    
#    for pos in solid_octagon_line((2, 10), (2, 2), 1):
#        dg.walls.add(pos)
    
#    for x in range(9, 12):
#        for y in range(4, 7):
#            dg.walls.add((x, y))  
    
#    for x in range(13, 16):
#        dg.walls.add((x, 4))
#    
#    dg.walls.add((10, 10))
#    dg.walls.add((10, 6))
#    
#    for x in range(5, 11):
#        dg.walls.add((x, 3))
#    dg.walls.add((13, 12))
        
#    start = (10, 0)
#    goal = (13, 15)
    
    start = (0, 0)
    goal = (3, 3)
    dg.set_search(start, goal)
    
    plt.figure()
    # walls
    plt.scatter([p[0] for p in dg.walls],
                [p[1] for p in dg.walls], color='black')
    # vertex
    plt.scatter([p[0] for p in dg.vertex.keys()],
                [p[1] for p in dg.vertex.keys()], color='blue')
    # edge
    for key in dg.edge.keys():
        pt1, pt2 = key
        plt.plot([pt1[0], pt2[0]], [pt1[1], pt2[1]], color='green')
    
#    plt.scatter([p[0] for p in dg.outlines],
#                [p[1] for p in dg.outlines], color='orange')
    
    
#    for num in dg.iso_graph.keys():
#        vertex = dg.iso_graph[num]['vertex']
#        edge = dg.iso_graph[num]['edge']
#        
#        plt.scatter([p[0] for p in vertex.keys()],
#                [p[1] for p in vertex.keys()], color='yellow')
#        for key in edge.keys():
#            pt1, pt2 = key
#            plt.plot([pt1[0], pt2[0]], [pt1[1], pt2[1]], color='yellow')
    
    came_from, cost_so_far = a_star_search(dg, start, goal, p=0.5)
    path = reconstruct_path(came_from, start, goal)
    path = reduce_path(path)
    for i in range(1, len(path)):
        plt.plot([path[i-1][0], path[i][0]],
                 [path[i-1][1], path[i][1]], color='red')