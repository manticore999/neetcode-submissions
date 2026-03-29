class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)}
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()
       

        def dfs(i,prev):
            nei = adj[i]
            visited.add(i)
            
            for a in nei :
                if a ==prev : 
                    continue
                if a in visited :
                    return False
                if not dfs(a,i) :
                    return False
            return True


        if dfs(0,-1) == False : return False
        return len(visited) == n

