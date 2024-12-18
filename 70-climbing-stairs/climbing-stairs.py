class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        def utilStairs(i):
            if i==0 or i==1:
                return 1 

            if dp[i]!=-1:
                return dp[i]

            dp[i] = utilStairs(i-1) +utilStairs(i-2)
            return dp[i]

    
        return utilStairs(n)