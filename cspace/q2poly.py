import numpy as np
import typing
import enum

"""
CS4610/CS5335 - Spring 2025 - Homework 2

Name: Zachary Walker-Liang
Email: walker-liang.z@northeastern.edu
With Whom you discussed the questions with: Nobody yet
"""

def q2poly(robot: typing.Dict[str, typing.List[float]], q: typing.List[float]) -> typing.Tuple[np.array, np.array, np.array, np.array]:
    """ A function that takes in the robot's parameters and a configuration and 
    returns the vertices of the robot's links after transformation and the pivot points of the links after transformation

    Parameters
    ----------
    robot : typing.dict[str, typing.List[float]]
        A dictionary containing the robot's parameters
    q : typing.List[float]
        A 2-element list representing the configuration of the robot

    Returns
    -------
    typing.Tuple[np.array, np.array, np.array, np.array]
        np.array: 
            a numpy array representing the vertices of the first link of the robot after transformation
        np.array: 
            a numpy array representing the vertices of the second link of the robot after transformation
        np.array: 
            a numpy array representing the pivot point of the first link of the robot after transformation
        np.array: 
            a numpy array representing the pivot point of the second link of the robot after transformation
    """


    ### Insert your code below: ###

    # The configuration of the arm is given by q = (q1, q2), where q1 is the angle between frame
    # 0’s x axis and frame 1’s x axis, and q2 is the angle between frame 1’s x axis and frame 2’s x axis. Both joints may
    # rotate between 0 and 2π radians. For example, the start configuration below is qstart = (0.85, 0.9), and the goal
    # configuration is qgoal = (3.05, 0.05).
    
    # (len(robot["link1"]) is 5, each polygon has 5 vertices where the 1st and 5th are the same, so that the polygon is closed
    # when drawing (I believe).
    pivot1 = np.array(robot["pivot1"]) # Pivot 1 never will change
    shape1 = np.array(robot["link1"])
    shape1 = RowVectorsToColumnVectorsWithHomogeneousCoord(shape1)
    shape1 = Get2DRotation(q[0]) @ shape1 # Rotate shape1 around the first pivot
    shape1 = ColumnVectorsToRowVectorsWithoutHomogeneousCoord(shape1)

    pivot2 = np.array(robot["pivot2"]).reshape(1, -1) # Reshape becuase numpy wants to make it an array instead of row vector 
    pivot2 = RowVectorsToColumnVectorsWithHomogeneousCoord(pivot2)
    pivot2 = Get2DRotation(q[0]) @ pivot2 #Pivot 2 is rotated around Pivot 1
    pivot2 = ColumnVectorsToRowVectorsWithoutHomogeneousCoord(pivot2)
    pivot2 = pivot2[0] # Extracts only the first row, as this is a row vector in a 2D array

    shape2 = np.array(robot["link2"]) # Should be rotated around pivot 1 # Should be rotated around first pivot 1 then pivot 2
    
    return shape1, shape2, pivot1, pivot2

def RowVectorsToColumnVectorsWithHomogeneousCoord(points: np.array):
    return np.vstack((points.T, np.ones((1, points.shape[0]))))

def ColumnVectorsToRowVectorsWithoutHomogeneousCoord(points: np.array):
    return np.delete(points, -1, axis=0).T



# Returns an rotation matrix, which will work on column vectors
def Get2DRotation(radians: float) -> np.array:
    if (radians < 0 or radians > 2 * np.pi):
        raise ValueError("Cannot rotate past 2pi degrees or less than 2pi degrees")

    return np.array([
        [np.cos(radians), -np.sin(radians), 0],
        [np.sin(radians), np.cos(radians), 0],
        [0, 0, 1]])

class Axis(enum.Enum):
    X = 1
    Y = 2
    Z = 3

# Returns an rotation matrix, which will work on column vectors
# FIXME: I got a little too excited and did 3D rotation before I realized it was only 2D rotation, though this 
# might be useful later.. 
def GetRotation(axis: Axis, radians: float) -> np.array:
    if (radians < 0 or radians > 2 * np.pi):
        raise ValueError("Cannot rotate past 2pi degrees or less than 2pi degrees")
    
    if (axis == Axis.X):
        return np.array([
                [1, 0, 0],
                [0, np.cos(radians), -np.sin(radians)],
                [0, np.sin(radians), np.cos(radians)]])
    elif (axis == Axis.Y):
        return np.array([
                [np.cos(radians), 0, np.sin(radians)],
                [0, 1, 0],
                [-np.sin(radians), 0, np.cos(radians)]])
    elif (axis == Axis.Z):
        return np.array([
                [np.cos(radians), -np.sin(radians), 0],
                [np.sin(radians), np.cos(radians), 0],
                [0, 0, 1]])