import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.patches import Polygon
from helper_functions import *
import typing
from collections import deque

"""
CS4610/CS5335 - Spring 2025 - Homework 2

Name: Zachary Walker-Liang
Email: walker-liang.z@northeastern.edu
With Whom you discussed the questions with:  Oliver Hugh and Kellan Mccarthy
"""

def C3_func(robot: typing.Dict[str, typing.List[float]], cspace: np.array,q_grid: np.array, q_goal: np.array) -> np.array:
    """Create a new 2D array that shows the distance from each point in the configuration space to the goal configuration.

    Parameters
    ----------
    robot : typing.Dict[str, typing.List[float]]
        A dictionary containing the robot's parameters
    cspace : np.array
        The configuration space of the robot given by C2. The first dimension is q1 and the second dimension is q2. Example: [q1, q2]
    q_grid : np.array
        A R x 1 numpy array representing the grid over the angle-range. R is the resolution.
    q_goal : np.array
        A 2 x 1 numpy array representing the goal configuration of the robot in the format of [q1, q2].

    Returns
    -------
    np.array
       A 2D numpy array representing the distance from each cell in the configuration space to the goal configuration. 
       The first dimension is q1 and the second dimension is q2. Example: [q1, q2]
    """

    ### Insert your code below: ###
    distances = np.full((cspace.shape[0], cspace.shape[1]), np.inf)
    exploreQueue = deque()
    goalIndex = FindNearestIndex(q_goal, q_grid)
    exploreQueue.append(goalIndex)
    distances[goalIndex[0]][goalIndex[1]] = 0
    
    while len(exploreQueue) > 0:
        nodeToExplore = exploreQueue.popleft()
        #print("Current explore queue: ")
        #print(exploreQueue)
        #print("XXXXXXXXXXXXXX")
        #print("Exploring node " + str(nodeToExplore))
        for i in range(-1, 2): # Explore surrounding nodes
            for j in range(-1, 2):
                neighborXCoord = nodeToExplore[0] + i
                neighborYCoord = nodeToExplore[1] + j
                # Do not attempt to explore nodes that are out of bounds
                if (neighborXCoord >= cspace.shape[0] or neighborXCoord < 0 or neighborYCoord >= cspace.shape[1] or neighborYCoord < 0):
                    continue
                # If this neighboring node has not been explored and is not intersecting with obstacle
                if np.isinf(distances[neighborXCoord, neighborYCoord]) and cspace[neighborXCoord][neighborYCoord] == 0:
                    distances[neighborXCoord, neighborYCoord] = distances[nodeToExplore[0], nodeToExplore[1]] + 1 # Update distance for this neighbor
                    exploreQueue.append((neighborXCoord, neighborYCoord)) # Add neighbor to be explored later
                    
    return distances

# Returns the index that is closest from q_grid values and q_goal
def FindNearestIndex(q_goal: np.array, q_grid: np.array) -> tuple[int, int]:
    closestPoint =[-1, -1]
    closestDiscreteQ1ValueToGoal = math.inf
    closestDiscreteQ2ValueToGoal = math.inf
    for i in range(len(q_grid)):
        for j in range(len(q_grid)):
            #print("q goal")
            #print(str(q_goal[0]) + " " + str(q_goal[1]))
            #print("q grid value")
            #print(str(q_grid[i]) + " " + str(q_grid[j]))
            q1Difference = abs(q_goal[0] - q_grid[i])
            if  q1Difference < closestDiscreteQ1ValueToGoal:
                closestDiscreteQ1ValueToGoal = q1Difference
                closestPoint[0] = i
            
            q2Difference = abs(q_goal[1] - q_grid[j])
            if q2Difference < closestDiscreteQ2ValueToGoal:
                closestDiscreteQ2ValueToGoal = q2Difference
                closestPoint[1] = j
    return (closestPoint[0], closestPoint[1])