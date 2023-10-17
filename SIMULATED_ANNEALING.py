import math
import sys
import numpy as np
import random
from BFS import BFS
from ASTAR import ASTAR
from HILLDESCENT import energyfunction
from VALID_MOVES import valid_moves


def SIMULATED_ANNEALING(maze, start_cell, goal_state, iterations, T, decay):

    currmaze = np.copy(maze)
    best_solution = energyfunction(currmaze, start_cell, goal_state)

    new_solution = np.copy(currmaze)
    new_energy = best_solution

    for i in range(iterations):
        neighbor = np.copy(currmaze)

        neighbors = valid_moves(neighbor, start_cell)

        neighbor_node = random.choice(neighbors)

        neighbor_energy = energyfunction(neighbor, start_cell, goal_state)

        delta_energy = neighbor_energy - best_solution

        if delta_energy < 0 or random.random() < math.exp(-delta_energy / T):
            currmaze = np.copy(neighbor)
            best_solution = neighbor_energy

            if best_solution < new_energy:
                new_solution = np.copy(currmaze)
                new_energy = best_solution

        T = T * decay

    return new_solution, new_energy


"""
def SIMULATED_ANNEALING(maze, start_cell, goal_state, iterations, T, decay):

	currmaze = np.copy(maze)
	best_solution = energyfunction(currmaze, start_cell, goal_state)
	
	new_solution = currmaze
	new_energy = best_solution

	for i in range(iterations):
		neighbor = currmaze
		neighbors = valid_moves(neighbor, start_cell)
		neighbor_node = random.choice(neighbors)
		neighbor_energy = energyfunction(neighbor, neighbor_node, goal_state)
		
		delta_energy = neighbor_energy - best_solution
		
		if delta_energy < 0 or random.random() < math.exp(-delta_energy / T):
			 currmaze = neighbor
			 best_solution = neighbor_energy
			if best_solution < new_energy:
				new_solution = currmaze
				new_energy = best_solution

			T = T * decay

	return best_solution
"""

