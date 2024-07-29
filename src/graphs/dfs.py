from collections import deque

def dfs_get_cycles(node):
    parents = {node: None}
    queue = deque([node])
    cycles = []
    while queue:
        node = queue.popleft()
        for child in node.children:
            if child not in parents:
                parents[child] = node
                queue.append(child)
            else:
                cycle = [child]
                current_node = node
                while current_node != child:
                    cycle.append(current_node)
                    current_node = parents[current_node]
                cycles.append(cycle)
    return cycles

def dfs_iterative(node):
    parents = {node: None}
    queue = deque([node])
    while queue:
        node = queue.pop()
        for child in node.children:
            if child not in parents:
                parents[child] = node
                queue.append(child)
    return parents

def dfs_recursive(node):
    def dfs_recursive_helper(node, parents):
        for child in node.children:
            if child not in parents:
                parents[child] = node
                dfs_recursive_helper(child, parents)
    parents = {node: None}
    dfs_recursive_helper(node, parents)
    return parents

def dfs_recursive_topo_sort(node):
    def dfs_topo_recursive_helper(node, visited, topological_ordering):
        visited.add(node)
        for child in node.children:
            if child not in visited:
                dfs_topo_recursive_helper(child, visited, topological_ordering)
        topological_ordering.append(node)
    topological_ordering = []
    visited = set()
    dfs_topo_recursive_helper(node, visited, topological_ordering)
    return topological_ordering[::-1]