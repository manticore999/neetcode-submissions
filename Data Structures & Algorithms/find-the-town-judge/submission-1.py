class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        h = {i:[] for i in range(1,n+1)}
        count = { i:0  for i in range(1,n+1)}
        for t in trust : 
            h[t[0]].append(t[1])
            count[t[1]]+=1
        for i in h:
            if h[i] == [] and count[i] == n-1:
                return i
        return -1