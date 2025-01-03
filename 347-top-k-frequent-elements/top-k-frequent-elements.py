class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        maxHeap = [[-1*freq,num] for num,freq in counter.items()]
        heapify(maxHeap)
        i=0
        res = []
        while i<k:
            res.append(heappop(maxHeap)[1])
            i+=1

        return res


