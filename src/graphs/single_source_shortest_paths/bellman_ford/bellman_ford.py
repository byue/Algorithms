def get_sssp(source, graph):
    distances = {node: 0 if node == source else float('inf') for node in graph}
    parents = {source: None}

    for _ in range(len(graph) - 1):
        has_converged = True
        for node in graph:
            for child in graph.neighbors(node):
                candidate_distance = distances[node] + graph[node][child]['weight']

                # found a better distance to child, relax distance
                if distances[child] > candidate_distance:
                    distances[child] = candidate_distance
                    parents[child] = node
                    has_converged = False

        # Terminate early if distances stop updating after a pass
        if has_converged:
            break

    # Check for negative cycles
    for node in graph:
        for child in graph.neighbors(node):
            if distances[child] > distances[node] + graph[node][child]['weight']:
                return None, None

    return distances, parents