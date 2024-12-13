class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        q=deque()
        color = [-1]*len(graph)

        for start in range(len(graph)):
            if color[start]==-1:
                color[start]=0
                q.append(start)

            while q:
                node = q.popleft()

                for nei in graph[node]:
                    if color[nei]==-1:
                        color [nei]= 1-color[node]
                        q.append(nei)
                    elif color[nei]==color[node]:
                        return False
        return True

            

        