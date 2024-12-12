class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        islands = 0
        visited = [[False for i in range(columns)] for j in range(rows)]
                    
        movements = [(1,0),(0,1),(0,-1),(-1,0)]



        def dfs(i,j):
            visited[i][j]=True
            for move in movements:
                nrow = i+move[0]
                ncol = j+move[1]

                if 0 <= nrow < rows and 0 <= ncol < columns and grid[nrow][ncol] == "1" and not visited[nrow][ncol]:
                    dfs(nrow, ncol)

        for row in range(rows):
            for col in range(columns):
                if (grid[row][col]=="1") & (not visited[row][col]):
                    islands+=1
                    dfs(row,col)


        return islands

