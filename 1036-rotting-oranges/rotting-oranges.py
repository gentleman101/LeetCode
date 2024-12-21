class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        q = deque()
        n = len(grid)
        m = len(grid[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        count_fresh_oranges = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((i,j,0))
                if grid[i][j]==1:
                    count_fresh_oranges+=1

        # Movements
        movements = [(1,0),(0,1),(-1,0),(0,-1)]
        max_time = 0
        while q:
            row,col,time = q.popleft()
            max_time = max(max_time,time)

            for moves in movements:
                nrow = row + moves[0]
                ncol = col + moves[1]

                if 0<=nrow<n and 0<=ncol<m and grid[nrow][ncol]==1 and not visited[nrow][ncol]:
                    q.append((nrow,ncol,time+1))
                    count_fresh_oranges-=1
                    visited[nrow][ncol] = True


        if count_fresh_oranges==0:
            return max_time

        else:
            return -1




            
        