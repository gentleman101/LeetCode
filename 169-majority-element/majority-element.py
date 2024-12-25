class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        el = nums[0]
        cnt = 1

        for i in range(1,len(nums)):

            if nums[i]==el:
                cnt+=1
            else:
                cnt-=1
                if cnt==0:
                    el=nums[i+1]

        return el
                
        