import heapq

def get_weighted_shortest_paths(source, graph):
    distances = {node: 0 if node == source else float('inf') for node in graph}
    parents = {source: None}
    visited = set([source])
    heap = []
    heapq.heappush(heap, (0, source))
    while heap:
        (_, node) = heapq.heappop(heap)
        visited.add(node)
        for child in graph.neighbors(node):
            if child not in visited:
                candidate_distance = distances[node] + graph[node][child]['weight']
                if distances[child] > candidate_distance:
                    distances[child] = candidate_distance
                    parents[child] = node
                    heapq.heappush(heap, (candidate_distance, child))
    return distances, parents