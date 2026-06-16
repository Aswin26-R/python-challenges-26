# Challenge 33: Graph Traversal

**Level:** 4 – Expert Python
**Difficulty:** ⭐⭐⭐⭐ (Expert)
**Estimated Time:** 90 minutes

---

## Learning Objectives

By completing this challenge, you will learn:

- What a graph is and how to represent it
- Breadth-First Search (BFS) — explores level by level
- Depth-First Search (DFS) — explores as deep as possible
- Finding shortest paths in unweighted graphs
- Detecting cycles in a graph

---

## Problem Description

A **graph** is a collection of nodes (vertices) connected by edges. Graphs model real-world networks: social networks, road maps, computer networks, and more.

You will implement a `Graph` class and traversal algorithms on it.

---

## Requirements

- [ ] `Graph` class with:
  - `add_node(node)` — add a node
  - `add_edge(node1, node2)` — add an undirected edge
  - `get_neighbors(node)` — return neighbors of a node
  - `bfs(start)` — Breadth-First Search traversal, returns visited order
  - `dfs(start)` — Depth-First Search traversal, returns visited order
  - `has_path(start, end)` — returns `True` if a path exists between start and end
  - `shortest_path(start, end)` — returns the shortest path as a list of nodes

---

## Expected Behavior

```python
g = Graph()
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "D")
g.add_edge("D", "E")

g.bfs("A")
# Returns: ["A", "B", "C", "D", "E"]  (level by level)

g.dfs("A")
# Returns: ["A", "B", "D", "C", "E"] or similar  (depends on order)

g.has_path("A", "E")
# Returns: True

g.has_path("A", "X")
# Returns: False

g.shortest_path("A", "E")
# Returns: ["A", "B", "D", "E"] or ["A", "C", "D", "E"]  (length 4)
```

---

## Graph Representation

Use an **adjacency list** — a dictionary where each key is a node and its value is a list of its neighbors:

```python
{
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"]
}
```

---

## BFS vs DFS

**BFS (Breadth-First Search):**
- Uses a **queue** (FIFO)
- Explores all neighbors at current depth before going deeper
- Finds shortest paths in unweighted graphs
- Good for: "What's the shortest route?"

**DFS (Depth-First Search):**
- Uses a **stack** (or recursion)
- Goes as deep as possible before backtracking
- Good for: "Is there a path? What paths exist?"

---

## Hints

> **Hint 1:** Store the graph as `self.adjacency_list = {}` — a dict of node → list of neighbors.

> **Hint 2:** BFS: use `from collections import deque`. Start with `queue = deque([start])`, `visited = {start}`.

> **Hint 3:** DFS: use a stack `stack = [start]` or recursion. Mark nodes visited to avoid infinite loops.

> **Hint 4:** `shortest_path`: modify BFS to also track parent nodes. Reconstruct path from end to start using parents.

---

## How to Run the Tests

```bash
cd level-04-expert/challenge-33-graph-traversal
pytest tests/ -v
```
