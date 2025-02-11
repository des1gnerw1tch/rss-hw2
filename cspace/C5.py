import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.patches import Polygon
from helper_functions import *
import typing

"""
CS4610/CS5335 - Spring 2025 - Homework 2

Name: Zachary Walker-Liang
Email: walker-liang.z@northeastern.edu
With Whom you discussed the questions with: Nobody yet
"""

def C5_func(q_grid: np.array, q_start: np.array, q_goal:np.array, c_path: typing.List[np.array]) -> typing.List[np.array]:
    """ Convert the path from indices of q_grid to actual robot configurations.

    Parameters
    ----------
    q_grid : np.array
        A R x 1 numpy array representing the grid over the angle-range. R is the resolution.
    q_start : np.array
        A 2 x 1 numpy array representing the start configuration of the robot in the format of [q1, q2].
    q_goal : np.array
        A 2 x 1 numpy array representing the goal configuration of the robot in the format of [q1, q2].
    c_path : typing.List[np.array]
        A list of 2 x 1 numpy array representing the path from the start configuration to the goal configuration using indices of q_grid.

    Returns
    -------
    typing.List[np.array]
        A list of 2 x 1 numpy array representing the path from the start configuration to the goal configuration using actual angle values.
        The first dimension is q1 and the second dimension is q2. Example: [ [q1_0 , q2_0], [q1_1, q2_1], .... ]
    """

    ### Insert your code below: ###

    q_path = []
    for index in c_path:
        # My path algorithm in C4 already includes q_start and q_goal
        q1, q2 = FindConfigurationAnglesFromConfigurationIndex(index[0], index[1], q_grid)
        q_path.append(np.array([q1, q2]))
    return q_path

# Finds the configuration angles q1, q2 from discretized angles
def FindConfigurationAnglesFromConfigurationIndex(x: int, y: int, q_grid: np.array) -> tuple[float, float]:
    return (q_grid[x], q_grid[y])