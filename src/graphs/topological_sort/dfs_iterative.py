from collections import deque

def topo_sort(graph, validate_cycles=True):
    color = {node: "WHITE" for node in graph}
    topological_ordering = deque()

    for root in graph:
        if color[root] == "WHITE":
            stack = deque([root])
            while stack:
                node = stack[-1]

                if color[node] == "WHITE":
                    color[node] = "GREY"
                    for child in reversed(list(graph.neighbors(node))):
                        if color[child] == "GREY" and validate_cycles:
                            return deque()
                        if color[child] == "WHITE":
                            stack.append(child)
                else:
                    stack.pop()
                    if color[node] == "GREY":
                        topological_ordering.appendleft(node)
                        color[node] = "BLACK"

    return topological_ordering
