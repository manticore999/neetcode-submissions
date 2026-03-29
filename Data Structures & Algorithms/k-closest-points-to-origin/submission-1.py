class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [ (math.sqrt(i[0]*i[0] + i[1]*i[1]),i)for i in points ]
        res = []
        heapq.heapify(heap)
        while (k>0) : 
            res.append(heapq.heappop(heap)[1])
            k-=1
        return res