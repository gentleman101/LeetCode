class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        m = len(isConnected[0])
        adj = defaultdict(list)
        visited = [False]*n
        cnt  = 0
        for r in range(n):
            for c in range(m):
                if r!=c and isConnected[r][c]==1:
                    adj[r].append(c)
                    adj[c].append(r)


        def dfs(city):
            visited[city]=True
            
            for neighbour in adj[city]:
                if not visited[neighbour]:
                    dfs(neighbour)

        for province in range(n):
            if not visited[province]:
                cnt+=1
                dfs(province)

        return cnt



        