class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        # def recurString(indText1,indText2):
        #     # Base Case

        #     if indText1<0 or indText2<0:
        #         return 0

        #     # Check each character
        #     if dp[indText1][indText2]!=-1:
        #         return dp[indText1][indText2]


        #     if text1[indText1]==text2[indText2]:
        #         dp[indText1][indText2] = 1+ recurString(indText1-1,indText2-1)
        #         return dp[indText1][indText2]

        #     if text1[indText1]!=text2[indText2]:
        #         operation1 = recurString(indText1-1,indText2)
        #         operation2 = recurString(indText1,indText2-1)
        #         dp[indText1][indText2] = (max(recurString(indText1-1,indText2),recurString(indText1,indText2-1)))
        #         return dp[indText1][indText2]

        # return recurString(len(text1)-1,len(text2)-1)


        # Tabulation
    # Create a DP table of size (n+1) x (m+1) initialized with -1
        s1 = text1
        s2 = text2
        n = len(s1)
        m = len(s2)
        dp = [[-1 for j in range(m + 1)] for i in range(n + 1)]

        # Initialize the base cases:
        # - The length of LCS with an empty string is 0, so dp[i][0] = 0 for all i
        # - The length of LCS with an empty string is 0, so dp[0][j] = 0 for all j
        for i in range(n + 1):
            dp[i][0] = 0
        for j in range(m + 1):
            dp[0][j] = 0

        # Fill in the DP table by considering characters from both strings
        for ind1 in range(1, n + 1):
            for ind2 in range(1, m + 1):
                if s1[ind1 - 1] == s2[ind2 - 1]:
                    # If the characters match, increment the LCS length
                    dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
                else:
                    # If the characters do not match, take the maximum of
                    # LCS length without one character from s1 or s2
                    dp[ind1][ind2] = max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])
        
        # The value in dp[n][m] represents the length of the Longest Common Subsequence
        return dp[n][m]




            