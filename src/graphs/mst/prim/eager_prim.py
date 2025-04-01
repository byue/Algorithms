import networkx as nx

# https://pypi.org/project/fibonacci-heap-mod/
# https://stromberg.dnsalias.org/svn/fibonacci-heap-mod/trunk/fibonacci_heap_mod.py
from fibonacci_heap_mod import Fibonacci_heap

# Runtime: O(E + VLog(V)) with Fibonacci Heap
# V insert's each taking O(1) with Fibonacci Heap, O(V)
# V dequeue-min's each taking O(Log(V)), O(VLog(V))
# E decrease-key's each taking O(1) with Fibonacci Heap, O(E)
# For binary heap, V insert's each take O(Log(V)), O(VLog(V))
# For binary heap, E decrease-key's each take O(Log(V)), O(ELog(V))
# For binary heap, V dequeue-min's each take O(Log(V)), O(VLog(V))
# Binary heap overall runtime is O((E + V) Log(V))
# Space: O(V), visited is per node, MST has V - 1 edges
def get_mst(graph):
    starting_node = next(iter(graph))
    visited = set([starting_node])

    # this is needed for getting Entry for decrease key operation, quirk of fibonacci heap mod lib.
    dest_node_to_entry = {}

    # since edges are updated throughout while loop for destination node
    # mst and total cost is not evaluated until after loop
    dest_node_to_edge = {}

    # initialize heap with nodes adjacent to MST (starts with starting node)
    # heap contains destination nodes
    pq = Fibonacci_heap()
    for next_node in graph.neighbors(starting_node):
        weight = graph[starting_node][next_node]['weight']
        dest_node_to_entry[next_node] = pq.enqueue(next_node, weight)
        dest_node_to_edge[next_node] = (starting_node, next_node, weight)

    # invariant: pq only has up to 1 entry per destination node
    while pq:
        current_node = pq.dequeue_min().get_value()
        visited.add(current_node)

        # visited check for dequeued current node not necessary since we ensure priority queue
        # does not have multiple entries for same destination node

        for next_node in graph.neighbors(current_node):
            weight = graph[current_node][next_node]['weight']

            # don't add destination nodes already visited to priority queue            
            if next_node in visited:
                continue

            # new edge to same destination node has higher cost, not included in MST
            if next_node in dest_node_to_edge and weight >= dest_node_to_edge[next_node][2]:
                continue

            # found an edge with lower cost to same destination node, replace in priority queue
            if next_node in dest_node_to_edge and weight < dest_node_to_edge[next_node][2]:
                pq.decrease_key(dest_node_to_entry[next_node], weight)
                dest_node_to_edge[next_node] = (current_node, next_node, weight)

            # destination node does not exist, add to priority queue
            if next_node not in dest_node_to_edge:
                dest_node_to_entry[next_node] = pq.enqueue(next_node, weight)
                dest_node_to_edge[next_node] = (current_node, next_node, weight)

    total_cost = 0
    mst = nx.Graph()

    # compute MST and total cost
    for u, v, weight in dest_node_to_edge.values():
        total_cost += weight
        mst.add_edge(u, v, weight=weight)

    return total_cost, mst