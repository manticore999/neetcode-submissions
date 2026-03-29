class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for src,target,v in times: 
            adj[src].append([v,target])
        visited = set()
        q = [(0,k)]
        res = 0
        while q and len(visited)<n :
            cost,node = heapq.heappop(q)
            if node in visited : 
                continue
            visited.add(node)
            res = max(cost,res)
            for a in adj[node]:
                a[0]+=cost
                heapq.heappush(q,a)
        return res if len(visited)==n else -1

