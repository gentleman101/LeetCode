class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        ahead = [[0] * (k + 1) for _ in range(2)]
        cur = [[0] * (k + 1) for _ in range(2)]
    
        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                for cap in range(1, k + 1):

                    if buy == 0:  # We can buy the stock
                        cur[buy][cap] = max(0 + ahead[0][cap],
                                        -prices[ind] + ahead[1][cap])

                    if buy == 1:  # We can sell the stock
                        cur[buy][cap] = max(0 + ahead[1][cap],
                                        prices[ind] + ahead[0][cap - 1])

            # Update the 'ahead' array with the current state
            ahead = cur.copy()

        return ahead[0][k]
        