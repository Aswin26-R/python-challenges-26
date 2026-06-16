from collections import deque


class Graph:
    """
    TODO:
    An undirected graph represented as an adjacency list.

    self.adjacency_list is a dict: {node: [neighbor1, neighbor2, ...]}
    """

    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, node):
        """
        TODO:
        Add a node to the graph (if it doesn't already exist).

        Example:
            g.add_node("A")
            # adjacency_list = {"A": []}
        """
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, node1, node2):
        """
        TODO:
        Add an UNDIRECTED edge between node1 and node2.
        Both nodes are added if they don't exist yet.
        Both nodes appear in each other's neighbor list.

        Example:
            g.add_edge("A", "B")
            # A's neighbors: ["B"]
            # B's neighbors: ["A"]
        """
        self.add_node(node1)
        self.add_node(node2)
        # TODO: Append node2 to node1's list and node1 to node2's list
        pass

    def get_neighbors(self, node):
        """
        TODO:
        Return the list of neighbors for the given node.
        Return [] if node doesn't exist.
        """
        pass

    def bfs(self, start):
        """
        TODO:
        Perform Breadth-First Search starting from 'start'.
        Return a list of all reachable nodes in BFS order (level by level).

        BFS uses a QUEUE (FIFO):
            visited = set with start node
            queue = deque with start node
            result = []

            while queue is not empty:
                node = queue.popleft()  ← take from FRONT
                result.append(node)
                for each neighbor of node:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            return result
        """
        if start not in self.adjacency_list:
            return []
        pass

    def dfs(self, start):
        """
        TODO:
        Perform Depth-First Search starting from 'start'.
        Return a list of all reachable nodes in DFS order.

        DFS uses a STACK (LIFO) — or recursion:
            visited = set()
            stack = [start]
            result = []

            while stack:
                node = stack.pop()  ← take from BACK (LIFO)
                if node not in visited:
                    visited.add(node)
                    result.append(node)
                    for neighbor in reversed(neighbors):  ← reversed for consistent ordering
                        if neighbor not in visited:
                            stack.append(neighbor)

            return result
        """
        if start not in self.adjacency_list:
            return []
        pass

    def has_path(self, start, end):
        """
        TODO:
        Return True if there is a path from start to end, False otherwise.

        Hint: Use BFS or DFS and check if end appears in the visited nodes.
        """
        if start not in self.adjacency_list or end not in self.adjacency_list:
            return False
        pass

    def shortest_path(self, start, end):
        """
        TODO:
        Return the shortest path from start to end as a list of nodes.
        If no path exists, return [].
        If start == end, return [start].

        Algorithm (BFS with parent tracking):
            parent = {start: None}
            queue = deque([start])
            visited = {start}

            while queue:
                node = queue.popleft()
                if node == end:
                    # Reconstruct path by tracing parents
                    path = []
                    while node is not None:
                        path.append(node)
                        node = parent[node]
                    return list(reversed(path))

                for neighbor in self.get_neighbors(node):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        parent[neighbor] = node
                        queue.append(neighbor)

            return []  ← no path found
        """
        if start not in self.adjacency_list or end not in self.adjacency_list:
            return []
        if start == end:
            return [start]
        pass
