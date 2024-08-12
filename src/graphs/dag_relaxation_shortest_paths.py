from src.graphs.dfs import dfs_recursive_topo_sort

def get_weighted_shortest_paths(source, graph):
    distances = {node: 0 if node == source else float('inf') for node in graph}
    parents = {source: None}
    topo_order_nodes = dfs_recursive_topo_sort(graph)
    for node in topo_order_nodes:
        for child in graph.neighbors(node):
            candidate_distance = distances[node] + graph[node][child]['weight']
            if distances[child] > candidate_distance:
                distances[child] = candidate_distance
                parents[child] = node
    return distances, parents
