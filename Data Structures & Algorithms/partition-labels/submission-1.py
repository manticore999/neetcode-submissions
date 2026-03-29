class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        d = {}

        for i in range (len(s)):
            if s[i] not in d :
                d[s[i]] = i
            d[s[i]] = i

        minString = d[s[0]]
        count = 0
        for i in range(len(s)):
            count+=1
            minString = max(minString, d[s[i]])
            if i == minString :
                res.append(count)
                count = 0
        return res



