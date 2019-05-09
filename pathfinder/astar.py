# -*- coding: utf-8 -*-
import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]
    
def diagonal_distance(a, b, D=1, D2=1):
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])
    return D * max(dx, dy) + (D2-D) * min(dx, dy)

def a_star_algorithm(graph, start, goal, heuristic=diagonal_distance):
    start = tuple(start)
    goal = tuple(goal)
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            return reconstruct_path(came_from, start, goal)
        
        for next in graph.get_neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current
                         
    # Return None when there is no path
    return None

def reconstruct_path(came_from, start, goal):
    start = tuple(start)
    goal = tuple(goal)
    
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    return path