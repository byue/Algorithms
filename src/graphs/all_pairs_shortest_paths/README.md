# All-Pairs Shortest Path (APSP)

## Overview

The **All-Pairs Shortest Path (APSP)** problem involves finding the shortest paths between every pair of nodes in a weighted graph. APSP is crucial in many applications such as network routing, transportation planning, and optimization problems where understanding the distances between all pairs of nodes is necessary.

This README will discuss various algorithms for solving the APSP problem, their uses, time complexities, and appropriate scenarios for applying each.

## Problem Definition

Given a graph \( G = (V, E) \) where \( V \) is the set of vertices (nodes) and \( E \) is the set of edges, the goal of the APSP problem is to find the shortest path between every pair of vertices \( u, v \in V \).

The output is a matrix or a dictionary of shortest path distances for every pair of nodes, or `infinity` if no path exists between the nodes.

### Example

For a graph with vertices \( A, B, C \), the expected output of the APSP algorithm would be a matrix or dictionary showing the shortest distance between each pair of vertices:

| From \ To | A   | B   | C   |
|-----------|-----|-----|-----|
| **A**     | 0   | 5   | 8   |
| **B**     | 5   | 0   | 3   |
| **C**     | 8   | 3   | 0   |

### Graph Types
APSP algorithms can handle directed and undirected graphs, as well as graphs with positive or negative edge weights. However, graphs containing negative-weight cycles present additional challenges.

## Algorithms for APSP

Several algorithms can be used to solve the APSP problem. The choice of algorithm depends on the specific properties of the graph and the constraints of the problem.

### 1. Floyd-Warshall Algorithm

#### Purpose:
Floyd-Warshall is a dynamic programming algorithm used to find the shortest paths between all pairs of nodes in a graph. It works for both directed and undirected graphs, even if the graph contains negative edge weights (but not negative-weight cycles).

#### Time Complexity:
- **Time complexity**: \( O(V^3) \), where \( V \) is the number of vertices.
- **Space complexity**: \( O(V^2) \) for storing the distance matrix.

#### Key Features:
- Efficient for dense graphs.
- Simple to implement.
- Handles negative edge weights, but cannot handle negative-weight cycles.
  
#### Applications:
- **Network routing**: Determining the shortest paths between all routers in a network.
- **Transportation systems**: Calculating shortest travel times between all points in a transportation network.
  
### 2. Johnson's Algorithm

#### Purpose:
Johnson's algorithm computes the APSP by first reweighting the graph to remove negative edge weights, then using **Dijkstra's algorithm** repeatedly for each vertex.

#### Time Complexity:
- **Time complexity**: \( O(V \cdot (V \log V + E)) \), where \( V \) is the number of vertices and \( E \) is the number of edges.
- **Space complexity**: \( O(V^2) \) for storing the distance matrix.

#### Key Features:
- Works for graphs with negative edge weights, but not negative-weight cycles.
- More efficient than Floyd-Warshall for sparse graphs.
  
#### Applications:
- **General-purpose APSP**: When the graph is sparse, Johnson’s algorithm is more efficient than Floyd-Warshall.
- **Computing shortest paths in weighted graphs with negative edge weights**.

### 3. Dijkstra’s Algorithm (Repeatedly for each node)

#### Purpose:
Dijkstra's algorithm finds the shortest path from a single source to all other nodes. By running Dijkstra’s algorithm \( V \) times, once for each node, it can solve the APSP problem.

#### Time Complexity:
- **Time complexity**: \( O(V \cdot (V \log V + E)) \), where \( V \) is the number of vertices and \( E \) is the number of edges.
- **Space complexity**: \( O(V^2) \) for storing the distance matrix.

#### Key Features:
- Works for graphs with non-negative weights.
- Efficient when using a priority queue (min-heap) for selecting the next node to process.
  
#### Applications:
- **Shortest path queries** in graphs where edge weights are non-negative.
  
### 4. Bellman-Ford Algorithm (Repeatedly for each node)

#### Purpose:
The Bellman-Ford algorithm computes the shortest paths from a single source vertex to all other vertices, and can also handle graphs with negative edge weights (but not negative-weight cycles).

#### Time Complexity:
- **Time complexity**: \( O(V \cdot E) \), where \( V \) is the number of vertices and \( E \) is the number of edges.
- **Space complexity**: \( O(V^2) \) for storing the distance matrix.

#### Key Features:
- Can handle negative edge weights.
- Works for sparse graphs.
- Can detect negative-weight cycles.

#### Applications:
- **Graphs with negative weights**: When the graph contains negative weights but no negative-weight cycles.
- **Cycle detection**: Bellman-Ford can detect negative-weight cycles, making it useful for detecting cycles in financial and network systems.

## Choosing the Right Algorithm

| Algorithm             | Time Complexity          | Best Use Case                                      |
|-----------------------|--------------------------|----------------------------------------------------|
| **Floyd-Warshall**     | \( O(V^3) \)             | Dense graphs, when the graph has negative weights  |
| **Johnson’s Algorithm**| \( O(V \cdot (V \log V + E)) \) | Sparse graphs with negative weights                 |
| **Dijkstra (Repeated)**| \( O(V \cdot (V \log V + E)) \) | Non-negative weights, sparse graphs                |
| **Bellman-Ford (Repeated)** | \( O(V \cdot E) \)      | Graphs with negative edge weights and no negative-weight cycles |

## Summary

The **All-Pairs Shortest Path (APSP)** problem is a critical problem in graph theory, and several algorithms exist for solving it. 

- **Floyd-Warshall** is best for dense graphs and works well for negative-weight edges (but not negative-weight cycles).
- **Johnson's Algorithm** is efficient for sparse graphs and can handle negative edge weights (but not negative-weight cycles).
- **Dijkstra's Algorithm** is useful for graphs with non-negative weights and is often faster for sparse graphs.
- **Bellman-Ford** is used for graphs with negative weights and can detect negative-weight cycles.

Choosing the right algorithm depends on the characteristics of your graph (e.g., density, edge weights) and the need for cycle detection.

## Conclusion

The APSP problem is fundamental in graph theory and has a wide range of applications, including network routing, transportation systems, and optimization tasks. By understanding the properties of different algorithms, one can choose the most efficient method to solve the problem for a given graph.

