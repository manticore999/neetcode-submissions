class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [[float('inf')] *(k+2) for i in range(n)]
        
        dist[src][0] = 0

        adj = defaultdict(list)
        
        for s,d,price in flights : 
            adj[s].append([price,d])
        
        minh = [(0,src,0)]
        
        while minh : 
            cost , source, stop = heapq.heappop(minh)
            if source == dst : return cost
            if  stop== k+1 : 
                continue
            for price,hop in adj[source]: 
                new_price = cost+price
                if new_price < dist[hop][stop+1]:
                    heapq.heappush(minh,(new_price,hop,stop+1))
                    dist[hop][stop+1] = new_price
        return -1