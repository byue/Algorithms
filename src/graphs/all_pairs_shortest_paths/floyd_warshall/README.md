# Floyd-Warshall Algorithm

## Overview
The **Floyd-Warshall algorithm** is a dynamic programming technique used to compute the shortest paths between all pairs of vertices in a weighted graph. Unlike algorithms that find shortest paths from a single source, Floyd-Warshall efficiently determines the shortest distances between every pair of nodes, making it a powerful solution for **all-pairs shortest path (APSP) problems**.

## Theory
Floyd-Warshall relies on the principle of **incremental improvement** by considering whether an intermediate vertex provides a shorter path between two other vertices. It systematically updates a distance matrix, checking whether paths that pass through an intermediate vertex yield a shorter total distance.

The core recurrence relation for updating distances is:

\[
d(i, j) = \min(d(i, j), d(i, k) + d(k, j))
\]

Where:
- \( d(i, j) \) is the shortest distance from vertex \( i \) to vertex \( j \).
- \( k \) is an intermediate vertex that we check to see if it provides a shorter path.

The algorithm iterates over all possible intermediate vertices and updates the shortest known paths accordingly.

## Use Cases
The Floyd-Warshall algorithm is particularly useful in:
- **Network routing**: Finding the shortest paths between all routers in a network.
- **Urban traffic analysis**: Computing shortest routes between all intersections in a city.
- **Flight route optimization**: Finding shortest travel times between all airports.
- **Transitive closure computation**: Determining reachability in graphs.

## Algorithm Runtime
The time complexity of Floyd-Warshall is **O(V³)**, where \( V \) is the number of vertices. The algorithm operates on a **distance matrix** and iterates over all pairs of vertices for each intermediate vertex.

- **Time Complexity:** \( O(V^3) \)
- **Space Complexity:** \( O(V^2) \) (stores shortest path distances and parent relationships)

## Comparison to Other APSP Algorithms
| Algorithm        | Time Complexity  | Best for...                          |
|-----------------|-----------------|--------------------------------------|
| **Floyd-Warshall** | \( O(V^3) \) | Dense graphs, simple implementation |
| **Dijkstra (V times)** | \( O(V^2 + VE) \) with simple PQ, \( O(V \log V + E) \) with Fibonacci heap | Sparse graphs, non-negative weights |
| **Johnson’s Algorithm** | \( O(V^2 \log V + VE) \) | Large graphs with some negative weights |
| **Bellman-Ford (V times)** | \( O(V^2E) \) | Detecting negative weight cycles |

### When to Use Floyd-Warshall?
- **Use Floyd-Warshall when** the graph is **dense** (i.e., many edges) or when you need a **simpler implementation**.
- **Avoid Floyd-Warshall for very large graphs**, as its **O(V³) complexity** makes it slower than alternatives like Johnson’s Algorithm for sparse graphs.

## Limitations
- Floyd-Warshall does **not work with negative-weight cycles**; it can detect them but not compute shortest paths in such cases.
- It is inefficient for graphs with large vertex counts due to its **cubic time complexity**.

## Summary
Floyd-Warshall is an elegant, matrix-based approach for computing **all-pairs shortest paths** in a graph. It is particularly valuable for problems where **graph size is moderate**, and a **simple, uniform approach** is preferred over more complex algorithms.

---
