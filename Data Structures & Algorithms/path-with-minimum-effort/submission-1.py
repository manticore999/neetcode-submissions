class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions = [[0,1],[0,-1],[-1,0],[1,0]]
        q =[(0,0,0)]
        visited = set()
        while q :
            cost,r,c = heapq.heappop(q)
            if (r,c) in visited:
                continue
            visited.add((r,c))
            if r == len(heights)-1 and c ==len(heights[0])-1 :
                return cost
            for i,j in directions:
                if r+i >=len(heights) or c+j>=len(heights[0]) or r+i< 0 or c+j < 0 or (r+i,c+j) in visited:
                    continue
                a = r+i
                b = c+j
                newcost = max(cost,abs(heights[r][c]-heights[a][b]))
                heapq.heappush(q,(newcost,a,b))
        return 0