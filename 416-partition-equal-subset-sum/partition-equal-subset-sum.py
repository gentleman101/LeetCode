class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False  # If the total sum is odd, it's impossible to partition

        target = sum(nums) // 2
        n = len(nums)

        # Initialize the dp array, where -1 indicates that a value hasn't been calculated yet
        dp = [[-1 for _ in range(target + 1)] for _ in range(n)]

        def utilPartition(i, total):
            # Base case: If the total is 0, return True (we found a valid subset)
            if total == 0:
                return True
            
            # Base case: If we have no elements left to consider
            if i < 0:
                return False

            # Check if we have already computed the result for dp[i][total]
            if dp[i][total] != -1:
                return dp[i][total]

            # Option 1: Don't take the current element
            notTake = utilPartition(i - 1, total)

            # Option 2: Take the current element (if it's less than or equal to total)
            Take = False
            if nums[i] <= total:
                Take = utilPartition(i - 1, total - nums[i])

            # Store the result in the dp array and return it
            dp[i][total] = Take or notTake
            return dp[i][total]

        return utilPartition(n - 1, target)
