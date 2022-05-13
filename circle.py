# James Shaw
# CSCI151
# 2/7/22
# circle.py

import stddraw
import stdarray
import math
import sys
import random

debug = False

points = int(sys.argv[1])
probability = float(sys.argv[2])

point_arr = stdarray.create1D(points)

RADIUS = .25
CENTER = (.5, .5)

# optional for debugging, draws circle
if debug:
    stddraw.circle(CENTER[0], CENTER[1], RADIUS)


def make_points(point_count, center, radius):
    """Draw points of circle

    :param point_count:
    :param center:
    :param radius:
    :return:
    """
    angle = 360 / point_count
    for index, i in enumerate(range(point_count)):
        point = calculate_point(center, radius, angle * i)
        point_arr[index] = point


def calculate_point(center, radius, angle):
    """Calculate the coordinates of a point

    :param center:
    :param radius:
    :param angle:
    :return: Tuple of x, y point coordinates
    """
    arc = (angle * math.pi) / 180
    dx = radius * math.cos(arc)
    dy = radius * math.sin(arc)
    return center[0] + dx, center[1] + dy


def random_connect(point_array, probability_of_line):
    """Randomly connect each point with each-other
    based on probability_of_line

    :param point_array: Array of tuple points
    :param probability_of_line: Float probability of line
    :return:
    """
    for index, point in enumerate(point_array):
        next_index = index + 1
        while next_index < len(point_array):
            next_point = point_array[next_index]
            rand = random.random()
            if rand <= probability_of_line:
                stddraw.line(
                    point[0],
                    point[1],
                    next_point[0],
                    next_point[1])
            next_index += 1


make_points(points, CENTER, RADIUS)

stddraw.setPenColor(stddraw.GRAY)
stddraw.setPenRadius(.0005)

random_connect(point_arr, probability)

# Draw points
stddraw.setPenColor(stddraw.BLACK)
stddraw.setPenRadius(.005)
for point in point_arr:
    stddraw.point(point[0], point[1])

stddraw.show()
