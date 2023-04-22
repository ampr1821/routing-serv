import networkx as nx

def all_paths_dfs(G, source, target):
    # Define a recursive function to traverse the graph and find all paths
    def dfs_paths(G, source, target, path=[]):
        path = path + [source]
        if source == target:
            return [path]
        paths = []
        for neighbor in G.successors(source):
            if neighbor not in path:
                new_paths = dfs_paths(G, neighbor, target, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths
    
    # Call the dfs_paths function and return the result
    return dfs_paths(G, source, target)

# Create a MultiDiGraph
G = nx.MultiDiGraph()

# Add nodes and edges to the graph
G.add_nodes_from([1, 2, 3, 4, 5])
G.add_edges_from([(1,2), (1,3), (2,3), (2,4), (3,4), (4,5), (5,1)])

# Call the all_paths_dfs function and print the result
source = 1
target = 5
all_paths = all_paths_dfs(G, source, target)
print(all_paths)
