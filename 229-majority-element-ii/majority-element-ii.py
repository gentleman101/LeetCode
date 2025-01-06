from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt1, cnt2 = 0, 0
        el1, el2 = None, None  # Initialize candidates as None

        # Step 1: Find potential candidates
        for num in nums:
            if cnt1 == 0 and num != el2:
                el1 = num
                cnt1 = 1
            elif cnt2 == 0 and num != el1:
                el2 = num
                cnt2 = 1
            elif num == el1:
                cnt1 += 1
            elif num == el2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        # Step 2: Verify candidates
        cnt1, cnt2 = 0, 0
        for num in nums:
            if num == el1:
                cnt1 += 1
            elif num == el2:
                cnt2 += 1

        # Return elements that appear more than n // 3 times
        result = []
        n = len(nums)
        if cnt1 > n // 3:
            result.append(el1)
        if cnt2 > n // 3:
            result.append(el2)

        return result
