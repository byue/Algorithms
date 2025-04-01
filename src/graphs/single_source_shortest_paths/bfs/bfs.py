from collections import deque

def get_sssp(node, graph):
    parents = {node: None}
    distances = {node: 0}
    queue = deque([node])
    while queue:
        node = queue.popleft()
        for child in graph.neighbors(node):
            if child not in parents:
                parents[child] = node
                distances[child] = distances[node] + 1
                queue.append(child)
    return distances, parents

def level_bfs(node, graph):
    parents = {node: None}
    queue = deque([node])
    levels = []
    while queue:
        levels.append(list(queue))
        for _ in range(len(queue)):
            node = queue.popleft()
            for child in graph.neighbors(node):
                if child not in parents:
                    parents[child] = node
                    queue.append(child)
    return levels, parents
