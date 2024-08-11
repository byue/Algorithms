from collections import deque

def kahn_topo_sort(graph):
    in_degrees = {node: 0 for node in graph}
    seen = set()
    for root in graph:
        if root not in seen:
            queue = deque([root])
            while queue:
                node = queue.popleft()
                seen.add(node)
                for child in graph.neighbors(node):
                    in_degrees[child] += 1
                    if child not in seen:
                        queue.append(child)
    queue = deque([node for node, in_degree in in_degrees.items() if in_degree == 0])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for child in graph.neighbors(node):
            in_degrees[child] -= 1
            if in_degrees[child] == 0:
                queue.append(child)
    if len(result) != len(in_degrees):
        return None
    return result
