import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for i in range(n)]
        for i, j, l in flights:
            adj[i].append([j, l])
        print(adj)
        dis = [float("inf") for _ in range(n)]
        dis[src] = 0
        heap = [(0, 0, src)]
        while heap:
            stops, price, city = heapq.heappop(heap)
            for c in adj[city]:
                if c[0] == dst:
                    if stops <= k and (price + c[1]) < dis[dst]:
                        dis[dst] = price + c[1]
                else:
                    if stops < k and (price + c[1]) < dis[c[0]]:
                        dis[c[0]] = price + c[1]
                        heapq.heappush(heap, (stops + 1, price + c[1], c[0]))
        if dis[dst] == float("inf"):
            return -1
        return dis[dst]