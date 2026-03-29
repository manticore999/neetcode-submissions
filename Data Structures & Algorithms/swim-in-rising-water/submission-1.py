class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        q = [(grid[0][0],0,0)]
        res= grid[0][0]
        visited = set()
        while(q):
            cost,r,c = heapq.heappop(q)
            visited.add((r,c))
            res = max(res,cost)
            if r == len(grid)-1 and c == len(grid)-1 :
                return res
            #empty the grid
            if r+1 < len(grid) and (r+1,c) not in visited:
                heapq.heappush(q,(max(cost,grid[r+1][c]),r+1,c))
            if c+1 < len(grid[0]) and (r,c+1) not in visited:
                heapq.heappush(q,(max(cost,grid[r][c+1]),r,c+1))
            if r-1 >=0 and (r-1,c) not in visited:
                heapq.heappush(q,(max(cost,grid[r-1][c]),r-1,c))
            if  c-1>= 0 and (r,c-1) not in visited:
                heapq.heappush(q,(max(cost,grid[r][c-1]),r,c-1))
        

