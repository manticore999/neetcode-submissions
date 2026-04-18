class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        h = defaultdict(int)
        for i in range(len(s)) : 
            h[s[i]] = i
        res = []
        end = 0
        size = 0
        for i in range(len(s)):
            size+=1
            end = max(end,h[s[i]])
            if end == i : 
                res.append(size)
                size = 0
        return res


             
