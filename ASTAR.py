import heapq
import numpy as np
from VALID_MOVES import valid_moves


def H_score(node, goal, n):
    nodex, nodey = node
    goalx, goaly = goal

    mandis = abs(nodex - goalx) + abs(nodey-goaly)

    heuristic = mandis/(n-1)

    return heuristic



"""
def ASTAR(maze, start, goal):

    pqueue = []

    heapq.heappush(pqueue, (H_score(maze, start, goal), 0, (start, ())))

    while pqueue:
        _, cost, node, path = heapq.heappop(pqueue)
        path = path + (node,)

        if node == goal:
            return len(path) - 1, path
        for neighbor in valid_moves(maze, node):
            edgeweight = maze[node][neighbor]
            if edgeweight is not None:
                g_score = cost + edgeweight
                heapq.heappush(
                    pqueue, (g_score + H_score(neighbor), g_score, neighbor, path))
"""


def ASTAR(maze, start, goal):
    n = len(maze)
    pqueue = []

    g_scores = {start: 0}

    heapq.heappush(pqueue, (0 + H_score(start, goal, n), start, ()))

    while pqueue:
        _, node, path = heapq.heappop(pqueue)
        path = path + (node,)

        if node == goal:
            return len(path) - 1, path

        for neighbor in valid_moves(maze, node):
            g_score = g_scores[node] + 1

            if neighbor not in g_scores or g_score < g_scores[neighbor]:
                g_scores[neighbor] = g_score
                f_score = g_score + H_score(neighbor, goal, n)
                heapq.heappush(pqueue, (f_score, neighbor, path))

    return None, None


