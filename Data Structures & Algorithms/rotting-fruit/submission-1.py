class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        rows , cols = len(grid), len(grid[0])
        q = deque()
        
        def rot(r,c):
            if r< 0 or c<0 or r>=rows or c>=cols or (r,c) in visited or grid[r][c]!=1 :
                return
            visited.add((r,c))
            q.append((r,c))


        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2 : 
                    q.append((r,c))
                    visited.add((r,c))
                    count+=1
                if grid[r][c] == 1:
                    count+=1

        rottenCount = len(q)
        if count == rottenCount :
            return 0

        minute = 0
        while q :
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c]= 2
                rot(r+1,c)
                rot(r-1,c)
                rot(r,c+1)
                rot(r,c-1)
            minute+=1
            rottenCount+=len(q)
        
        if rottenCount == count :
            return minute-1
        return -1
        




