import networkx as nx
from collections import deque

def ford_fulkerson(graph, source, sink):
    def get_augmenting_path(residual, source, sink):
        parents = {source: None}
        queue = deque([source])
        while queue:
            node = queue.popleft()
            for child in residual.neighbors(node):
                if child not in parents and residual[node][child]['weight'] > 0:
                    parents[child] = node
                    queue.append(child)
                    if child == sink:
                        path = deque()
                        while child:
                            if parents[child]:
                                path.appendleft((parents[child], child))
                            child = parents[child]
                        return path
        return None
    def find_min_cut(graph, source, residual):
        reachable = set([source])
        queue = deque([source])
        while queue:
            node = queue.popleft()
            for neighbor in residual.neighbors(node):
                if residual[node][neighbor]['weight'] > 0 and neighbor not in reachable:
                    reachable.add(neighbor)
                    queue.append(neighbor)
        min_cut_edges = set()
        for u, v in graph.edges():
            if u in reachable and v not in reachable:
                min_cut_edges.add((u, v))
        source_nodes = reachable
        sink_nodes = set(graph.nodes()) - reachable
        return min_cut_edges, source_nodes, sink_nodes

    residual = nx.DiGraph()
    flows = {}
    for u, v in graph.edges():
        # forward edge initial residual flow is capacity, backward edge 0
        flows[(u, v)] = 0
        flows[(v, u)] = 0
        residual.add_edge(u, v, weight=graph[u][v]['weight'])
        residual.add_edge(v, u, weight=0)
    max_flow = 0
    while augmenting_path := get_augmenting_path(residual, source, sink):
        bottleneck = min(residual[u][v]['weight'] for u, v in augmenting_path)
        for u, v in augmenting_path:
            residual[u][v]['weight'] -= bottleneck
            residual[v][u]['weight'] += bottleneck
            flows[(u, v)] += bottleneck
            flows[(v, u)] -= bottleneck
        max_flow += bottleneck
    flows = {edge: val for edge, val in flows.items() if edge in graph.edges()}
    min_cut_edges, source_nodes, sink_nodes = find_min_cut(graph, source, residual)
    return max_flow, flows, min_cut_edges, source_nodes, sink_nodes