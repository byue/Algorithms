from collections import deque

def get_sssp(source, graph):
    distances = {node: 0 if node == source else float('inf') for node in graph}
    parents = {source: None}
    queue = deque([source])
    in_queue = set([source])
    relax_count = {node: 0 for node in graph}

    while queue:
        node = queue.popleft()
        in_queue.remove(node)

        for child in graph.neighbors(node):
            candidate_distance = distances[node] + graph[node][child]['weight']

            # shorter distance found, relax distance
            if distances[child] > candidate_distance:
                distances[child] = candidate_distance
                parents[child] = node

                # avoid redundant processing of node in queue
                if child not in in_queue:
                    queue.append(child)
                    in_queue.add(child)
                    relax_count[child] += 1

                    # negative cycle found
                    if relax_count[child] > len(graph):
                        return None, None

    return distances, parents