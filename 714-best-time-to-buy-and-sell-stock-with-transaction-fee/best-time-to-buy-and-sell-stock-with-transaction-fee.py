class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        n = len(prices)
        dp = [[-1 for _ in range(2)] for _ in range(len(prices))]
        def utilProfit(i,buyFlag):
            if i==n:
                return 0
            if dp[i][buyFlag]!=-1:
                return dp[i][buyFlag]


            if buyFlag:

                profit = max(utilProfit(i+1,True),-prices[i]+utilProfit(i+1,False))

            else:

                profit = max(utilProfit(i+1,False),prices[i]-fee+utilProfit(i+1,True))
            dp[i][buyFlag] = profit
            return dp[i][buyFlag]

        return utilProfit(0,True)
        