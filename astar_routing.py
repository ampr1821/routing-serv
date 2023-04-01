import osmnx as ox
import networkx as nx
import sys

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
