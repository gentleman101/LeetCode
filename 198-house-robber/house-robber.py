class Solution:
    def rob(self, nums: List[int]) -> int:
        # n = len(nums)
        # dp = [-1 for _ in range(n)]
        # def utilRob(i):
        #     if i==0:
        #         return nums[i]
        #     if i<0:
        #         return 0
        #     if dp[i]!=-1:
        #         return dp[i]
        #     notTake = utilRob(i-1)
        #     Take = nums[i] + utilRob(i-2)
        #     dp[i] = max(Take,notTake)
        #     return dp[i]
        # return utilRob(n-1)

        n = len(nums)
        prev=nums[0]
        prev2=0
        
        for i in range(1,n):
            notTake = prev

            Take = nums[i]
            if i>1:
                Take +=  prev2
            curr = max(Take,notTake)
            prev2 = prev
            prev = curr
        return prev

        