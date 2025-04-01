# Bellman-Ford Algorithm

## Overview
The **Bellman-Ford algorithm** is a fundamental algorithm for finding the **shortest paths** from a single source vertex to all other vertices in a weighted graph. Unlike **Dijkstra's algorithm**, Bellman-Ford works with **negative-weight edges** and can detect **negative-weight cycles**.

## Purpose
- Find the **shortest paths** from a source node in a weighted graph.
- Handle graphs with **negative-weight edges**.
- Detect **negative-weight cycles**, which can cause shortest paths to become arbitrarily small.

## Theory
Bellman-Ford follows a **relaxation** process, iterating through all edges **|V| - 1** times (where |V| is the number of vertices). During each iteration, it updates the shortest known distances to each vertex. If, after **|V| - 1** iterations, a shorter path is still found, then a **negative-weight cycle** exists.

The key idea behind Bellman-Ford is **edge relaxation**: if a shorter path to a vertex is found through an edge, we update the shortest distance.

Why do we loop **|V| - 1 times**?  
- In the worst case, a shortest path in a graph with **V** vertices contains at most **V - 1 edges** (a simple path cannot have more than **V - 1** edges without forming a cycle).  
- Each iteration ensures that all shortest paths using at most **i** edges are correctly computed.  
- After **V - 1 iterations**, every possible shortest path **must** have been found, because any shorter path would have to involve a cycle.

If after **V - 1 iterations** we can still update a shortest path, that means there is a **negative-weight cycle** in the graph, since paths can be made infinitely smaller.

## Applications
- **Graph networks** (routing in networks with costs)
- **Currency arbitrage detection** (finding cycles in exchange rates)
- **Negative-weight cycle detection** (important for validating input graphs)

## Runtime Complexity
- **O(V × E)** (where |V| is the number of vertices and |E| is the number of edges)
- Works well for **small or moderately sized** graphs but is slower than Dijkstra’s algorithm for large graphs without negative weights.

---

# Shortest Path Faster Algorithm (SPFA)

## Overview
The **Shortest Path Faster Algorithm (SPFA)** is an optimized variant of Bellman-Ford that uses a **queue-based approach** to improve efficiency in many practical cases. Instead of iterating blindly |V| - 1 times, SPFA **only processes nodes that need updating**.

## Optimization
- Instead of iterating through all edges in every step, SPFA keeps track of **only the nodes that need updates** using a queue.
- Typically runs in **O(V + E)** on many graphs, making it **faster than standard Bellman-Ford** in practice.

## Worst-Case Complexity
- **O(V × E)** (same as Bellman-Ford in the worst case).
- Often **much faster** in sparse graphs or when negative-weight edges are rare.

---

## Comparison: Bellman-Ford vs. SPFA
| Feature                  | Bellman-Ford           | SPFA                     |
|--------------------------|-----------------------|--------------------------|
| Handles Negative Weights | ✅ Yes                | ✅ Yes                   |
| Detects Negative Cycles  | ✅ Yes                | ✅ Yes                   |
| Worst-Case Complexity    | **O(V × E)**          | **O(V × E)**             |
| Typical Performance      | **Slower**            | **Faster** (O(V + E))    |
| Uses a Queue             | ❌ No                 | ✅ Yes                   |

---

## Conclusion
Bellman-Ford is a powerful algorithm that works on graphs with negative weights and detects negative cycles. The **SPFA variant** optimizes it by reducing unnecessary edge relaxations, making it faster in many cases. However, SPFA still has **O(V × E)** worst-case complexity, making it less efficient than **Dijkstra’s algorithm** when all weights are non-negative.

