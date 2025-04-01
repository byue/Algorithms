# Floyd-Warshall Algorithm for All-Pairs Shortest Paths

## Overview

The **Floyd-Warshall algorithm** is an algorithm for finding the **shortest paths** in a **weighted graph** with **positive or negative edge weights** (but no negative weight cycles). It solves the **All-Pairs Shortest Path (APSP)** problem, which involves computing the shortest paths between every pair of nodes in a graph.

### Purpose
The algorithm is used to compute the shortest paths between all pairs of nodes in a graph. It works efficiently for dense graphs or when all-pairs shortest path information is required for subsequent computations.

### Theory

Floyd-Warshall is a **dynamic programming** algorithm that iteratively improves the shortest path estimates between all pairs of vertices in a graph. The core idea is to use an intermediate node `k` to try and improve the shortest path between any two nodes `i` and `j`. If a path from `i` to `j` can be improved by passing through `k`, then the algorithm updates the shortest path between `i` and `j`.

The algorithm proceeds by considering each node in the graph as an intermediate node and checking if any shortest path can be improved by traversing that node.

### Recurrence Relation

The recurrence used in the Floyd-Warshall algorithm is:

`dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`

This means that for each pair of nodes `i` and `j`, the shortest path between `i` and `j` is the minimum of its current distance (`dist[i][j]`) and the sum of the shortest path from `i` to `k` and from `k` to `j`.

### Base Case

- For each node `i`, the shortest distance from `i` to itself is `0`:  
  `dist[i][i] = 0` for all `i`.
- The initial distances between directly connected nodes are initialized as the edge weights between them, and the distance for other pairs is set to infinity (`∞`).

### Algorithm Steps

1. **Initialization**:  
   - Set `dist[i][j] = ∞` for all pairs `(i, j)` unless there is an edge between them, in which case set `dist[i][j]` to the weight of the edge.
   - Set `dist[i][i] = 0` for all nodes `i` (distance from a node to itself is always 0).

2. **Iterate through all possible intermediate nodes `k`**:  
   For each node `k` in the graph, update the distance `dist[i][j]` for all pairs `(i, j)` by checking if passing through node `k` gives a shorter path.

3. **Repeat**:  
   Repeat the above step for every node `k` in the graph.

4. **Termination**:  
   After all intermediate nodes have been considered, the matrix `dist` will contain the shortest distances between all pairs of nodes.

### What do `i`, `j`, and `k` represent?

- `i`: The starting node for a path.
- `j`: The destination node for a path.
- `k`: The intermediate node that is considered in the path from `i` to `j`.

The algorithm iterates through all nodes and tries to find a shorter path from node `i` to node `j` by potentially using `k` as an intermediate node.

## Runtime Complexity

The time complexity of the Floyd-Warshall algorithm is:

- **Time complexity**: `O(V^3)`  
  Where `V` is the number of vertices in the graph.  
  The algorithm involves three nested loops over all nodes, leading to a cubic runtime.

- **Space complexity**: `O(V^2)`  
  The algorithm uses a `V x V` matrix to store the shortest path distances between every pair of vertices.

## Applications

- **Graph analysis**: Floyd-Warshall is useful for analyzing dense graphs where all-pairs shortest path information is needed.
- **Network routing**: It can be used to find the shortest routes between all pairs of routers in a network.
- **Transitive closure**: In some cases, Floyd-Warshall can be used to compute the transitive closure of a directed graph, i.e., finding whether there is a path between every pair of nodes.
- **Flight and transport scheduling**: Floyd-Warshall is suitable for applications such as transportation and circuit layout where you need to find the shortest route or time between any two locations in the system.

## Conclusion

Floyd-Warshall is a fundamental algorithm for solving the All-Pairs Shortest Path problem in graphs, especially when negative edge weights are involved. Its cubic time complexity makes it suitable for graphs with fewer vertices or when the graph is dense, but it is generally outperformed by other algorithms like Dijkstra or Johnson’s algorithm for sparse graphs.

