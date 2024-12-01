class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(comb, hmap):
            # Base case: if the combination has the same length as nums, add to results
            if len(comb) == len(nums):
                res.append(comb.copy())
                return

            for num in range(len(nums)):
                if num not in hmap:
                    # Choose
                    comb.append(nums[num])
                    hmap.add(num)
                    # Explore
                    backtrack(comb, hmap)
                    # Unchoose
                    comb.pop()
                    hmap.remove(num)

        backtrack([], set())  # Start with an empty combination and empty set
        return res
