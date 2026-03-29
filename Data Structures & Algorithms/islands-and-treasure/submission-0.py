class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        q = deque()

        def addDistance(r,c):
            if r< 0 or c < 0 or r>= rows or c>=cols or (r,c) in visited or grid[r][c] == -1:
                return 
            visited.add((r,c))
            q.append([r,c])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))
        
        distance = 0
        while q:
            for i in range(len(q)) :
                r,c = q.popleft()
                if grid[r][c] != 0 :    
                    grid[r][c] = distance
                addDistance(r+1,c)
                addDistance(r-1,c)
                addDistance(r,c+1)
                addDistance(r,c-1)
            distance+=1

        