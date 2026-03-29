class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        res = 0
        def inbound(r,c):
            if r>=rows or r< 0 or c>=cols or c<0 :
                return False
            return True
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 :
                    continue
                count = 4
                for i,j in directions :
                    if inbound(r+i,j+c) and grid[r+i][c+j] == 1:
                        count-=1
                res+=count
        return res