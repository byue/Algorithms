# Breadth-First Search (BFS)

## Overview
**Breadth-First Search (BFS)** is a fundamental graph traversal algorithm used to explore nodes level by level. It guarantees the shortest path in **unweighted graphs** and is widely used in various applications such as pathfinding, networking, and social network analysis.

---

## **How BFS Works**
1. **Initialize** a queue and start from a given **source node**.
2. **Mark the source node as visited** and store its parent (if needed).
3. **Iterate through the queue**:
   - Dequeue a node and explore all its **unvisited neighbors**.
   - Mark each neighbor as visited, record its parent, and **enqueue it**.
4. **Repeat until the queue is empty**.

BFS **expands outward in layers**, ensuring that a node is visited **only after all nodes in previous layers** have been explored.

---

## **Runtime Complexity**
| **Graph Representation** | **Time Complexity** | **Space Complexity** |
|-------------------------|--------------------|---------------------|
| Adjacency List          | **O(V + E)**       | **O(V)** (Queue & Visited Set) |
| Adjacency Matrix        | **O(V²)**          | **O(V)** |

- **V = Number of vertices (nodes)**
- **E = Number of edges**

In an adjacency list representation, BFS runs in **O(V + E)** time, as each node and edge is processed once.

---

## **Applications of BFS**
### **1. Shortest Path in Unweighted Graphs**
   - BFS finds the shortest path from a **source node** to all other nodes in an **unweighted graph**.
   - Example: **Google Maps walking directions** (where each step is equal in cost).

### **2. Connected Components in Graphs**
   - BFS helps **discover all connected nodes** in an undirected graph.
   - Used in **network analysis** to detect **clusters of users**.

### **3. Web Crawlers**
   - Search engines use BFS to explore **web pages level by level**.

### **4. Social Network Analysis**
   - BFS is used to measure **friend recommendations** (e.g., **shortest connection path in LinkedIn or Facebook**).

### **5. Solving Puzzles and Games**
   - Used in **mazes, chess moves, and AI decision trees**.

---

## **BFS vs. Depth-First Search (DFS)**
| Feature         | **BFS**                     | **DFS**                     |
|---------------|---------------------------|---------------------------|
| **Traversal Order** | Level-by-level (Queue) | Deep-first (Stack/Recursion) |
| **Shortest Path (Unweighted Graphs)** | ✅ Yes | ❌ No |
| **Memory Usage** | Higher (O(V) queue) | Lower (O(depth) recursion) |
| **Better for** | Finding shortest paths, connected components | Exploring deep structures, cycle detection |

- **Use BFS when finding the shortest path** or **exploring breadth-wise**.
- **Use DFS for deep search problems**, like **backtracking** or **topological sorting**.

---

## **Conclusion**
BFS is a **powerful algorithm** for graph traversal that ensures **shortest paths in unweighted graphs**. Its applications span across **search engines, social networks, and AI**. While **BFS is more memory-intensive than DFS**, it is the preferred choice when **optimal paths matter**.
