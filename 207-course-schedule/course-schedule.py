class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegrees = [0]*numCourses
        q = deque()
        res = []
        for c1,c2 in prerequisites:
            adj[c2].append(c1)

        for courses in range(numCourses):
            for i in adj[courses]:
                indegrees[i]+=1

        for degrees in range(numCourses):
            if indegrees[degrees]==0:
                q.append(degrees)

        while q:
            node = q.popleft()
            res.append(node)

            for neighbours in adj[node]:
                indegrees[neighbours]-=1
                if indegrees[neighbours]==0:
                    q.append(neighbours)


        return len(res)==numCourses



