import sys
import csv
from queue import PriorityQueue
from math import radians, cos, sin, asin, sqrt

# Read CSV file and store data in a list
filename = "blr.csv"
path_data = []
with open(filename, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        path_data.append(row)

# Get start and end coordinates from command line arguments
start_lat = float(sys.argv[1])
start_lon = float(sys.argv[2])
end_lat = float(sys.argv[3])
end_lon = float(sys.argv[4])

# Define a function to calculate the great circle distance between two points on the Earth's surface
def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6371 * c
    return km

# Define a function to calculate the heuristic (i.e., estimated) distance between two points
def heuristic(lat1, lon1, lat2, lon2):
    return haversine(lat1, lon1, lat2, lon2)

# Define a class for nodes in the A* search tree
class Node:
    def __init__(self, lat, lon, g=0, h=0, parent=None):
        self.lat = lat
        self.lon = lon
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f

# Find the nearest point in the graph to the start and end coordinates
def find_nearest_point(lat, lon):
    nearest_point = None
    nearest_distance = float('inf')
    for data in path_data:
        lat1, lon1, lat2, lon2, distance = map(float, data)
        d1 = haversine(lat, lon, lat1, lon1)
        d2 = haversine(lat, lon, lat2, lon2)
        if d1 < nearest_distance:
            nearest_distance = d1
            nearest_point = (lat1, lon1)
        if d2 < nearest_distance:
            nearest_distance = d2
            nearest_point = (lat2, lon2)
    return nearest_point

start_node = Node(*find_nearest_point(start_lat, start_lon))
end_node = Node(*find_nearest_point(end_lat, end_lon))

# Initialize the A* search
# start_node = Node(start_lat, start_lon)
# end_node = Node(end_lat, end_lon)
open_set = PriorityQueue()
open_set.put(start_node)
closed_set = set()
path = []

print('starting')

# Perform the A* search
while not open_set.empty():
    current_node = open_set.get()

    if current_node.lat == end_node.lat and current_node.lon == end_node.lon:
        # If the end node has been reached, construct the path and exit the loop
        while current_node is not None:
            path.append((current_node.lat, current_node.lon))
            current_node = current_node.parent
        path.reverse()
        break

    closed_set.add((current_node.lat, current_node.lon))

    for data in path_data:
        lat1, lon1, lat2, lon2, distance = map(float, data)
        if lat1 == current_node.lat and lon1 == current_node.lon:
            neighbor_node = Node(lat2, lon2, g=current_node.g + distance, h=heuristic(lat2, lon2, end_node.lat, end_node.lon), parent=current_node)
        elif lat2 == current_node.lat and lon2 == current_node.lon:
            neighbor_node = Node(lat1, lon1, g=current_node.g + distance, h=heuristic(lat1, lon1, end_node.lat, end_node.lon), parent=current_node)
        else:
            continue

        if (neighbor_node.lat, neighbor_node.lon) in closed_set:
            continue

        open_set.put(neighbor_node)

# Print the path
for node in path:
    print(node)
