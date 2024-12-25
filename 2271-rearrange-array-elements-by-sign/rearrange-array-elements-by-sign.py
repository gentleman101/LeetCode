class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p,n = 0,1
        res = [0]*len(nums)
        for num in nums:
            if num<0:
                res[n]=num
                n+=2
            if num>0:
                res[p]=num
                p+=2

        return res

        