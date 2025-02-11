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

Name: Zachary Walker-Liang
Email: walker-liang.z@northeastern.edu
With Whom you discussed the questions with: Nobody yet
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

    plt.xlim([0, 12])
    plt.ylim([0, 12])
    plt.axis('square')

    ax.set_title("Swept Volume Collisions")

    for i in range(len(q_path)):
        if (i - 1 < 0):
            continue
        arm1Verts, arm2Verts, pivot1, pivot2 = q2poly(robot, q_path[i]) # Arm 1 and 2
        prevArm1Verts, prevArm2Verts, prevPivot1, prevPivot2 = q2poly(robot, q_path[i - 1])
        foundCollision, convexHullArm1, convexHullArm2 = IsConvexHullIntersectingWithObstacles(arm1Verts, arm2Verts, prevArm1Verts, prevArm2Verts, obstacles)
        if (foundCollision):
            PlotPolygonsToAx(obstacles, convexHullArm1.tolist(), convexHullArm2.tolist(), ax)
            num_collisions+=1
    # DO NOT CALL plt.show() inside this function. It is called in hw2_cspace.py
    return num_collisions, fig    


def IsConvexHullIntersectingWithObstacles(arm1Verts: np.array,
                                        arm2Verts: np.array, 
                                        prevArm1Verts: np.array,
                                        prevArm2Verts: np.array,
                                        obstacles: typing.List[Polygon]) -> tuple[bool, np.array, np.array]:
                                        
    obstaclePolygons = []
    for obstacle in obstacles:
        obstaclePolygons.append(Polygon_shapely(obstacle))
    
    unionArm1 = shapely.union(Polygon_shapely(arm1Verts), Polygon_shapely(prevArm1Verts))
    unionArm2 = shapely.union(Polygon_shapely(arm2Verts), Polygon_shapely(prevArm2Verts))
    convexHull1 = shapely.convex_hull(unionArm1)
    convexHull2 = shapely.convex_hull(unionArm2)
    for obstacle in obstaclePolygons:
        if obstacle.intersects(convexHull1) or obstacle.intersects(convexHull2):
            return True, np.array(list(convexHull1.exterior.coords)), np.array(list(convexHull2.exterior.coords))
    
    return False, np.array(list(convexHull1.exterior.coords)), np.array(list(convexHull2.exterior.coords))
    
    

def PlotPolygonsToAx(obstacles: typing.List[Polygon],
                     arm1Hull: typing.List[typing.List[float]],
                     arm2Hull: typing.List[typing.List[float]], 
                     ax) -> None:
    for i in range(len(obstacles)):
        coord = obstacles[i]
        p = Polygon(coord, facecolor = 'k')
        ax.add_patch(p)
    
    arm1Hull_p = Polygon(arm1Hull, facecolor = 'r', alpha=0.3)
    arm1Hull_p = ax.add_patch(arm1Hull_p)

    arm2Hull_p = Polygon(arm2Hull, facecolor = 'b', alpha=0.3)
    arm2Hull_p = ax.add_patch(arm2Hull_p)