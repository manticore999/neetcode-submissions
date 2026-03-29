class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        minh = [(grid[0][0],0,0)]
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        visited = set()
        while minh : 
            cost ,r ,c = heapq.heappop(minh)
            if (r,c) in visited :
                continue
            visited.add((r,c))
            if [r,c] == [rows-1,cols-1]:
                return cost
            for dr,dc in directions :     
                a,b = r+dr,c+dc
                if a<0 or a >= rows or b<0 or b>= cols :
                    continue
                heapq.heappush(minh,(max(cost,grid[a][b]),a,b))

             

            

