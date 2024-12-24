class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            # If the middle element is the target
            if nums[m] == target:
                return m

            # Determine which half is sorted
            if nums[l] <= nums[m]:  # Left half is sorted
                if nums[l] <= target < nums[m]:  # Target is in the left half
                    r = m - 1
                else:  # Target is in the right half
                    l = m + 1
            else:  # Right half is sorted
                if nums[m] < target <= nums[r]:  # Target is in the right half
                    l = m + 1
                else:  # Target is in the left half
                    r = m - 1

        return -1  # Target not found




