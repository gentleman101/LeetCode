class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1 for _ in range(amount+1)] for _ in range(n)]
        def utilChange(i, total):
            # Base case: If the total is 0, no coins are needed
            if total == 0:
                return 0
            # Base case: If no coins are left and the amount is not 0, return a large value (infeasible)
            if i < 0:
                return float('inf')

            if dp[i][total] !=-1:
                return dp[i][total]
            # Do not take the current coin
            notTake = utilChange(i - 1, total)
            # Take the current coin if it doesn't exceed the total
            Take = float('inf')
            if coins[i] <= total:
                Take = 1 + utilChange(i, total - coins[i])

            dp[i][total] = min(notTake, Take)
            return dp[i][total]

        result = utilChange(n - 1, amount)
        # If result is still a large value, it means the amount cannot be made up
        return result if result != float('inf') else -1
