class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n : return True
        neigh = { i:[] for i in range(n) } 
        for i,j in edges:
            neigh[i].append(j)
            neigh[j].append(i)
        
        visit = set()
        def dfs(i,prev):     
            if i in visit:
                return False
            visit.add(i)
            for j in neigh[i]:
                if j == prev:
                    continue
                if not dfs(j,i):
                    return False
            return True
        
        return dfs(0,-1) and  len(visit) == n
