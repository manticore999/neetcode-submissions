class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int: 
        heapq.heapify_max(stones)
        
        while len(stones)> 1 : 
            x = heapq.heappop_max(stones)
            if not stones : return x
            y = heapq.heappop_max(stones)
            difference = x-y 
            if difference > 0 :
                heapq.heappush_max(stones,difference)
        return 0 if len(stones) == 0 else stones[0]