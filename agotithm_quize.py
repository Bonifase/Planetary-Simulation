from importlib.resources import path
from itertools import count
import sys

letters = [chr(i) for i in range(65, 91)]
fmt = ('{:2s}') * 4

# for fn in zip(*[iter(letters + [' ']*5)]*4):
#     sys.stdout.write(' '*10)
#     print(fmt.format(*fn))

"""
A competitive runner would like to create a route that starts and ends at his house, 
with the condition that the route goes entirely uphill at first, and then entirely downhill.

Given a dictionary of places of the form {location: elevation}, and a dictionary mapping paths
between some of these locations to their corresponding distances, find the length of the shortest 
route satisfying the condition above. Assume the runner's home is location 0.

For example, suppose you are given the following input:
elevations = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
paths = {
    (0, 1): 10,
    (0, 2): 8,
    (0, 3): 15,
    (1, 3): 12,
    (2, 4): 10,
    (3, 4): 5,
    (3, 0): 17,
    (4, 0): 10
}
In this case, the shortest valid path would be 0 -> 2 -> 4 -> 0, with a distance of 28.
"""

elevations = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
paths = {
    (0, 1): 10,
    (0, 2): 8,
    (0, 3): 15,
    (1, 3): 12,
    (2, 4): 10,
    (3, 4): 5,
    (3, 0): 17,
    (4, 0): 10
}

def shortest_path_dfs(elevations, paths):
    shortest_distance = count = 0
    running_distance = float('inf')
    path = values = []
    for key, value in elevations.items():
        count += 1
        if count + 1 == len(elevations):
            shortest_distance += value
            break
        path = [i for i in paths.keys() if key == i[0]]
        values = [v for k, v in paths.items() if k in path]
        # print(key, values)
        if min(values) > running_distance:
            continue
        else: 
            running_distance = min(values)
        # print(running_distance)
        shortest_distance += running_distance
        # print("================================")
    print(shortest_distance)

# shortest_path_dfs(elevations, paths)
# 
"""
You are a hiker preparing for an upcoming hike. You are given heights, 
a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col).
You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, 
(rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish 
to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the 
route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
""" 