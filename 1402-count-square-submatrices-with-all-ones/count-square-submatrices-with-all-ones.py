class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for j in range(len(matrix[0])):
            dp[0][j] = matrix[0][j]

        for i in range(len(matrix)):
            dp[i][0] = matrix[i][0]


        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    dp[i][j]=0

                else:
                    dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
        
        sum = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                sum+=dp[i][j]


        return sum