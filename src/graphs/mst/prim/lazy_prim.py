import networkx as nx
import heapq

# Runtime: O(ELog(E)) with binary heap, without decrease-key
# E insert's, each costing O(Log(E)), so O(ELog(E))
# E delete min's, each costing O(Log(E)), so O(ELog(E))
# Space: O(E + V), visited is per node, priority queue has entries per edge (destination node can have multiple entries)
def get_mst(graph):
    starting_node = next(iter(graph))
    mst = nx.Graph()
    visited = set([starting_node])

    # initialize priority queue with edges connecting to destination node adjacent to MST
    # (MST initially only has starting node). Heap contains edges.
    pq = [(graph[starting_node][next_node]['weight'], starting_node, next_node) for next_node in graph.neighbors(starting_node)]
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

        for next_node in graph.neighbors(current_node):
            if next_node not in visited:
                heapq.heappush(pq, (graph[current_node][next_node]['weight'], current_node, next_node))

    return total_cost, mst
