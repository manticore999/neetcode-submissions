class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid),len(grid[0])
        visited = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        def dfs(row,col):
            if row >= rows or row <0 or col < 0 or col >= cols or (row,col) in visited or grid[row][col] == 0:
                return 0
            area = 0
            visited.add((row,col))
            for a,b in directions :
                area += dfs(row+a,col+b)
            return 1+ area

        res = 0    
        for r in range(rows) :
            for c in range(cols):
                res = max(res,dfs(r,c))
        return res

