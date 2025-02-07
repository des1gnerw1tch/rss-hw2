import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
from q2poly import q2poly
from helper_functions import *
import typing

"""
CS4610/CS5335 - Spring 2025 - Homework 2

Name: Zachary Walker-Liang
Email: walker-liang.z@northeastern.edu
With Whom you discussed the questions with: Nobody yet
"""

def C1_func(robot: typing.Dict[str, typing.List[float]], q: typing.List[float], obstacles: typing.List[Polygon]) -> None:
    """ Plot the robot in the workspace.

    Parameters
    ----------
    robot : typing.Dict[str, typing.List[float]]
        A dictionary containing the 2D robot's geometric parameters. This contains links and pivots
        (joints) defining the robot's zero configuration'. The format looks like: 
            robot = {
                "link1"     :   [list of vertices for link1]
                "link2"     :   [list of vertices for link2]
                "pivot1"    :   [vertex of pivot1]
                "pivot2"    :   [vertex of pivot2]
            }
        
        The robot can be thought of as a chain, starting with pivot1, link1 connects to pivot2 ...
        Each pivot defines a coordinate frame for the respective link, with the frame origin at the
        pivot. There is no rotation component to the zero configuration of the frames. The
        coordinates of each pivot are defined in the frame of the previous link. The first pivot is
        defined in the world frame (frame 0). The links are defined as a list of vertices that form the shape
        of the link. The vertices of a link are given in the frame defined by that link's pivot.
        This robot definition is analagous to the URDF robot description format, which is commonly
        used in ROS to define a robot's geometry.

    q : typing.List[float]
        A 2-element list representing the configuration of the robot. This has the format: 
            q = [pivot_1_joint_angle, pivot_2_joint_angle]
    
    obstacles : typing.List[Polygon]
        A list of polygons representing the obstacles
    """

    ### Insert your code below:

    #plot_obstacles_robot does no transformations, you will need to compute the transformed
    #coordinates of the robot's links and pivots for the given configuration.
    
    #HINT your code here should be a single call to the funtion "q2poly"

    # example of [0,0] configuration
    shape1 = [[5.2, 3  ],\
              [5.2, 2  ],\
              [8.7, 2.1],\
              [8.7, 2.9]]
    shape2 = [[ 8.2,  2.9],\
              [ 8.2,  2.1],\
              [11.2,  2.3],\
              [11.2,  2.7]]
    pivot1 =  [6.4, 2.5]
    pivot2 =  [8.5, 2.5]

    linkShape1Transformed, linkShape2Transformed, pivot1Transformed, pivot2Transformed = q2poly(robot, q)

    plot_obstacles_robot(obstacles=obstacles, 
                         link1=linkShape1Transformed, 
                         link2=linkShape2Transformed, 
                         origin1=pivot1Transformed, 
                         origin2=pivot2Transformed)
 