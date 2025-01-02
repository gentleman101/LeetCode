class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        for num in nums:
            heappush(q,-1*num)

        for i in range(k):
            result = heappop(q)

        return result*-1