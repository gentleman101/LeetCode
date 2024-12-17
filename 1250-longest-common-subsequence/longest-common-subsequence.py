class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        def recurString(indText1,indText2):
            # Base Case

            if indText1<0 or indText2<0:
                return 0

            # Check each character
            if dp[indText1][indText2]!=-1:
                return dp[indText1][indText2]


            if text1[indText1]==text2[indText2]:
                dp[indText1][indText2] = 1+ recurString(indText1-1,indText2-1)
                return dp[indText1][indText2]

            if text1[indText1]!=text2[indText2]:
                operation1 = recurString(indText1-1,indText2)
                operation2 = recurString(indText1,indText2-1)
                dp[indText1][indText2] = (max(recurString(indText1-1,indText2),recurString(indText1,indText2-1)))
                return dp[indText1][indText2]

        return recurString(len(text1)-1,len(text2)-1)


        # Tabulation
        n = len(text1)
        m = len(text2)

        for i in range(n+1):
            dp[i][0] = 0


        for j in range(m+1):
            dp[0][j] = 0

        for i in range(n+1):
            for j in range(m+1):

                if text1[n-1]==text2[m-1]:
                    dp[n][m] = 1+ dp[n-1][m-1]

                else:
                    dp[n][m] = max(dp[n-1][m],dp[indText1][indText2-1])

        return dp[n][m]




            