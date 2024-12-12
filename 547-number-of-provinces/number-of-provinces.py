class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        connected = collections.defaultdict(list)
        count = 0

        for row in range(len(isConnected)):
            for col in range(len(isConnected[0])):
                if (isConnected[row][col]==1) & (row!=col):
                    connected[row].append(col)
                    connected[col].append(row)


        visit = [False]*len(isConnected)


        def dfs(v):
            visit[v]= True
            for i in connected[v]:
                if not visit[i]:
                    dfs(i)

        for i in range(len(isConnected)):
            if not visit[i]:
                count+=1
                dfs(i)
            
        return count
        