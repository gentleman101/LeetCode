class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        r,c = len(grid),len(grid[0])
        dp = [[-1 for _ in range(c)] for _ in range(r)]
        def utilPathSum(row,col):
            # base case
            if row==0 and col==0:
                return grid[0][0]

            if dp[row][col]!=-1:
                return dp[row][col]
            # Up
            up,left = float(inf),float(inf)
            if row>0:
                up = grid[row][col] + utilPathSum(row-1,col)

            # Left

            if col>0:
                left = grid[row][col] + utilPathSum(row,col-1)

            dp[row][col] = min(up,left)
            return dp[row][col] 

        return utilPathSum(r-1,c-1)
        