class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        def utilLCS(i,j):
            if i<0 or j<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            matching =0
            if text1[i]==text2[j]:
                matching = 1 + utilLCS(i-1,j-1)
            notMatching = -1e9
            if text1[i]!=text2[j]:
                notMatching = max(utilLCS(i-1,j),utilLCS(i,j-1))
            dp[i][j] = max(matching,notMatching)
            return dp[i][j]

        return utilLCS(n-1,m-1)





        