class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        n = len(prices)

        # Two states for current and future
        ahead = [0, 0]  # ahead[0]: can't buy, ahead[1]: can buy
        curr = [0, 0]
        
        for i in range(n-1,-1,-1):
            for buyFlag in [0,1]:
                if buyFlag:
                    profit = max(ahead[True],-prices[i]+ahead[False])

                else:

                    profit = max(ahead[False],prices[i]-fee+ahead[True])
                curr[buyFlag] = profit
            ahead = curr
        return ahead[1]
        