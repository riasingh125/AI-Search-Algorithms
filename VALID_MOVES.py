
def valid_moves(maze, node):
    n = len(maze)
    x, y = node
    moves = maze[x][y]
    neighbors = []

    if y + moves < n:
        neighbors.append((x, y + moves))

    if y - moves >= 0:
        neighbors.append((x, y - moves))

    if x + moves < n:
        neighbors.append((x + moves, y))

    if x - moves >= 0:
        neighbors.append((x - moves, y))

    return neighbors


"""
def valid_moves(maze, node):
	neighbors = []
	x, y = node

	rightx = x + 1
	leftx = x - 1
	topy = y - 1
	bottomy = y + 1

	noderight = (rightx, y)
	nodeleft = (leftx, y)
	nodetop = (x, topy)
	nodebottom = (x, bottomy)

	if (
		(rightx >= 0 and rightx < len(maze))
		and (leftx >= 0 and leftx < len(maze))
		and (topy >= 0 and topy < len(maze[0]))
		and (bottomy >= 0 and bottomy < len(maze[0]))
	):
		neighbors.extend([noderight, nodeleft, nodetop, nodebottom])

	return neighbors
	"""


