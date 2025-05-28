from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Check if the start or end cell is blocked
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        visited = [[False for _ in range(n)] for _ in range(n)]
        q = deque()
        movements = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        q.append((0, 0, 1))  # (row, col, step count)
        visited[0][0] = True

        while q:
            row, col, step = q.popleft()

            # If we reach the bottom-right cell
            if row == n-1 and col == n-1:
                return step

            # Explore all possible movements
            for move in movements:
                nrow = row + move[0]
                ncol = col + move[1]

                # Check bounds, visited, and grid value
                if 0 <= nrow < n and 0 <= ncol < n and not visited[nrow][ncol] and grid[nrow][ncol] == 0:
                    q.append((nrow, ncol, step + 1))
                    visited[nrow][ncol] = True

        # If no path is found
        return -1
