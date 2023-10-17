import sys
import numpy as np
import random
from BFS import BFS
from ASTAR import ASTAR
from VALID_MOVES import valid_moves


def energyfunction(maze, start, goal):

    not_reachable = np.sum(BFS(maze, start) == -1)
    astar = len(ASTAR(maze, start, goal))

    energy = astar + not_reachable

    return energy



"""
def HILLDESCENT(maze, start_cell, goal_state, iterations):

    best_solution = (np.copy(maze), energyfunction(
        maze, start_cell, goal_state))

    for i in range(iterations):
        currmaze = np.copy(maze)
        currvalue = energyfunction(
            maze, start_cell, goal_state)

        neighbors = valid_moves(currmaze, start_cell)
        neighbor = random.choice(neighbors)

        next_energy = energyfunction(neighbor, start_cell, goal_state)

        if next_energy < currvalue:
            best_solution = (neighbor, next_energy)

        return best_solution
"""


def HILLDESCENT(maze, start_cell, goal_state, iterations):
    best_solution = (np.copy(maze), energyfunction(
        maze, start_cell, goal_state))

    for i in range(iterations):
        currmaze = np.copy(best_solution[0])
        currvalue = best_solution[1]

        neighbors = valid_moves(currmaze, start_cell)
        neighbor = random.choice(neighbors)

        next_energy = energyfunction(
            currmaze, start_cell, goal_state)

        if next_energy < currvalue:
            best_solution = (np.copy(neighbor), next_energy)

    return best_solution


'''

def HILLDESCENT_RANDOM_RESTART(maze, start_cell, goal_state, iterations, num_searches):

    best_solution = None

    for i in range(num_searches):
        currmaze = np.copy(maze)
        current_solution = (np.copy(currmaze), energyfunction(
            currmaze, start_cell, goal_state))

        for j in range(iterations):
            currvalue = current_solution[1]

            neighbors = valid_moves(currmaze, start_cell)

            neighbor = random.choice(neighbors)

            next_energy = energyfunction(neighbor, start_cell, goal_state)

            if next_energy < currvalue:
                current_solution = (np.copy(neighbor), next_energy)

        if best_solution is None or current_solution[1] < best_solution[1]:
            best_solution = current_solution

    return best_solution
'''

def HILLDESCENT_RANDOM_RESTART(maze, start_cell, goal_state, iterations, num_searches):
    best_solution = None
    for search in range(num_searches):
        currmaze = np.copy(maze)
        current_solution = (np.copy(currmaze), energyfunction(
            currmaze, start_cell, goal_state))

        for iteration in range(iterations):
            currmaze = np.copy(current_solution[0])
            currvalue = current_solution[1]

            neighbors = valid_moves(currmaze, start_cell)

            if not neighbors:
                break

            neighbor = random.choice(neighbors)

            next_energy = energyfunction(
                currmaze, start_cell, goal_state)  

            if next_energy < currvalue:
                current_solution = (np.copy(neighbor), next_energy)

        if best_solution is None or current_solution[1] < best_solution[1]:
            best_solution = current_solution

    return best_solution


"""
def HILLDESCENT_RANDOM_RESTART(maze, start_cell, goal_state, iterations, num_searches):
    best_solution = None
    for search in range(num_searches):
        currmaze = np.copy(maze)
        current_solution = (np.copy(currmaze), energyfunction(
            currmaze, start_cell, goal_state))

        for iteration in range(iterations):
            currmaze = np.copy(current_solution[0])
            currvalue = current_solution[1]

            neighbors = valid_moves(currmaze, start_cell)

            if not neighbors:
                print(
                    f"Search {search + 1}, Iteration {iteration + 1}: No valid neighbors found. Terminating.")
                break

            neighbor = random.choice(neighbors)

            next_energy = energyfunction(neighbor, start_cell, goal_state)

            if next_energy < currvalue:
                current_solution = (np.copy(neighbor), next_energy)
                print(
                    f"Search {search + 1}, Iteration {iteration + 1}: Improved solution found. Energy: {next_energy}")

        if best_solution is None or current_solution[1] < best_solution[1]:
            best_solution = current_solution
            print(
                f"Search {search + 1}: New best solution found. Energy: {best_solution[1]}")

    return best_solution
"""



def HILLDESCENT_RANDOM_UPHILL(maze, start_cell, goal_state, iterations, probability):
    best_solution = None

    for _ in range(iterations):
        currmaze = np.copy(maze)
        current_solution = (np.copy(currmaze), energyfunction(
            currmaze, start_cell, goal_state))

        for _ in range(iterations):
            currvalue = current_solution[1]

            neighbors = valid_moves(currmaze, start_cell)

            if not neighbors:
                break

            neighbor = random.choice(neighbors)

            next_energy = energyfunction(currmaze, start_cell, goal_state)

            newprob = random.random()

            if next_energy < currvalue or newprob < probability:
                current_solution = (np.copy(neighbor), next_energy)

        if best_solution is None or current_solution[1] < best_solution[1]:
            best_solution = current_solution

    return best_solution


