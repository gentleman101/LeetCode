class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        def backtracking(start, comb, total):
            if total == target:
                res.append(comb.copy())
                return
            for i in range(start, len(candidates)):
                # If the current number exceeds the target, skip it
                if total + candidates[i] > target:
                    continue
                # Include the number and proceed with the next recursive call
                comb.append(candidates[i])
                backtracking(i, comb, total + candidates[i])
                comb.pop()  # Backtrack

        backtracking(0, [], 0)
        return res
