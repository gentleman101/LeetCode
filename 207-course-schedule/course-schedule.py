class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        visited = [False] * numCourses
        path  = [False] * numCourses


        for c1,c2 in prerequisites:
            adj[c2].append(c1)



        def dfs(c):
            visited[c] = True
            path[c] = True

            for neighbour in adj[c]:
                if not visited[neighbour]:
                    if dfs(neighbour)==False:
                        return False
                else:
                    if path[neighbour]:
                        return False

            path[c] = False
            return True

        for course in range(numCourses):
            if not visited[course]:
                if not  dfs(course):
                    return False
        

        return True