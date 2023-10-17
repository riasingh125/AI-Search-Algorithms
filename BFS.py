import numpy as np
from VALID_MOVES import valid_moves
from collections import deque

def BFS(maze, start):
    n_rows = len(maze)
    n_cols = len(maze)


    if start[0] < 0 or start[0] >= n_rows or start[1] < 0 or start[1] >= n_cols:
        return None 

    path_matrix = np.full((n_rows, n_cols), -1, dtype=int)

    queue = deque([(start[0], start[1], 0)])

    path_matrix[start[0]][start[1]] = 0

    while queue:
        row, col, distance = queue.popleft()

        neighbors = valid_moves(maze, (row, col))

        for new_row, new_col in neighbors:
            new_distance = distance + 1

            if path_matrix[new_row][new_col] == -1 or new_distance < path_matrix[new_row][new_col]:
                path_matrix[new_row][new_col] = new_distance
                queue.append((new_row, new_col, new_distance))
 
    return path_matrix



'''
def BFS(maze, start):

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    rows, cols = len(maze), len(maze[0])

    queue = deque([(start[0], start[1], 0)])

    visited = set()

    visited.add(start)

    path_matrix = np.full((rows, cols), -1)
    path_matrix[start[0]][start[1]] = 0

    while queue:
        row, col, distance = queue.popleft()

        if maze[row][col] == 'G':
            return path_matrix

        for dr, dc in directions:
            r, c = rows + dr, cols + dc

            if (r, c) in valid_moves(maze, (r, c)) and (r, c) not in visited:
                queue.append((r, c, distance + 1))
                visited.add((r, c))
                path_matrix[r][c] = distance + 1

    return path_matrix

'''


"""
	visited = set()
	distances = {start: 0}
	
	queue = deque([start])

	while queue:
		current_cell = queue.popleft()
		for neighbor in valid_moves(maze, current_cell):
			if neighbor not in visited:
				visited.add(neighbor)
				distances[neighbor] = distances[current_cell] + 1
				queue.append(neighbor)
"""

"""
def BFS(maze, start):

	directions = [(1,0), (-1,0), (0,1), (0,-1)]
	
	rows, cols = len(maze), len(maze[0])

	queue = deque([(start[0], start[1], 0)])

	visited = set()

	visited.add(start)

	path_matrix = np.full((rows, cols), -1)
	path_matrix[start[0]][start[1]] = 0

	while queue:
		rows, cols, distance = queue.popleft()

		if maze[rows][cols] == 'G':
			return path_matrix
		
		for dr,dc in directions:
			r, c = rows + dr, cols + dc

			if 0 <= r < rows and 0 <= c < cols and maze[r][c] != '#' and (r,c) not in visited:
				queue.append((r,c, distance + 1))
				visited.add((r,c))
				path_matrix[r][c] = distance + 1

"""

"""
def BFS(maze, start):

	directions = [(1,0), (-1,0), (0,1), (0,-1)]
	
	rows, cols = len(maze), len(maze[0])

	queue = deque([(start[0], start[1], 0)])

	visited = set()

	visited.add(start)

	while queue == True:
		rows, cols, distance = queue.popleft()

		if maze[row][col] == 'G':
			return distance
		for dr,dc in directions:
			r, c = rows + dr, cols + dc
			if 0 <= r < rows and 0 <= c < cols and maze[r][c] != '#' and (r,c) not in visited:
				queue.append((r,c, distance + 1))
				visited.add((r,c))

		return -1
"""
