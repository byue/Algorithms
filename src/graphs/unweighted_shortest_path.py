def unweighted_shorted_path(parents, source, destination):
    if not parents[destination]:
        return None
    path = [destination]
    current_node = parents[destination]
    while current_node:
        path.append(current_node)
        if current_node == source:
            break
        current_node = parents[current_node]
    if current_node:
        return path[::-1]
    return None
