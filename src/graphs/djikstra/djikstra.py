from fibonacci_heap_mod import Fibonacci_heap

# Runtime: O(E + VLog(V))
# V insert's each taking O(Log(V))
# V dequeue-min's each taking O(Log(V))
# E decrease-key's each taking O(1) with Fibonacci Heap
# Space: O(V), pq only has 1 entry per node, parent and shortest path dictionaries are only 1 entry per node
def get_weighted_shortest_paths(source, graph):
    shortest_path_distance = {current_node: 0 if current_node == source else float('inf') for current_node in graph}
    parent_node = {source: None}
    pq = Fibonacci_heap()
    dest_node_to_entry = {source: pq.enqueue(source, 0)}

    while pq:
        current_node = pq.dequeue_min().get_value()

        for next_node in graph.neighbors(current_node):
            # candidate distance to next_node is shortest path to current_node and distance of edge from current_node to next_node
            # instead of taking distance of single endge to next_node like in Prim's, we consider the distance of entire path to next_node.
            # Djikstra's optimizes for shortest path from some distant source, instead of minimizing sum of edge weights like in Prim's (pick locally smallest edge)
            candidate_distance = shortest_path_distance[current_node] + graph[current_node][next_node]['weight']

            # if candidate distance going through current_node to next_node does not exceed
            # current shortest path distance to next_node then skip processing
            if shortest_path_distance[next_node] <= candidate_distance:
                continue

            shortest_path_distance[next_node] = candidate_distance
            parent_node[next_node] = current_node

            # node already exists in pq, decrease key since distance decreased,
            # otherwise add new entry to pq
            if next_node in dest_node_to_entry:
                pq.decrease_key(dest_node_to_entry[next_node], candidate_distance)
            else:
                dest_node_to_entry[next_node] = pq.enqueue(next_node, candidate_distance)

    return shortest_path_distance, parent_node