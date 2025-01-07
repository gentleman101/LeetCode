class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        ans = len(nums)  # Default position if target is greater than all elements
        
        while l <= r:
            m = (l + r) // 2
            if target < nums[m]:
                # ans = m  # Potential insertion position
                r = m - 1
            elif target > nums[m]:
                l = m + 1
            else:  # Found the target
                return m

        return l  # After the loop, `l` points to the insertion position
 