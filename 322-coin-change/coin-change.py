class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[float('inf')] * (amount + 1) for _ in range(n)]

        # Initialize for 0 total
        for i in range(n):
            dp[i][0] = 0

        # Initialize for the first row
        for total in range(amount + 1):
            if total % coins[0] == 0:
                dp[0][total] = total // coins[0]

        # Fill the DP table
        for i in range(1, n):
            for total in range(amount + 1):
                notTake = dp[i - 1][total]
                Take = float('inf')
                if coins[i] <= total:
                    Take = 1 + dp[i][total - coins[i]]
                dp[i][total] = min(notTake, Take)

        # Final answer
        result = dp[n - 1][amount]
        return result if result != float('inf') else -1
