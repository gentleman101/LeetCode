class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])

        pq = []
        mad = -1
        movements = [(1,0),(0,1),(-1,0),(0,-1)]
        dist = [[float(inf) for _ in range(m)] for _ in range(n)]


        heappush(pq,(0,0,0))
        dist[0][0] = heights[0][0]
        max_effort = 0
        while pq:
            energy,row,col = heappop(pq)
            if row == n - 1 and col == m - 1:
                return energy
            for move in movements:
                nrow = row + move[0]
                ncol = col + move[1]

                if 0<=nrow<n and 0<=ncol<m:
                    effort = abs(heights[nrow][ncol]-heights[row][col])
                    max_effort = max(energy,effort)
                    if max_effort<dist[nrow][ncol]:
                        dist[nrow][ncol] = effort
                        heappush(pq,(max_effort,nrow,ncol))

        return dist[n-1][m-1]
                    



        


