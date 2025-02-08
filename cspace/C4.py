import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.patches import Polygon
from helper_functions import *
import typing
from C3 import FindNearestIndex

"""
CS4610/CS5335 - Spring 2025 - Homework 2

Name: Zachary Walker-Liang
Email: walker-liang.z@northeastern.edu
With Whom you discussed the questions with: Nobody yet
"""

def C4_func(distances: np.array,q_grid: np.array, q_start: np.array) -> typing.List[np.array]:
    """Using the distance array from C3, find the optimal path from the start configuration to the goal configuration (zero value).

    Parameters
    ----------
    distances : np.array
        A 2D numpy array representing the distance from each cell in the configuration space to the goal configuration.
        This is given by C3 
    q_grid : np.array
        A R x 1 numpy array representing the grid over the angle-range. R is the resolution.
    q_start : np.array
        A 2 x 1 numpy array representing the start configuration of the robot in the format of [q1, q2].

    Returns
    -------
    typing.List[np.array]
        A list of 2 x 1 numpy array representing the path from the start configuration to the goal configuration using indices of q_grid.
        Example: [ [q1_0 , q2_0], [q1_1, q2_1], .... ]
    """

    ### Insert your code below: ###
    startingPosition = FindNearestIndex(q_start, q_grid)
    distanceAwayFromGoal = distances[startingPosition[0]][startingPosition[1]]
    path = []
    path.append(np.array([startingPosition[0], startingPosition[1]]))

    currentPosition = startingPosition
    while (distanceAwayFromGoal != 0):
        nearestNeighbor = None
        nearestNeighborDistanceFromGoal = math.inf
        for i in range(-1, 2): # Explore surrounding nodes
            for j in range(-1, 2):
                neighborXCoord = currentPosition[0] + i
                neighborYCoord = currentPosition[1] + j
                # Do not attempt to explore nodes that are out of bounds
                if (neighborXCoord >= distances.shape[0] or neighborXCoord < 0 or neighborYCoord >= distances.shape[1] or neighborYCoord < 0):
                    continue
                
                neighborDistanceFromGoal = distances[neighborXCoord, neighborYCoord]
                # Find the neighbor that is closest to goal
                if (nearestNeighborDistanceFromGoal > neighborDistanceFromGoal):
                    nearestNeighbor = (neighborXCoord, neighborYCoord)
                    nearestNeighborDistanceFromGoal = neighborDistanceFromGoal
        currentPosition = nearestNeighbor
        distanceAwayFromGoal = nearestNeighborDistanceFromGoal
        path.append(np.array([nearestNeighbor[0], nearestNeighbor[1]]))
    return path
