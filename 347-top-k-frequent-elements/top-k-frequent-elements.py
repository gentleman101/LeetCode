class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # countDict = defaultdict(list)
        countList = [[] for _ in range(len(nums)+1)]
        for i in set(nums):
            cnt  = nums.count(i)
            countList[cnt].append(i)
        res = []
        for i in range(len(countList)-1,0,-1):

            res.extend(countList[i])
            if k==len(res):
                return res


        