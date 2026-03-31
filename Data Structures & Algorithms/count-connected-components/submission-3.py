class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def find(n):
            if n!= par[n]:
                return find(par[n])
            return n 
        
        def union(a,b):
            a = find(a)
            b = find(b)

            if a == b:
                return 0
            if rank[a]> rank[b] : 
                par[b] = a
                rank[a]+=rank[b]
                return 1
            else : 
                par[a] = b
                rank[b]+=rank[a]
                return 1
        
        for a,b in edges : 
            n-=union(a,b)
        return n

        