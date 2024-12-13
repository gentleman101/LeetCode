from collections import deque
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n  # -1: uncolored, 0: color A, 1: color B

        for start in range(n):
            if color[start] == -1:  # If the node is unvisited
                q = deque([start])
                color[start] = 0  # Start coloring with color 0

                while q:
                    node = q.popleft()
                    for neighbour in graph[node]:
                        if color[neighbour] == -1:  # If uncolored, assign opposite color
                            color[neighbour] = 1 - color[node]
                            q.append(neighbour)
                        elif color[neighbour] == color[node]:  # If same color, not bipartite
                            return False

        return True
