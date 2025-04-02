# Depth-First Search (DFS)

## Overview
Depth-First Search (DFS) is a fundamental algorithm for traversing or searching through graphs and trees. It explores as far as possible along each branch before backtracking, making it particularly useful for problems that require exhaustive exploration.

## Purpose
DFS is designed to systematically explore all vertices and edges of a graph. It helps in solving various graph-related problems, such as detecting cycles, finding paths, and analyzing connectivity.

## Theory
DFS follows a simple principle: **explore deeply before backtracking**. The algorithm starts at a given source node, marks it as visited, and explores one of its unvisited neighbors. This process repeats recursively (or using a stack in an iterative implementation) until there are no more unvisited neighbors, at which point the algorithm backtracks.

The traversal order depends on the order in which neighbors are visited. DFS can be implemented using:
- **Recursive approach** (implicit stack through function calls)
- **Iterative approach** (explicit stack for managing traversal)

## Runtime Complexity
DFS has a time complexity of **O(V + E)**, where:
- **V** is the number of vertices.
- **E** is the number of edges.

The space complexity is **O(V)** in the worst case due to recursion depth or explicit stack usage.

## Applications
DFS is widely used in various computational problems, including:
- **Graph traversal**: Exploring all nodes in a graph.
- **Cycle detection**: Identifying cycles in directed and undirected graphs.
- **Topological sorting**: Ordering nodes in a directed acyclic graph (DAG).
- **Connected components**: Finding clusters of connected nodes in a graph.
- **Pathfinding**: Discovering paths in mazes or networked structures.
- **Solving puzzles and games**: Used in backtracking algorithms like Sudoku solvers.

## DFS vs. BFS
| Feature      | DFS | BFS |
|-------------|----|----|
| Search Order | Depth-first (explores deeply first) | Breadth-first (explores level by level) |
| Data Structure | Stack (explicit or recursion) | Queue |
| Space Complexity | **O(V)** (recursive stack) | **O(V)** (queue storage) |
| Use Cases | Cycle detection, pathfinding, connected components | Shortest path (unweighted graphs), level-order traversal |

## Conclusion
DFS is a powerful and versatile algorithm that plays a crucial role in graph theory and problem-solving. Its deep exploration strategy makes it suitable for problems that require thorough search and analysis, especially when combined with techniques like backtracking and memoization.
