class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[0,1],[0,-1],[-1,0]]
        visited = set()
        rows,cols = len(grid),len(grid[0])
        
        def rot(r,c):
            if r<0 or r >= rows or c<0 or c>= cols or grid[r][c] !=1 or (r,c) in visited: 
                return 0
            if grid[r][c] == 1 : 
                grid[r][c] = 2
                visited.add((r,c))
                return 1
            
        q = deque()
        count = 0 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2 :
                    q.append((r,c))
                    visited.add((r,c))
                if grid[r][c] == 1 :
                    count+=1
        if count == 0 : return 0
        if not q   : return -1
       
        minutes = 0
        rotted = 0
        while q : 
            n = len(q)
            while n>0:
                r,c = q.popleft()
                for a,b in directions :
                    if rot(a+r,c+b) == 1 : 
                        rotted +=1
                        q.append((a+r,c+b))
                n-=1
            minutes+=1
        
        return minutes-1 if rotted == count else -1


