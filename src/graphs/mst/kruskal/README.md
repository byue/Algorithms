# Kruskal's Algorithm for Minimum Spanning Tree (MST)

## Purpose
Kruskal's Algorithm is a greedy algorithm used to find the **Minimum Spanning Tree (MST)** of a connected, undirected graph. An MST is a subset of the edges in a graph that connects all the vertices without any cycles and with the minimum possible total edge weight.

### Key Features of MST:
- **Connectivity**: All nodes are connected.
- **No Cycles**: No cycles are present in the MST.
- **Minimum Weight**: The sum of the weights of the edges is as small as possible.

## Theory
Kruskal's Algorithm follows these main steps:

1. **Sort the edges** in the graph by increasing edge weight.
2. **Pick the smallest edge**. If it connects two nodes that are not yet connected, add it to the MST.
3. Repeat step 2 until there are exactly \(V - 1\) edges in the MST (where \(V\) is the number of vertices in the graph).
4. **Avoid cycles** by using a **Union-Find** data structure to check whether two vertices are already connected.

The key data structures used are:
- **Union-Find (Disjoint Set Union - DSU)**: To keep track of connected components and efficiently check for cycles when adding an edge.
- **Priority Queue** or **Sorted Edge List**: To pick the smallest edges first.

### Steps:
1. Sort all edges by weight.
2. Initialize a Union-Find data structure to manage the connected components.
3. Add edges to the MST, skipping those that would form a cycle.
4. Stop when the MST contains \(V - 1\) edges.

## Runtime Complexity
The time complexity of Kruskal's Algorithm is \(O(E \log E)\), where \(E\) is the number of edges in the graph. The sorting of edges dominates the time complexity. 

- Sorting the edges takes \(O(E \log E)\).
- Union-Find operations (find and union) take almost constant time \(O(\alpha(V))\), where \(\alpha\) is the inverse Ackermann function, which grows extremely slowly.

Thus, the overall time complexity is \(O(E \log E)\), making Kruskal's algorithm efficient for sparse graphs.

## Applications
Kruskal's algorithm is particularly useful for:

- **Network Design**: Building the least-cost network connecting multiple nodes, such as laying out electrical grids, designing computer networks, or connecting cities with roads or railways.
- **Clustering**: In machine learning, MST can be used for hierarchical clustering algorithms.
- **Data Compression**: Algorithms like **Huffman coding** for data compression can be seen as a variant of MST.

## Comparison with Prim's Algorithm

Both **Kruskal's Algorithm** and **Prim's Algorithm** are used to find the Minimum Spanning Tree (MST), but they have different approaches:

### When to Use Kruskal's Algorithm:
- **Sparse Graphs**: Kruskal's is efficient when the graph is sparse, as it only needs to sort the edges.
- **Edge-Centric**: If the problem requires focusing on edge selection, Kruskal's algorithm is often preferred.
- **Disjoint Components**: Kruskal’s works well when the graph might not be fully connected initially, since it works by adding edges across components.

### When to Use Prim's Algorithm:
- **Dense Graphs**: Prim's algorithm is better suited for dense graphs because it grows the MST one node at a time, without needing to sort all edges.
- **Node-Centric**: If the problem involves selecting edges based on nodes rather than the entire edge set, Prim’s algorithm can be more natural.
- **Connected Graphs**: If the graph is already connected and you start with any node, Prim’s algorithm works efficiently.

### Key Differences:
| **Factor**         | **Kruskal's Algorithm**          | **Prim's Algorithm**         |
|--------------------|----------------------------------|-----------------------------|
| **Approach**       | Edge-centric (works with edges) | Node-centric (grows tree from a node) |
| **Graph Density**  | Better for sparse graphs         | Better for dense graphs     |
| **Data Structure** | Sort edges, Union-Find for cycles| Priority Queue, adjacency list |
| **Complexity**     | \(O(E \log E)\)                  | \(O(E + V \log V)\)         |
| **Best Use Case**  | Graphs with many edges, sparse  | Graphs with many nodes and edges |

In conclusion, **Kruskal's Algorithm** is a powerful choice for finding the MST in sparse graphs with fewer edges, whereas **Prim's Algorithm** may be more effective when the graph is dense, and node-based traversal is preferred. The choice of algorithm depends largely on the structure and properties of the graph being analyzed.
