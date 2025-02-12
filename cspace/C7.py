import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.patches import Polygon
from helper_functions import *

"""
CS4610/CS5335 - Spring 2025 - Homework 2

Name: Zachary Walker-Liang
Email: walker-liang.z@northeastern.edu
With Whom you discussed the questions with: Oliver Hugh and Kellan Mccarthy
"""

def C7_func(cspace: np.array) -> np.array:
    """Pad the configuration space by one grid cell.

    Parameters
    ----------
    cspace : np.array
        The origianl configuration space of the robot.

    Returns
    -------
    np.array
        The padded configuration space of the robot.
    """

    ### Insert your code below: ###

    padded_cspace = cspace.copy()
    for row in range(cspace.shape[0]):
        for col in range(cspace.shape[1]):
            if (padded_cspace[row][col] == 1):
                continue
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if row + i < 0 or row + i >= cspace.shape[0] or col + j < 0 or col + j >= cspace.shape[1]:
                        continue
                    if (cspace[row + i][col + j] == 1): # If neighbor is a wall
                        padded_cspace[row][col] = 1
    return padded_cspace