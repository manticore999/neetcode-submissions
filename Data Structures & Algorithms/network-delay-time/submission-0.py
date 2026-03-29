from collections import defaultdict, deque
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))   # store as tuple for clarity
        
        best_time = {}                 # node -> shortest known time
        q = deque()
        q.append((k, 0))               # start node with time 0
        
        while q:
            node, time_so_far = q.popleft()
            
            # If we already have a better time for this node, skip processing
            if node in best_time and time_so_far >= best_time[node]:
                continue
            
            best_time[node] = time_so_far
            
            for neighbor, weight in graph[node]:
                new_time = time_so_far + weight
                q.append((neighbor, new_time))
        
        if len(best_time) != n:
            return -1
        return max(best_time.values())