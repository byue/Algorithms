# Johnson's Algorithm for All-Pairs Shortest Paths

## Overview
**Johnson's Algorithm** is an algorithm used to compute **all-pairs shortest paths (APSP)** in a weighted directed graph. It is particularly useful when the graph contains **negative-weight edges** but **no negative-weight cycles**. In order to leverage Djikstra's algorithm, negative weights are transformed to positive weights, without distorting shortest paths.

## Purpose
- Find shortest paths between **all pairs** of vertices in a weighted graph.
- Handle **negative-weight edges** while preserving shortest paths.
- Improve efficiency over the naïve approach of running **Bellman-Ford** for each vertex.

## Theory

The key idea behind **Johnson’s Algorithm** is **reweighting**:
1. **Add a new vertex** `s` to the graph, connecting it to all other vertices with **zero-weight edges**.
2. **Run Bellman-Ford** from `s` to detect **negative-weight cycles**:
   - If a negative-weight cycle exists, **abort** (shortest paths are undefined).
   - Otherwise, compute shortest distances **h(v)** from `s` to all vertices `v`.
3. **Reweight the graph** using a **potential function** `h(v)`, ensuring all edges are **non-negative**:
   - Define new weights:  
     \[
     w'(u, v) = w(u, v) + h(u) - h(v)
     \]
   - This transformation **preserves shortest paths** but makes all weights **non-negative**.
4. **Run Dijkstra’s Algorithm** from each vertex:
   - Since weights are now **non-negative**, Dijkstra’s algorithm runs efficiently in **O(V log V + E)** time per source.
5. **Convert back to original weights**:
   - After computing shortest paths in the transformed graph, adjust the final distances using:
     \[
     \delta(u, v) = \delta'(u, v) - h(u) + h(v)
     \]

## Applications
- **Network Routing** (e.g., shortest paths in communication networks).
- **Transportation Systems** (e.g., computing shortest travel routes).
- **Supply Chain Optimization** (e.g., finding the best logistics paths).
- **Circuit Layout Design** (e.g., optimizing wiring connections).

## Runtime Complexity
The total runtime of Johnson’s Algorithm is:
\[
O(VE) + O(V(V \log V + E)) = O(V^2 \log V + VE)
\]
Breaking this down:
- **O(VE)** for **Bellman-Ford** (detects negative cycles and computes reweighting function).
- **O(V(V log V + E))** for **|V| runs of Dijkstra** (computes shortest paths after reweighting).

### Comparison to Other APSP Algorithms
| Algorithm   | Handles Negative Weights | Detects Negative Cycles | Runtime Complexity |
|------------|-------------------------|-------------------------|--------------------|
| Floyd-Warshall | ❌ No | ❌ No | **O(V³)** |
| Bellman-Ford (|V| times) | ✅ Yes | ✅ Yes | **O(V²E)** |
| Dijkstra (|V| times) | ❌ No | ❌ No | **O(V² log V + VE)** |
| **Johnson’s Algorithm** | ✅ Yes | ✅ Yes | **O(V² log V + VE)** |

## Conclusion
**Johnson’s Algorithm** is a powerful method for computing shortest paths in graphs with **negative weights**. It combines **Bellman-Ford** for cycle detection and reweighting, then leverages **Dijkstra** for efficient path computation. While it has the same worst-case complexity as Bellman-Ford for dense graphs, it is significantly faster on **sparse graphs** where Dijkstra’s **O(V log V + E)** performance dominates.
