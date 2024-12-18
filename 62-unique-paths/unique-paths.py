class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for i in range(m)] for j in range(n)]
        def bot(m,n):
            if m==0 or n==0:
                return 1
            # if m<0 or n<0:
            #     return 0
            if dp[n][m]!=-1:
                return dp[n][m]
            if m>0:
                up = bot(m-1,n)
            if n>0:
                left = bot(m,n-1)
            dp[n][m]=up+left
            return dp[n][m]

        return bot(m-1,n-1)

    # def uniquePaths(self, m: int, n: int) -> int:
    #     dp = [[-1 for i in range(n)] for j in range(m)]
    #     # base cases
    #     # loop m and n

    #     for i in range(m):
    #         for j in range(n): 
    #             if i==0 and j==0:
    #                 dp[i][j]=1
    #                 continue
    #             up=0
    #             left=0
    #             if i>0:       
    #                 up = dp[i-1][j]
    #             if j>0:
    #                 left = dp[i][j-1]
    #             dp[i][j]=up+left

    #     return dp[m-1][n-1]


        