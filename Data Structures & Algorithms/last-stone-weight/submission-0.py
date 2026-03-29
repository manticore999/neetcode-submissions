class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = stones  
        heapq.heapify_max(stones)
        while (len(maxheap) > 1 ):
            x = heapq.heappop_max(maxheap)
            y = heapq.heappop_max(maxheap)
            if x > y :
                heapq.heappush_max(maxheap,x-y)
        return maxheap[0] if len(maxheap) == 1  else 0