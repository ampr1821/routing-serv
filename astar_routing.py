import osmnx as ox
import networkx as nx
import sys
from astar import AStar
from haversine import haversine

class a_star(AStar):
    def __init__(self,graph):
        self.graph = graph

    def heuristic_cost_estimate(self, n1, n2) -> float:
        if isinstance(n1, int):
            n1 = self.graph.nodes[n1]['x'], self.graph.nodes[n1]['y']
        if isinstance(n2, int):
            n2 = self.graph.nodes[n2]['x'], self.graph.nodes[n2]['y']
        x1, y1 = n1
        x2, y2 = n2
        return haversine((y1, x1), (y2, x2))

    def distance_between(self, n1, n2):
        if 'length' in self.graph[n1][n2]:
            return self.graph[n1][n2]['length']
        else:
            return 99999999 # return a large number if 'length' attribute is not present

    def neighbors(self, node):
        return list(self.graph.neighbors(node))

if __name__ == "__main__":
    
    if(len(sys.argv) < 5):
        print('Enter two lat long pairs!')
        exit(-1)

    # create the points
    point1 = (float(sys.argv[1]), float(sys.argv[2]))
    point2 = (float(sys.argv[3]), float(sys.argv[4]))

    # create the graph
    # 12.903203, 77.648572 12.912441, 77.632885
    G = ox.graph_from_place("HSR ,Bengaluru, India", network_type='drive')
    start_node = ox.distance.nearest_nodes(G, point1[1], point1[0])
    goal_node = ox.distance.nearest_nodes(G, point2[1], point2[0])
    astar = a_star(G)
    path = astar.astar(start_node, goal_node)
    path = list(path)

    for i in path:
        lon = G._node[i]['x'] #lon
        lat = G._node[i]['y'] #lat
        print(str(lat) + ","+str(lon))

    sys.stdout.flush()
# command to run (Windows)
# python get_route.py 12.9246572 77.5582014 13.0110216 77.6747875
#hsr 
# python get_route.py 12.909229431138986 77.63947874679494 12.914080814688852 77.64155496935096
# command to run (Linux)
# python3 get_route.py 12.9246572 77.5582014 13.0110216 77.6747875
