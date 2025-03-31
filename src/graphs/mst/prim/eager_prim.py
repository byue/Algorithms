import networkx as nx

# https://pypi.org/project/fibonacci-heap-mod/
# https://stromberg.dnsalias.org/svn/fibonacci-heap-mod/trunk/fibonacci_heap_mod.py
from fibonacci_heap_mod import Fibonacci_heap

# Runtime: O(E + VLog(V)) with Fibonacci Heap/decrease key
# Space: O(V)
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
    for u, v, data in graph.edges(starting_node, data=True):
        next_node = v if u == starting_node else u
        dest_node_to_entry[next_node] = pq.enqueue(next_node, data['weight'])
        dest_node_to_edge[next_node] = (starting_node, next_node, data['weight'])

    # invariant: pq only has up to 1 entry per destination node
    while pq:
        current_node = pq.dequeue_min().get_value()
        visited.add(current_node)

        # visited check for dequeued current node not necessary since we ensure priority queue
        # does not have multiple entries for same destination node

        for u, v, data in graph.edges(current_node, data=True):
            next_node = v if u == current_node else u

            # don't add destination nodes already visited to priority queue            
            if next_node in visited:
                continue

            # new edge to same destination node has higher cost, not included in MST
            if next_node in dest_node_to_edge and data['weight'] >= dest_node_to_edge[next_node][2]:
                continue

            # found an edge with lower cost to same destination node, replace in priority queue
            if next_node in dest_node_to_edge and data['weight'] < dest_node_to_edge[next_node][2]:
                pq.decrease_key(dest_node_to_entry[next_node], data['weight'])
                dest_node_to_edge[next_node] = (current_node, next_node, data['weight'])

            # destination node does not exist, add to priority queue
            if next_node not in dest_node_to_edge:
                dest_node_to_entry[next_node] = pq.enqueue(next_node, data['weight'])
                dest_node_to_edge[next_node] = (current_node, next_node, data['weight'])

    total_cost = 0
    mst = nx.Graph()

    # compute MST and total cost
    for u, v, weight in dest_node_to_edge.values():
        total_cost += weight
        mst.add_edge(u, v, weight=weight)

    return total_cost, mst