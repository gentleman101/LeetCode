class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)

        maxHeap = [-1*values for values in counter.values()]
        heapify(maxHeap)
        q = deque()
        time = 0
        while maxHeap or q:
            time+=1
            if maxHeap:
                cnt = 1+heappop(maxHeap)
                if cnt:
                    q.append([cnt,time+n])

            if q and q[0][1]==time:
                heappush(maxHeap,q.popleft()[0])

        return time

