from flask import Flask, request
from flask_cors import CORS, cross_origin
import osmnx as ox
from waitress import serve
from astar_routing import *

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
@cross_origin()
def test_connection():
    return "Yes, we are open!"

@app.route("/getroute")
@cross_origin()
def retRoute():
    args = request.args
    lat1 = float(args.get('lat1', None))
    lat2 = float(args.get('lat2', None))
    lon1 = float(args.get('lon1', None))
    lon2 = float(args.get('lon2', None))
    print('Request received!')

    if lat1 != None:

        # Load the graph
        G = ox.graph_from_place("HSR, Bengaluru, India", network_type='drive')
        start_node = ox.distance.nearest_nodes(G, lat1, lon1)
        goal_node = ox.distance.nearest_nodes(G, lat2, lon2)

        astar = a_star(G)

        path = astar.astar(start_node, goal_node)
        path = list(path)
        returnList = []

        print(len(path))

        for i in path:
            lon = G._node[i]['x'] #lon
            lat = G._node[i]['y'] #lat
            returnList.append([lat, lon])
            # print(str(lat) + "," + str(lon))
        
        return returnList
    else:
        return "Error! Two Lat Long pairs!"

print("Serving the app on port 5566")
serve(app, host='0.0.0.0', port=5566)