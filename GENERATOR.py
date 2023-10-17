import sys
import numpy as np
from BFS import BFS
import random
from collections import deque



def generator(k):
    maze = np.random.randint(1, k, size=(k, k), dtype=int)
    
    start = (random.randint(0, k-1), random.randint(0, k-1))
    goal = (random.randint(0, k-1), random.randint(0, k-1))
    

    while start == goal:
        goal = (random.randint(0, k-1), random.randint(0, k-1))

    maze[goal] = 0
    
    return maze, start, goal
   




def generator_pathcheck(k):
    while True:
        maze, start, goal = generator(k)
        path_matrix = BFS(maze, start)

        if path_matrix[goal[0]][goal[1]] != -1:
            return maze, start, goal



"""
def generator_pathcheck(k):
    init_board = {(i, j): random.randint(1, k - 1)
                  for i in range(k) for j in range(k)}

    start_cell, goal_state = random.sample(init_board.keys(), 2)

    print(start_cell, goal_state)

    if BFS(init_board, start_cell):
        return init_board, start_cell, goal_state
    else:
        return generator_pathcheck(k)

"""

""" def generate_path_check(k):
	init_board = {}

	for i in range(k):
		for j in range(k):
			rando = random.randint(1, k - 1)
			init_board[(i, j)] = rando

	start_cell = random.choice(list(init_board.keys()))
	goal_state = random.choice(list(init_board.keys()))

	while start_cell == goal_state:
		goal_state = random.choice(list(init_board.keys()))

	print(start_cell, goal_state)

	if bfs(init_board, start_cell, goal_state):
		return init_board, start_cell, goal_state
	else:
		return generate_path_check(k)
"""
'''
def generator(k):

    init_board = []

    for i in range(k):
        row = []
        for j in range(k):
            rando = random.randint(1, k)
            row.append(rando)
        init_board.append(row)

    start_cell = random.choice(init_board)
    goal_state = random.choice(init_board)

    while start_cell == goal_state:
        start_cell = random.choice(init_board)
    print(start_cell, goal_state)

    return init_board, start_cell, goal_state
'''


