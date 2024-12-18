class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[-1 for j in range(n)] for i in range(n)] 
        def utilTotal(i,j):
            if dp[i][j] != -1:
                    return dp[i][j]

            # If we are at the bottom of the triangle, return the value in the current cell
            if i == n - 1:
                return triangle[i][j]

            # Calculate the minimum path sum by considering two possible moves: down and diagonal
            down = triangle[i][j] + utilTotal(i + 1, j)
            diagonal = triangle[i][j] + utilTotal(i + 1, j + 1)

            # Store the computed minimum path sum in the memoization table
            dp[i][j] = min(down, diagonal)
            return dp[i][j]

        return utilTotal(0,0)
        