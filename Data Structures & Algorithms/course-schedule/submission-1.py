class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = {i:[] for i in range(numCourses)}
        for c,p in prerequisites:
            adj[c].append(p)
        
        visiting = set()
        def dfs(n):
            nei = adj[n]
            if n in visiting : return False
            visiting.add(n)
            for i in nei :
                t = dfs(i)
                if t ==False :
                    return False
            visiting.remove(n)
            adj[n] = []
            return True 
        
        for i in range(numCourses): 
            if dfs(i) == False :
                return False
        return True





