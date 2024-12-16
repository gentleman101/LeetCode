class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Edge cases
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        
        # Helper function to solve for a linear subarray
        def solveUtil(arr):
            m = len(arr)
            dp = [-1] * m  # Initialize DP for the size of the subarray
            
            def recur(ind):
                if dp[ind] != -1:
                    return dp[ind]
                if ind == 0:
                    return arr[ind]
                if ind < 0:
                    return 0
                pick = arr[ind] + recur(ind - 2)
                nonPick = recur(ind - 1)
                dp[ind] = max(pick, nonPick)
                return dp[ind]
            
            return recur(m - 1)
        
        # Compute for the two cases
        return max(solveUtil(nums[1:]), solveUtil(nums[:-1]))
