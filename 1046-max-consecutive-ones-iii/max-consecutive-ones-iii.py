from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        max_length = 0

        for r in range(len(nums)):
            # Reduce `k` for each zero encountered
            if nums[r] == 0:
                k -= 1

            # If `k` goes negative, shrink the window from the left
            if k<0:
                if nums[l]==0:
                    k+=1
                l+=1

            # Update the maximum length
            max_length = max(max_length, r - l + 1)

        return max_length
