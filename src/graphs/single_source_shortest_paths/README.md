# Single Source Shortest Path (SSSP) Algorithms

## Overview
Single Source Shortest Path (**SSSP**) algorithms compute the shortest paths from a **single source node** to all other nodes in a graph. The choice of algorithm depends on the properties of the graph, including whether it is **weighted or unweighted**, **acyclic or general**, and whether it contains **negative weights**.

---

## **SSSP Algorithms and Their Properties**

| **Restrictions**      | **Graph Type**      | **Weights**        | **Algorithm Name**    | **Running Time O(·)**  |
|----------------------|-------------------|-------------------|----------------------|-----------------------|
| **General Unweighted** | Any               | Unweighted        | **BFS**              | **O(V + E)**         |
| **DAG**              | Directed Acyclic   | Any               | **DAG Relaxation**   | **O(V + E)**         |
| **General Any**      | Any                | Any               | **Bellman-Ford**     | **O(V · E)**         |
| **General Non-negative** | Any            | Non-negative      | **Dijkstra**         | **O(V log V + E)**   |

---

## **Algorithm Descriptions**

### **1. Breadth-First Search (BFS)**
- **Use Case:** Graphs with **unweighted** edges.
- **Approach:** Expands nodes layer by layer using a **queue**.
- **Time Complexity:** **O(V + E)**
- **Why It Works:** Since all edges have the same weight, the shortest path is the path with the fewest edges.

### **2. DAG Relaxation**
- **Use Case:** **Directed Acyclic Graphs (DAGs)** with any weights.
- **Approach:** Uses **topological sorting** followed by **relaxation** in topological order.
- **Time Complexity:** **O(V + E)**
- **Why It Works:** Since there are no cycles, a topological order guarantees that all nodes are processed in a valid dependency sequence.

### **3. Bellman-Ford Algorithm**
- **Use Case:** **Any graph**, including those with **negative weights**.
- **Approach:** Performs **|V| - 1 iterations**, relaxing all edges in each iteration.
- **Time Complexity:** **O(V · E)**
- **Why It Works:** The shortest path has at most **V - 1 edges**, so iterating **V - 1 times** ensures correctness.
- **Bonus:** Can detect **negative weight cycles**.

### **4. Dijkstra's Algorithm**
- **Use Case:** **Any graph with non-negative weights**.
- **Approach:** Uses a **priority queue (min-heap)** to always expand the **closest unvisited node**.
- **Time Complexity:** **O(V log V + E)** (with binary heap)  
- **Why It Works:** Expanding nodes greedily ensures that each node’s shortest path is determined before moving to farther nodes.

---

## **Choosing the Right Algorithm**
| **Graph Type** | **Edge Weights** | **Best Algorithm** |
|--------------|----------------|------------------|
| **Unweighted Graphs** | No weights | **BFS** |
| **DAGs (Acyclic Graphs)** | Any weights | **DAG Relaxation** |
| **General Graphs (with possible negative weights)** | Any | **Bellman-Ford** |
| **General Graphs (no negative weights)** | Non-negative only | **Dijkstra** |

---

## **Conclusion**
The choice of SSSP algorithm depends on the properties of the graph:
- **BFS** is ideal for unweighted graphs.
- **DAG Relaxation** leverages topological sorting for efficiency.
- **Bellman-Ford** handles negative weights and detects negative cycles.
- **Dijkstra’s Algorithm** is the fastest for graphs **without negative weights**.

Understanding these algorithms helps optimize shortest path computations in real-world applications like **navigation, networking, and AI pathfinding**.
