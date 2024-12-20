class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(len(prices)+1)]




        for i in range(n-1,-1,-1):
            for buyFlag in [0,1]:
                if buyFlag:
                    profit = max(dp[i+1][True],-prices[i]+dp[i+1][False])

                else:

                    profit = max(dp[i+1][False],prices[i]-fee+dp[i+1][True])
                dp[i][buyFlag] = profit
        return dp[0][1]
        