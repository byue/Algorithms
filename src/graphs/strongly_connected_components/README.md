# Kosaraju's Algorithm

## Overview
Kosaraju's Algorithm is a graph traversal technique used to find **Strongly Connected Components (SCCs)** in a **directed graph**. A strongly connected component is a maximal subset of vertices such that every vertex in the subset can reach every other vertex in the subset.

This algorithm utilizes **Depth-First Search (DFS)** twice to efficiently identify SCCs.

## Purpose
- Identify **Strongly Connected Components** in a directed graph.
- Detect **cycles** in directed graphs.
- Find **components that can be collapsed** into a single node in **DAG compression**.

## Theory
Kosaraju's Algorithm works based on **two DFS passes**:
1. **First DFS Pass (Forward Pass)**
   - Run a **DFS on the original graph** to compute a **topological ordering** (ordering based on finishing times).
   - The **nodes are pushed onto a stack in order of their finish times**.
  
2. **Transpose the Graph**
   - Reverse the direction of all edges (construct the **transpose graph**).

3. **Second DFS Pass (Backward Pass)**
   - Pop nodes from the stack and run **DFS on the transposed graph** in the order given by the stack.
   - Each DFS run identifies a **new SCC**.

## What It's Used For
- **Analyzing Webpages & Hyperlinks**: Identifying clusters of interlinked web pages.
- **Optimizing Compiler Dependency Analysis**: Finding cycles in dependencies.
- **Social Network Analysis**: Identifying groups of users strongly connected by relationships.
- **Graph Compression**: Reducing a graph to its SCC components to form a Directed Acyclic Graph (DAG).

## Time Complexity
- **O(V + E)** (Linear time)
- Requires **two full DFS traversals**, making it very efficient for large graphs.

## Comparison to Tarjan’s Algorithm
| Feature             | Kosaraju’s Algorithm            | Tarjan’s Algorithm              |
|---------------------|--------------------------------|---------------------------------|
| **Approach**       | Two DFS traversals & graph reversal | Single DFS traversal |
| **Extra Space**    | Requires **explicit stack** & transposed graph | Uses **implicit recursion stack** |
| **Efficiency**     | **O(V + E)**, but needs two passes | **O(V + E)**, only one DFS pass |
| **Implementation** | Easier to understand and implement | Slightly more complex due to low-link values |
| **Usage**         | Best when graph transposition is cheap or memory is available | Best for **online** SCC detection |

## When to Use Kosaraju vs. Tarjan
- **Use Kosaraju** if:
  - You can afford an explicit stack and **don’t mind storing the transposed graph**.
  - You prefer a conceptually simpler **two-pass algorithm**.

- **Use Tarjan** if:
  - You need a **single-pass DFS approach** with less memory usage.
  - You want to compute SCCs **as part of an ongoing DFS traversal**.

## Applications
- **Detecting cycles** in dependency graphs (e.g., circular dependencies in software modules).
- **Network clustering** (e.g., breaking large networks into connected subnetworks).
- **Solving 2-SAT problems** in boolean satisfiability problems.

Kosaraju's Algorithm remains a powerful and **easy-to-implement** method for **Strongly Connected Components** detection, making it an essential tool in graph theory.
