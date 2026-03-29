class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        par = [i for i in range(n)]   
        rank = [1 for i in range(n)]

        def find(n):
            if n!=par[n]:
                return find(par[n])
            return n
        
        def union(n1,n2):
            a,b = find(n1),find(n2)
            if a == b:
                return 0
            if rank[a]>rank[b]:
                par[b] = par[a]
                rank[a]+=rank[b]
                return 1
            else:
                par[a] = par[b]
                rank[b]+=rank[a]
                return 1
        for a,b in edges:
            n-= union(a,b)
        return n
                        
