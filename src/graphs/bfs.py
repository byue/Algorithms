from collections import deque

def bfs(node, graph):
    parents = {node: None}
    queue = deque([node])
    while queue:
        node = queue.popleft()
        for child in graph.neighbors(node):
            if child not in parents:
                parents[child] = node
                queue.append(child)
    return parents

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
