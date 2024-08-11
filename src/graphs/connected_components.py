from collections import deque

def connected_components(graph):
    visited = set()
    connected_components = []
    for root_node in graph:
        if root_node not in visited:
            connected_component = []
            queue = deque([root_node])
            while queue:
                node = queue.popleft()
                visited.add(node)
                connected_component.append(node)
                for child in graph.neighbors(node):
                    if child not in visited:
                        queue.append(child)
            connected_components.append(connected_component)
    return connected_components
