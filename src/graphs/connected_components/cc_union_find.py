from src.union_find.union_find import UnionFind

def connected_components(graph):
    uf = UnionFind()
    for u, v in graph.edges():
        uf.union(u, v)
    components = {}
    for node in graph:
        root = uf.find(node)
        if root not in components:
            components[root] = []
        components[root].append(node)
    return list(components.values())