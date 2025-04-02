def topo_sort(graph):
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
