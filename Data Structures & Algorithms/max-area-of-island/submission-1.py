class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        res = 0
        rows,cols = len(grid),len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>= cols or (r,c) in visited or grid[r][c] == 0:
                return 0
            visited.add((r,c))
            s = 1
            for a,b in directions:
                s+= dfs(r+a,c+b)
            return s
        for r in range(rows):
            for c in range(cols):
                res = max(res,dfs(r,c))
        return res
