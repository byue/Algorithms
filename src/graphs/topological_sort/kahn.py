from collections import deque

def topo_sort(graph, validate_cycles=True):
    # calculate in-degrees
    in_degrees = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph.neighbors(node): 
            in_degrees[neighbor] += 1

    # queue initialized with nodes with 0 in-degree (no prereqs)
    queue = deque([node for node, in_degree in in_degrees.items() if in_degree == 0])
    result = []

    # add to result in topological order
    while queue:
        node = queue.popleft()
        result.append(node)
        for child in graph.neighbors(node):
            # simulate trimming node - child connection, child decreases in-degrees
            in_degrees[child] -= 1
            # no more prereqs after trimming parents, add child to queue
            if in_degrees[child] == 0:
                queue.append(child)

    # cycle is detected if the number of nodes processed is less than the total number of nodes in the graph
    # A cycle prevents all nodes from having in-degree 0 at some point.
    # Nodes involved in a cycle will never reach the queue, so they won't be added to the topological_order.
    if len(result) != len(in_degrees) and validate_cycles:
        return []

    return result