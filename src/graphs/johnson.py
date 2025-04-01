from src.graphs.bellman_ford import get_weighted_shortest_paths as bellman_ford
import src.graphs.single_source_shortest_paths.djikstra.djikstra as djikstra

def get_all_pairs_shortest_paths(graph):
    virtual_graph = graph.copy()
    for node in graph:
        virtual_graph.add_edge('Virtual', node, weight=0)
    distances, _ = bellman_ford('Virtual', virtual_graph)
    if not distances:
        return None
    transformed_graph = graph.copy()
    for parent, child, data in transformed_graph.edges(data=True):
        data['weight'] += distances[parent]
        data['weight'] -= distances[child]
    djikstra_result = {node: djikstra.get_sssp(node, transformed_graph) for node in transformed_graph}
    for source in djikstra_result:
        for destination in djikstra_result[source][0]:
            djikstra_result[source][0][destination] -= distances[source]
            djikstra_result[source][0][destination] += distances[destination]
    return djikstra_result
