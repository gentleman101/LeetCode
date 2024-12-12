from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        q = deque()
        fresh_count = 0

        # Initialize the queue with all initially rotten oranges
        for row in range(rows):
            for col in range(columns):
                if grid[row][col] == 2:
                    q.append((row, col, 0))  # (row, col, time)
                elif grid[row][col] == 1:
                    fresh_count += 1

        # Directions for 4 possible movements
        movements = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        max_time = 0

        # Perform BFS
        while q:
            row, col, time = q.popleft()
            max_time = max(max_time, time)

            for move in movements:
                nrow, ncol = row + move[0], col + move[1]

                # If the neighboring cell is a fresh orange, rot it and add to the queue
                if 0 <= nrow < rows and 0 <= ncol < columns and grid[nrow][ncol] == 1:
                    grid[nrow][ncol] = 2  # Mark as rotten
                    fresh_count -= 1  # Decrease fresh orange count
                    q.append((nrow, ncol, time + 1))

        # If there are any fresh oranges left, return -1
        return max_time if fresh_count == 0 else -1
