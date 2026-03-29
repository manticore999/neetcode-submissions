class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for point in range(len(points)):
            for nei in range(len(points)):
                if nei !=point : 
                    distance = abs(points[point][0]-points[nei][0]) + abs(points[point][1]-points[nei][1])
                    adj[point].append([distance,nei])
        visited = set()
        res = 0
        q = [[0,0]]
        while q and len(visited)<len(points):
            cost , p = heapq.heappop(q)
            if p in visited :
                continue
            visited.add(p)
            res+=cost
            for n in adj[p]:
                heapq.heappush(q,n)
        return res    
        

