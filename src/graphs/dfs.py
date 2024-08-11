from collections import deque

def dfs_get_all_cycles_undirected(graph):
    def dfs(graph, path, seen_in_any_component, seen_in_component, node, cycles):
        seen_in_any_component.add(node)
        path.append(node)
        if node in seen_in_component:
            cycle = [node]
            for i in range(len(path) - 2, -1, -1):
                if path[i] == node:
                    break
                cycle.append(path[i])
            cycles[frozenset(cycle)] = cycle
            del path[-1]
            return
        seen_in_component.add(node)
        for child in graph.neighbors(node):
            dfs(graph, path, seen_in_any_component, seen_in_component, child, cycles)
        seen_in_component.remove(node)
        del path[-1]
    cycles = {}
    seen_in_any_component = set()
    for node in graph:
        if node not in seen_in_any_component:
            dfs(graph, [], seen_in_any_component, set(), node, cycles)
    return list(cycles.values())

def dfs_iterative(graph):
    node = next((n for n in graph), None)
    parents = {node: None}
    queue = deque([node])
    while queue:
        node = queue.pop()
        for child in graph.neighbors(node):
            if child not in parents:
                parents[child] = node
                queue.append(child)
    return parents

def dfs_recursive(graph):
    def dfs_recursive_helper(node, parents):
        for child in graph.neighbors(node):
            if child not in parents:
                parents[child] = node
                dfs_recursive_helper(child, parents)
    node = next((n for n in graph), None)
    parents = {node: None}
    dfs_recursive_helper(node, parents)
    return parents

def dfs_recursive_topo_sort(graph):
    def dfs_topo_recursive_helper(node, visited, topological_ordering):
        visited.add(node)
        for child in graph.neighbors(node):
            if child not in visited:
                dfs_topo_recursive_helper(child, visited, topological_ordering)
        topological_ordering.append(node)
    topological_ordering = []
    visited = set()
    node = next((n for n in graph), None)
    dfs_topo_recursive_helper(node, visited, topological_ordering)
    return topological_ordering[::-1]