# Ford-Fulkerson Algorithm

## Overview

The **Ford-Fulkerson Algorithm** is a foundational method for solving the **Maximum Flow Problem** in a **flow network**. It computes the maximum amount of flow that can be sent from a designated source to a sink without violating the capacity constraints on the edges.

---

## Purpose

To find the **maximum flow** in a directed graph where each edge has a capacity and each flow must respect this capacity. It's a cornerstone in network flow theory and serves as a base for several optimized algorithms.

---

## Theory

The core idea of Ford-Fulkerson is **greedy augmentation**:
1. Start with an initial flow of 0.
2. As long as there exists an **augmenting path** (a path from source to sink with available capacity), augment the flow along this path.
3. Repeat until no more augmenting paths are found.

To handle backtracking, a **residual graph** is maintained, which reflects the remaining capacities and allows for the reversal of flow if needed.

The flow is **augmented** by the minimum residual capacity along the augmenting path, and the residual graph is updated accordingly.

---

## Runtime

- In general, runtime depends on how flows are chosen:
  - **O(E * max_flow)** in the worst case if capacities are integers.
  - May not terminate if capacities are irrational numbers (hence why **Edmonds-Karp**, a BFS-based variant with O(VE²), is commonly preferred in practice).

---

## Applications

Ford-Fulkerson and its variants are widely used in:
- **Network routing** and bandwidth allocation
- **Circulation problems**
- **Bipartite graph matching**
- **Project selection**
- **Image segmentation**
- **Job assignments**

---

## Application: Bipartite Matching

One elegant application of Ford-Fulkerson is in solving **maximum bipartite matching**.

### Problem Setup:
Given a bipartite graph with partitions U and V, and edges only between nodes in different partitions, find the **maximum number of matching pairs** such that no two edges share an endpoint.

### Transformation to Flow:
1. Add a **source** node connected to every node in U.
2. Add a **sink** node connected from every node in V.
3. Assign capacity 1 to all edges (original edges + those connecting to source and sink).
4. Run Ford-Fulkerson to compute the max flow.

Each unit of flow from source to sink corresponds to a unique match. Hence, the size of the maximum matching is equal to the value of the maximum flow.

---

## Summary

Ford-Fulkerson is an intuitive and powerful algorithm for network flow problems. Its flexibility allows it to serve as a tool for solving various real-world and theoretical problems, from network design to graph matching.
