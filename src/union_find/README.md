# UnionFind (Disjoint Set Union) by Rank

## Overview

The **UnionFind** data structure, also known as **Disjoint Set Union (DSU)**, is a powerful and efficient algorithm used to manage a collection of disjoint sets. It supports two primary operations:
- **Union**: Merge two sets into one.
- **Find**: Determine which set an element belongs to.

This implementation uses **union by rank** and **path compression** optimizations to improve performance and make the operations nearly constant time, even for large sets.

## Purpose

UnionFind is commonly used in scenarios where we need to:
- Track the connected components of a graph.
- Determine if two elements belong to the same set.
- Efficiently merge two sets into one.

## Optimizations

### Path Compression
When performing the **Find** operation, path compression flattens the structure of the tree. This ensures that future calls to **Find** are faster by making the tree more shallow.

### Union by Rank
When performing the **Union** operation, union by rank ensures that the smaller tree is always attached to the root of the larger tree. This keeps the overall tree balanced, reducing its height and improving the efficiency of subsequent operations.

Together, these optimizations make the **UnionFind** operations nearly constant time (O(α(n)), where α is the inverse Ackermann function, which grows extremely slowly).

## Methods

### `find(x)`
- **Description**: Determines the root of the set containing element `x`. Uses path compression to flatten the structure of the tree, speeding up future operations.
- **Time Complexity**: O(α(n))

### `union(x, y)`
- **Description**: Merges the sets containing elements `x` and `y`. The tree with the smaller rank is attached under the tree with the larger rank.
- **Time Complexity**: O(α(n))

### `connected(x, y)`
- **Description**: Checks if elements `x` and `y` belong to the same set.
- **Time Complexity**: O(α(n))

## Applications

UnionFind is a versatile data structure and is used in many algorithms, including:

### 1. **Cycle Detection in Graphs**
UnionFind is frequently used in graph algorithms to detect cycles. For example, when checking if adding an edge between two nodes forms a cycle, we check if the two nodes are already connected. If they are, adding the edge would create a cycle.

### 2. **Kruskal's Minimum Spanning Tree Algorithm**
UnionFind is integral to Kruskal's algorithm for finding the minimum spanning tree (MST) of a graph. By using UnionFind to efficiently check and merge components, we can determine the MST in O(E log E) time, where E is the number of edges.

### 3. **Connected Components in a Graph**
UnionFind can be used to determine the connected components of a graph. If two nodes are connected, they belong to the same component, and the **Find** operation can help group them together.

### 4. **Dynamic Connectivity**
UnionFind can solve dynamic connectivity problems, where the structure of the graph is constantly changing with nodes being connected or disconnected over time.

## Example Usage

```python
# Initialize the UnionFind data structure
uf = UnionFind()

# Union of two sets
uf.union(1, 2)
uf.union(2, 3)

# Check if two elements are in the same set
print(uf.connected(1, 3))  # True

# Find the root of an element
print(uf.find(1))  # 1 (or the representative of the set)