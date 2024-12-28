class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-1 for _ in range(k+1)] for _ in range(2)] for _ in range(n)]
        def utilProfit(i,buy,trans):
            if i==n or trans==0:
                return 0

            profit = 0
            
            if dp[i][buy][trans]!=-1:
                return dp[i][buy][trans]

            if buy:
                profit =max(utilProfit(i+1,buy,trans),-prices[i]+utilProfit(i+1,False,trans))

            if not buy:
                profit = max(utilProfit(i+1,buy,trans),prices[i] + utilProfit(i+1,True,trans-1))

            dp[i][buy][trans] = profit 

            return dp[i][buy][trans]

        return utilProfit(0,True,k)
