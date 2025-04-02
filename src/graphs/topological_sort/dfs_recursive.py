from collections import deque

def topo_sort(graph, validate_cycles=True):
    color = {node: "WHITE" for node in graph}
    topological_ordering = deque()

    def dfs(node):
        color[node] = "GREY"
        for child in graph.neighbors(node):
            # cycle detected, back-edge if node is GREY
            if color[child] == "GREY" and validate_cycles:
                return False
            if color[child] == "WHITE" and not dfs(child):
                return False
        color[node] = "BLACK"
        topological_ordering.appendleft(node)
        return True

    for node in graph:
        if color[node] == "WHITE" and not dfs(node):
            return deque()

    return topological_ordering
