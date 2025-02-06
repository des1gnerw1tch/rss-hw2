import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.patches import Polygon
from matplotlib.figure import Figure
from helper_functions import *
from q2poly import q2poly
import shapely
from shapely.geometry import Polygon as Polygon_shapely
from shapely import MultiPoint
import typing

"""
CS4610/CS5335 - Spring 2025 - Homework 2

Name:
Email:
With Whom you discussed the questions with:
"""

def C6_func(robot: typing.Dict[str, typing.List[float]], 
            q_path: typing.List[np.array], 
            obstacles: typing.List[Polygon]) -> typing.Tuple[int, Figure]:
    """Calculate the number of collisions that occur along the path, and generate a visualization.
    The visualization should be passed as a matplotlib figure to the outer hw2_cspace.py function.
    
    Parameters
    ----------
    robot : typing.Dict[str, typing.List[float]]
        A dictionary containing the robot's parameters.
    q_path : typing.List[np.array]
       A list of 2 x 1 numpy array representing the path from the start configuration to the goal 
       configuration using actual angle values.
    obstacles : typing.List[Polygon]
        A list of polygons representing the obstacles.

    Returns
    -------
    num_collisions : int
        The number of collisions that occur along the path.
    figure : matplotlib.figure.Figure
        Figure showing swept volume collisions

    """

    ### Insert your code below: ###
    num_collisions: int = 0
    fig, ax = plt.subplots()
    ax.set_title("Swept Volume Collisions")
    # DO NOT CALL plt.show() inside this function. It is called in hw2_cspace.py

    return num_collisions, fig