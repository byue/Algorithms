import networkx as nx
import heapq

def get_mst(graph):
    starting_node = next(iter(graph))
    mst = nx.Graph()
    visited = set([starting_node])
    pq = [(data['weight'], u, v) for u, v, data in graph.edges(starting_node, data=True)]
    heapq.heapify(pq)
    total_cost = 0
    while pq:
        weight, prev_node, current_node = heapq.heappop(pq)
        if current_node not in visited:
            visited.add(current_node)
            mst.add_edge(prev_node, current_node, weight=weight)
            total_cost += weight
            for u, v, data in graph.edges(current_node, data=True):
                next_node = v if u == current_node else u
                if next_node not in visited:
                    heapq.heappush(pq, (data['weight'], current_node, next_node))
    return total_cost, mst
