class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 0

        for j in range(m+1):
            dp[0][j] = 0

        for i in range(1,n+1):
            for j in range(1,m+1):
                matching = 0
                notMatching = -1e9
                if text1[i-1]==text2[j-1]:
                    matching = 1 + dp[i-1][j-1]
                else:
                    notMatching = max(dp[i-1][j],dp[i][j-1])
                dp[i][j] = max(matching,notMatching)

        return dp[n][m]





        