# -*- coding: utf-8 -*-
"""Basic A-star Algorithm

content:
    - PriorityQueue
    - diagonal_distance
    - a_star_algorithm
    - reconstruct_path
    - is_in_path
    - reduce_path

reference:
    1. https://www.redblobgames.com/pathfinding/a-star/implementation.html
    2. http://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html

latest update: 2019/05/10

"""
import heapq

class PriorityQueue:    
    def __init__(self):
        """ Queue with priority
        In ref. 1, it shows the reason why using a prioty queue to store the costs 
        of calculated vertices.
        """
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]
    
def diagonal_distance(a, b, D=1, D2=1):
    """ Diagonal Distance
    In ref. 2, it shows that on a square grid that allows 8 directions of 
    movement, use Diagonal distance.
    """
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])
    return D * max(dx, dy) + (D2-D) * min(dx, dy)

def a_star_search(graph, start, goal, heuristic=diagonal_distance, p=0):
    """A-star Search
    This function is the basic A* algorithm with a tie-breaking parameter.
    The default value of p is set to 0 (no tie-breaking). 
    """
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            break
        
        for next in graph.get_neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + (1.0 + p)*heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current
                         
    return came_from, cost_so_far

def reconstruct_path(came_from, start, goal):
    """Reconstruct Path
    Reconstruct a path from search result.
    """
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]        
    path.append(start) # optional
    path.reverse() # optional
    return path

def is_in_path(P1, P2, P3):
    """Is in path
    Check if the points are in the same line.
    """
    a = (P2[0] - P1[0]) * (P3[1] - P2[1])
    b = (P2[1] - P1[1]) * (P3[0] - P2[0])    
    if a - b == 0:
        return True
    else:
        return False
    
def reduce_path(path):
    """Reduce Path
    Reduce all the locations in a path into turning points.
    """
    reduced_path = [path[0], path[1]]    
    ind = 2
    while ind < len(path):
        if is_in_path(path[ind], path[ind-1], path[ind-2]):
            reduced_path[-1] = path[ind]
        else:
            reduced_path.append(path[ind])
        ind += 1                            
    if reduced_path[-1] != path[-1]:
        reduced_path.append(path[-1])    
    return reduced_path