import networkx as nx
import heapq

def _visit(graph, node, included_in_mst, pq):
    included_in_mst.add(node)
    for edge in graph.edges(node, data=True):
        u, v, data = edge
        other_node = v if u == node else u
        if other_node not in included_in_mst:
            heapq.heappush(pq, (data['weight'], edge))

def get_mst(graph):
    pq = []
    starting_node = next(iter(graph))
    mst = nx.Graph()
    included_in_mst = set()
    _visit(graph, starting_node, included_in_mst, pq)
    total_cost = 0
    while len(pq) > 0:
        _, edge = heapq.heappop(pq)
        u, v, data = edge
        if u in included_in_mst and v in included_in_mst:
            continue
        mst.add_edge(u, v, weight=data['weight'])
        total_cost += data['weight']
        for node in filter(lambda node: node not in included_in_mst, [u, v]):
            _visit(graph, node, included_in_mst, pq)
    return total_cost, mst
