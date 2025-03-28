from src.union_find.union_find import UnionFind
import networkx as nx

def get_mst(graph):
    nodes = graph.nodes()
    uf = UnionFind()
    total_cost = 0
    num_edges = 0
    mst = nx.Graph()
    for u, v, data in sorted(graph.edges(data=True), key=lambda x: x[2]['weight']):
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            total_cost += data['weight']
            num_edges += 1
            mst.add_edge(u, v, weight=data['weight'])
            if num_edges == len(nodes) - 1:
                break
    return total_cost, mst
