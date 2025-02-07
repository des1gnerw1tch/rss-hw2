import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
from shapely.geometry import Polygon as Polygon_shapely
from helper_functions import *
from q2poly import q2poly
import typing

"""
CS4610/CS5335 - Spring 2025 - Homework 2

Name: Zachary Walker-Liang
Email: walker-liang.z@northeastern.edu
With Whom you discussed the questions with: Nobody yet
"""

def C2_func(robot: typing.Dict[str, typing.List[float]], cspace: np.array, obstacles: typing.List[Polygon],q_grid: np.array) -> np.array:
    """Create the configuration space for the robot with the given obstacles in the given empty cspace array.

    Parameters
    ----------
    robot : typing.Dict[str, typing.List[float]]
        A dictionary containing the robot's parameters
    cspace : np.array
        An empty 2D numpy array
    obstacles : typing.List[Polygon]
        A list of polygons representing the obstacles
    q_grid : np.array
        A R x 1 numpy array representing the grid over the angle-range. R is the resolution.

    Returns
    -------
    np.array
        A 2D numpy array representing the updated configuration space. The first dimension is q1 and the second dimension is q2. Example: [q1, q2]
    """
    for i in range(len(q_grid)):
        for j in range(len(q_grid)):
            cspace[i, j] = IsConfigurationIntersectingWithObstacle(robot, q_grid[i], q_grid[j], obstacles)

    return cspace

def IsConfigurationIntersectingWithObstacle(robot: typing.Dict[str, typing.List[float]], q1, q2, obstacles: typing.List[Polygon]) -> bool:
    obstaclePolygons = []
    for obstacle in obstacles:
        obstaclePolygons.append(Polygon_shapely(obstacle))

    robotPolygons = []
    linkShape1Transformed, linkShape2Transformed, pivot1, pivot2 = q2poly(robot, [q1, q2])
    robotPolygons.append(Polygon_shapely(linkShape1Transformed))
    robotPolygons.append(Polygon_shapely(linkShape2Transformed))

    for oPoly in obstaclePolygons:
        for rPoly in robotPolygons:
            if (oPoly.intersects(rPoly)):
                return True
    return False
