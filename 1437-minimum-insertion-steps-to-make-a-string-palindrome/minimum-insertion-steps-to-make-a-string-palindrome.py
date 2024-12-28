class Solution:
    def minInsertions(self, s: str) -> int:
        s2 = s[::-1]
        n = len(s)

        dp = [[-1 for _ in range(n)] for _ in range(n)]
        def utilInsertions(i,j):
            if i<0 or j<0:
                return 0
            length = 0

            if dp[i][j]!=-1:
                return dp[i][j]

            if s[i]==s2[j]:
                length = 1+utilInsertions(i-1,j-1)

            else:
                length = max(utilInsertions(i-1,j),utilInsertions(i,j-1))


            dp[i][j] = length
            return dp[i][j]

        return n-utilInsertions(n-1,n-1)
        
        