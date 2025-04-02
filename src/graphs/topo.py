from collections import deque

def kahn_topo_sort(graph):
    in_degrees = {node: 0 for node in graph}
    seen = set()
    for root in graph:
        if root not in seen:
            seen.add(root)
            queue = deque([root])
            while queue:
                node = queue.popleft()
                for child in graph.neighbors(node):
                    in_degrees[child] += 1
                    if child not in seen:
                        seen.add(child)
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
        return []
    return result

def dfs_recursive_topo_sort(graph):
    def dfs_topo_recursive_helper(node, visited, visited_in_component, topological_ordering):
        visited.add(node)
        visited_in_component.add(node)
        for child in graph.neighbors(node):
            if child in visited_in_component or \
                    (child not in visited and not dfs_topo_recursive_helper(child, visited, visited_in_component, topological_ordering)):
                return False
        topological_ordering.append(node)
        visited_in_component.remove(node)
        return True
    topological_ordering = []
    visited = set()
    for node in graph:
        if node not in visited and not dfs_topo_recursive_helper(node, visited, set(), topological_ordering):
            return []            
    return topological_ordering[::-1]
