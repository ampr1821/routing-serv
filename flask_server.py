from flask import Flask, request
from flask_cors import CORS, cross_origin
import osmnx as ox
from waitress import serve
from astar_routing import *
import pickle

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Load the graph
try:
    f = open('blr.bin', 'rb')
    print('Graph found, loading from disk')
    G = pickle.load(f)
    f.close()
except:
    print('Graph does not exist, downloading from internet')
    G = ox.graph_from_place("Bengaluru, India", network_type='drive')
    f = open('blr.bin', 'wb')
    pickle.dump(G, f)
    f.close()

astar = a_star(G)

@app.route("/")
@cross_origin()
def test_connection():
    print('Ping request received!')
    return "Yes, we are open!"

@app.route("/getroute")
@cross_origin()
def retRoute():
    args = request.args
    lat1 = float(args.get('lat1', None))
    lat2 = float(args.get('lat2', None))
    lon1 = float(args.get('lon1', None))
    lon2 = float(args.get('lon2', None))
    print(str(lat1) + "," + str(lon1) + "," + str(lat2) + "," + str(lon2))

    if lat1 != None and lat2 != None and lon1 != None and lon2 != None:

        path = astar.get_route((lat1, lon1), (lat2, lon2))
        path = list(path)
        returnList = []

        print(len(path))
        # print(path)

        for i in range(len(path) -1):
            edge_data = G.get_edge_data(path[i], path[i + 1])
            lon = G.nodes[path[i]]['x'] #lon
            lat = G.nodes[path[i]]['y'] #lat
            returnList.append([lat, lon])
            
            if 'geometry' in edge_data[0].keys():
                print('yes')
                for j in edge_data[0]['geometry'].wkt[12:-1].split(','):
                    t = j.split()
                    lon = t[0] #lon
                    lat = t[1] #lat
                    print(t)
                    returnList.append([lat, lon])
            
            lon = G.nodes[path[i + 1]]['x'] #lon
            lat = G.nodes[path[i + 1]]['y'] #lat
            returnList.append([lat, lon])
        
        return returnList
    else:
        return "Error! Two Lat Long pairs!"

print("Serving the app on port 5566")
serve(app, host='0.0.0.0', port=5566)