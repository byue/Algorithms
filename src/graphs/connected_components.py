from collections import deque

def connected_components(nodes):
    visited = set()
    connected_components = []
    for node in nodes:
        if node not in visited:
            connected_component = []
            queue = deque([node])
            while queue:
                node = queue.popleft()
                connected_component.append(node)
                for child in node.children:
                    if child not in visited:
                        visited.add(child)
                        queue.append(child)
            connected_components.append(connected_component)
    return connected_components
