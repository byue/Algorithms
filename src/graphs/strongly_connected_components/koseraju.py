from src.graphs.topological_sort.dfs_iterative import topo_sort
from collections import deque

# Call DFS topo sort to get nodes in topological order (must be reverse postorder)
# Compute graph reversed (for in-line we just take predecessors instead of neighbors in BFS)
# Call DFS or BFS on reversed graph, loop over nodes in reverse topological order
def get_scc(graph):
    # either BFS or DFS could have been done here, but topo sort needs to be DFS
    def bfs_on_reverse_edges(graph, nodes):
        visited = set()
        connected_components = []
        for root_node in reversed(nodes): # reverse order of topo-sort (essentially postorder traversal of graph)
            if root_node not in visited:
                visited.add(root_node)
                connected_component = []
                queue = deque([root_node])
                while queue:
                    node = queue.popleft()
                    connected_component.append(node)
                    for child in graph.predecessors(node): # instead of reversing graph we get child from predecessors instead of successors
                        if child not in visited:
                            visited.add(child)
                            queue.append(child)
                connected_components.append(connected_component)
        return connected_components
    return bfs_on_reverse_edges(graph, topo_sort(graph, validate_cycles=False))

