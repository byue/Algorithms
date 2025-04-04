from src.graphs.min_cut_max_flow.ford_fulkerson import ford_fulkerson
import networkx as nx

def bipartite_matching(U, V, bipartite_graph):
    G = nx.DiGraph()
    source = 'source'
    sink = 'sink'

    # Add source edges
    for u in U:
        G.add_edge(source, u, weight=1)

    # Add sink edges
    for v in V:
        G.add_edge(v, sink, weight=1)

    # Add bipartite edges
    for u, v in bipartite_graph.edges():
        if u in U and v in V:
            G.add_edge(u, v, weight=1)
        elif u in V and v in U:
            G.add_edge(v, u, weight=1)

    # Run max flow
    max_flow, flows, *_ = ford_fulkerson(G, source, sink)
    if max_flow != len(U):
        return None

    # Extract matches
    matches = {}
    for u in U:
        for v in bipartite_graph.neighbors(u):
            if flows.get((u, v), 0) == 1:
                matches[u] = v
                break
    return matches
