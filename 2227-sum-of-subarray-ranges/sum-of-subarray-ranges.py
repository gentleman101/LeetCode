from typing import List

class Solution:
    def pse(self, arr: List[int], n: int) -> List[int]:
        stack = []
        res = [-1] * n  # Store index of previous smaller element

        for i in range(n):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            res[i] = stack[-1] if stack else -1
            stack.append(i)
        return res

    def nse(self, arr: List[int], n: int) -> List[int]:
        stack = []
        res = [n] * n  # Store index of next smaller element

        for i in range(n - 1, -1, -1):
            while stack and arr[i] < arr[stack[-1]]:
                stack.pop()
            res[i] = stack[-1] if stack else n
            stack.append(i)
        return res

    def pge(self, arr: List[int], n: int) -> List[int]:
        stack = []
        res = [-1] * n  # Store index of previous greater element

        for i in range(n):
            while stack and arr[i] >= arr[stack[-1]]:
                stack.pop()
            res[i] = stack[-1] if stack else -1
            stack.append(i)
        return res

    def nge(self, arr: List[int], n: int) -> List[int]:
        stack = []
        res = [n] * n  # Store index of next greater element

        for i in range(n - 1, -1, -1):
            while stack and arr[i] > arr[stack[-1]]:
                stack.pop()
            res[i] = stack[-1] if stack else n
            stack.append(i)
        return res

    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        minSum = 0
        maxSum = 0

        # Creating required stacks
        pse_stack = self.pse(nums, n)
        nse_stack = self.nse(nums, n)
        pge_stack = self.pge(nums, n)
        nge_stack = self.nge(nums, n)

        for i in range(n):
            # Calculating minimum contributions
            minleft = i - pse_stack[i]
            minright = nse_stack[i] - i
            minSum += minleft * minright * nums[i]

            # Calculating maximum contributions
            maxleft = i - pge_stack[i]
            maxright = nge_stack[i] - i
            maxSum += maxleft * maxright * nums[i]

        return maxSum - minSum
