from collections import deque

def connected_components(graph):
    visited = set()
    connected_components = []
    for root_node in graph:
        if root_node not in visited:
            visited.add(root_node)
            connected_component = []
            queue = deque([root_node])
            while queue:
                node = queue.popleft()
                connected_component.append(node)
                for child in graph.neighbors(node):
                    if child not in visited:
                        visited.add(child)
                        queue.append(child)
            connected_components.append(connected_component)
    return connected_components
