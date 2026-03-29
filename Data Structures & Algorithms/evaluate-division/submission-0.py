class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i,eq in enumerate(equations):
            adj[eq[0]].append([eq[1],values[i]])
            adj[eq[1]].append([eq[0], 1 / values[i]])
        
        def bfs(src,target):
            if src not in adj or target not in adj :
                return -1
            if src == target :
                return 1.0
            
            res = 0
            q = deque([[src,1]])
            visited  = set()
            while q : 
                s, val = q.pop()
                visited.add(s)
                for t in adj[s]:
                    if t[0] in visited:
                        continue
                    if t[0] ==target :
                        return val*t[1]
                    q.append([t[0],val*t[1]])
            return -1

        return [bfs(q[0],q[1]) for q in queries ]


