from collections import deque

def kahn_topo_sort(nodes):
    in_degrees = {node: 0 for node in nodes}
    seen = set()
    for root in nodes:
        queue = deque([root])
        while queue:
            node = queue.popleft()
            seen.add(node)
            for child in node.children:
                if child not in seen:
                    in_degrees[child] = 0
                    queue.append(child)
                in_degrees[child] += 1
    queue = deque([node for node, in_degree in in_degrees.items() if in_degree == 0])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for child in node.children:
            in_degrees[child] -= 1
            if in_degrees[child] == 0:
                queue.append(child)
    if len(result) != len(in_degrees):
        return None
    return result
