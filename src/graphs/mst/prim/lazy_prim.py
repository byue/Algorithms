import networkx as nx
import heapq

# Runtime: O(ELog(E)) with binary heap
# Space: O(E + V)
def get_mst(graph):
    starting_node = next(iter(graph))
    mst = nx.Graph()
    visited = set([starting_node])

    # initialize priority queue with edges connecting to destination node adjacent to MST
    # (MST initially only has starting node). Heap contains edges.
    pq = [(data['weight'], u, v) for u, v, data in graph.edges(starting_node, data=True)]
    heapq.heapify(pq)
    total_cost = 0

    while pq:
        weight, prev_node, current_node = heapq.heappop(pq)
        # possibly nodes already visited since there is no deduplication of
        # destination nodes in pq.
        if current_node in visited:
            continue

        visited.add(current_node)
        mst.add_edge(prev_node, current_node, weight=weight)
        total_cost += weight

        for u, v, data in graph.edges(current_node, data=True):
            next_node = v if u == current_node else u
            if next_node not in visited:
                heapq.heappush(pq, (data['weight'], current_node, next_node))

    return total_cost, mst
