class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        l,r = max(nums),sum(nums)

        def largestsum(i):
            cumSum = 0
            parts = 1
            for num in nums:
                if cumSum + num>i:
                    parts+=1
                    cumSum=num
                else:
                    cumSum+=num

            return parts

        while l<=r:
            mid = (l+r)//2
            part = largestsum(mid)
            if part<=k:
                r = mid-1
            else:
                l = mid+1

        return l




        