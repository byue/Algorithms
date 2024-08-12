def get_weighted_shortest_paths(source, graph):
    distances = {node: 0 if node == source else float('inf') for node in graph}
    parents = {source: None}
    for _ in range(len(graph) - 1):
        for node in graph:
            for child in graph.neighbors(node):
                candidate_distance = distances[node] + graph[node][child]['weight']
                if distances[child] > candidate_distance:
                    distances[child] = candidate_distance
                    parents[child] = node
    for node in graph:
        for child in graph.neighbors(node):
            if distances[child] > distances[node] + graph[node][child]['weight']:
                return None, None
    return distances, parents