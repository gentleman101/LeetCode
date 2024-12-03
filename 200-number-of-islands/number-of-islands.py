class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        islands = 0
        visited = [[False for _ in range(columns)] for _ in range(rows)]
        movements = [(1,0),(0,1),(-1,0),(0,-1)]

        def dfs (row,col):
            visited[row][col]=True
            for move in movements:
                nrow = row + move[0]
                ncol = col + move[1]
                if (
                    0 <= nrow < rows
                    and 0 <= ncol < columns
                    and not visited[nrow][ncol]
                    and grid[nrow][ncol] == "1"
                ):
                    dfs(nrow,ncol)

        for row in range(rows):
            for col in range(columns):
                if grid[row][col] == "1" and not visited[row][col]:
                    islands +=1
                    dfs(row,col)

        return islands

        