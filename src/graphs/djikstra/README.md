# Dijkstra's Algorithm for Single Source Shortest Paths

## Overview
Dijkstra's algorithm is a **greedy algorithm** used to find the **shortest path from a single source node to all other nodes** in a weighted graph. It guarantees the shortest path in graphs with **non-negative weights** and is widely used in real-world applications like GPS navigation and network routing.

---

## **Theory of Dijkstra's Algorithm**
Dijkstra's algorithm works by iteratively expanding the shortest-known path from the source node. It maintains a **priority queue (min-heap)** that always expands the **closest unvisited node**, ensuring that each node's shortest path is determined before moving to farther nodes.

### **Key Steps:**
1. Assign an initial distance of **0** to the source node and **infinity (∞)** to all other nodes.
2. Use a **priority queue (min-heap)** to always expand the node with the smallest known distance.
3. For each neighboring node, update its shortest distance if a **better path** is found.
4. Repeat until all nodes have been visited.

---

## **Time Complexity**
The runtime of Dijkstra's algorithm depends on the data structure used for the priority queue:

| Priority Queue Type  | Time Complexity  |
|----------------------|-----------------|
| **Binary Heap** (`heapq`) | \( O((V + E) \log V) \) |
| **Fibonacci Heap**  | \( O(V \log V + E) \) |

- **V** = Number of vertices (nodes)
- **E** = Number of edges  
- Using a **Fibonacci Heap** results in better performance for **dense graphs**, but binary heaps are simpler to implement.

### **Space Complexity**
- **O(V + E)** (storing graph data and priority queue)

---

## **Comparison with Prim’s Algorithm**
Dijkstra’s and Prim’s algorithms are similar in that they both use a **greedy approach** and a **priority queue**. However, they solve different problems:

| Feature  | **Dijkstra’s Algorithm** | **Prim’s Algorithm** |
|----------|-------------------------|---------------------|
| **Purpose** | Finds shortest paths from a **single source** | Finds the **minimum spanning tree** (MST) |
| **Graph Type** | Weighted graphs with **non-negative** weights | Weighted **undirected** graphs |
| **Approach** | Expands paths based on the **shortest known distance** | Expands edges based on the **minimum weight** |
| **Priority Queue** | Stores **nodes with distances** | Stores **edges with weights** |
| **Result** | A shortest-path tree rooted at the source | A spanning tree connecting all nodes |

### **Key Difference:**  
- **Dijkstra’s algorithm** finds the shortest path **to all nodes** starting from a single source.
- **Prim’s algorithm** constructs a **tree** connecting all nodes with the minimum total edge weight.

---

## **When to Use Dijkstra's Algorithm**
| **Scenario** | **Best Choice** | **Reason** |
|-------------|---------------|------------|
| **Finding shortest paths from a single source** | Dijkstra’s Algorithm | Provides shortest paths to all nodes efficiently |
| **Graph has only positive weights** | Dijkstra’s Algorithm | Works correctly without modifications |
| **Graph contains negative weights** | Bellman-Ford Algorithm | Dijkstra does not handle negative weights |
| **Finding a minimum-cost connection for all nodes** | Prim’s Algorithm | Builds an MST instead of shortest paths |

---

## **Applications of Dijkstra’s Algorithm**
Dijkstra’s algorithm is widely used in:
- **Navigation Systems (GPS & Maps):**  
  - Computes the shortest driving or walking routes.
- **Network Routing (Internet & Telecommunications):**  
  - Optimizes packet forwarding and routing protocols.
- **Robotics & AI Pathfinding:**  
  - Guides autonomous robots and AI agents through optimal paths.
- **Operations Research:**  
  - Solves logistics and supply chain routing problems.
- **Video Game Pathfinding:**  
  - Used in A* search for AI movement in games.

---

## **Conclusion**
Dijkstra’s algorithm is a fundamental algorithm for shortest path problems in graphs. It efficiently finds the shortest path from a single source to all other nodes using a **greedy** approach and a **priority queue**. Compared to Prim’s algorithm, which finds the **minimum spanning tree**, Dijkstra’s algorithm is the preferred choice when finding the **shortest routes** between points in a network.

Understanding Dijkstra’s and Prim’s algorithms helps in optimizing network design, navigation systems, and various computational problems in computer science.
