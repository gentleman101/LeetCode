class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l,r = 1,max(nums)
        def divisorUtil(n):
            divSum = 0

            for num in nums:
                divSum+=ceil(num/n)

            return divSum


        while l<=r:
            mid = (l+r)//2
            div = divisorUtil(mid)
            if div<=threshold:
                r = mid-1

            else:
                l = mid+1

        return l
            

