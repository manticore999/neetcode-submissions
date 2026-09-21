class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for point in points : 
            heapq.heappush(h,[math.sqrt(point[0]**2 +point[1]**2),point])
            res = []
        while k > 0 : 
            res.append( heapq.heappop(h)[1])
            k-=1
        return res