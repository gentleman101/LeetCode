class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit  = 0
        mini = prices[0]

        for i in range(1,len(prices)):

            profit  = prices[i] - mini

            if profit>maxProfit:
                maxProfit = profit

            mini = min(mini,prices[i])

        return maxProfit
