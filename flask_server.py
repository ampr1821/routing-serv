from flask import Flask, request
import osmnx as ox
from waitress import serve
from astar_routing import *

app = Flask(__name__)

# Load the graph
G = ox.graph_from_place("HSR, Bengaluru, India", network_type='drive')
astar = a_star(G)

@app.route("/")
def test_connection():
    return "Yes, we are open!"

@app.route("/getroute")
def retRoute():
    args = request.args
    lat1 = args.get('lat1', None)
    lat2 = args.get('lat2', None)
    lon1 = args.get('lon1', None)
    lon2 = args.get('lon2', None)

    if lat1 != None:
        start_node = ox.distance.nearest_nodes(G, lat1, lon1)
        goal_node = ox.distance.nearest_nodes(G, lat2, lon2)
        path = astar.astar(start_node, goal_node)
        # path = list(path)
        returnList = []

        for i in path:
            lon = G._node[i]['x'] #lon
            lat = G._node[i]['y'] #lat
            returnList.append([lat, lon])
            # print(str(lat) + "," + str(lon))
        
        return returnList
    else:
        return "Error! Two Lat Long pairs!"

print("Serving the app")
serve(app, host='0.0.0.0', port=5566)