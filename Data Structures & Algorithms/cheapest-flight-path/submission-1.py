class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)

        gcosts = [float("inf")]*n
        gcosts[src] = 0
        
        for i in range(k+1):
            temp = gcosts.copy()
            for flight in flights :
                s,c,cost = flight
                if gcosts[s] == float("inf"):
                    continue
                if gcosts[s]+cost < temp[c]:
                    temp[c] = gcosts[s]+cost
            gcosts = temp.copy()
        return gcosts[dst] if gcosts[dst] < float("inf") else -1


        