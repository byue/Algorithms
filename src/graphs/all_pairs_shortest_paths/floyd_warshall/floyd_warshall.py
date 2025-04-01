def get_apsp(graph):
    """All-pairs shortest paths using Floyd-Warshall.
    Returns a dictionary: {node: (distance_dict, parent_dict)}.
    """
    dist = {u: {v: float('inf') for v in graph} for u in graph}
    parent = {u: {} for u in graph}

    # Initialize distances and parents
    for u in graph:
        dist[u][u] = 0
        parent[u][u] = None
    for u, v, data in graph.edges(data=True):
        dist[u][v] = graph[u][v]['weight']
        parent[u][v] = u

    # Floyd-Warshall core algorithm
    for k in graph:
        for i in graph:
            for j in graph:
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    new_dist = dist[i][k] + dist[k][j]
                    if new_dist < dist[i][j]:
                        dist[i][j] = new_dist
                        parent[i][j] = parent[k][j]  # Update parent for path reconstruction

    # Detect negative cycles
    for i in graph:
        if dist[i][i] < 0:
            return None  # Negative cycle detected

    # Construct final result as {node: (distance_dict, parent_dict)}
    result = {u: (dist[u], parent[u]) for u in graph}
    return result