class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        d = {}

        for i in range (len(s)):
            if s[i] not in d :
                d[s[i]] = [i,i]
            d[s[i]][1] = i

        minString = d[s[0]][1]
        count = 0
        for i in range(len(s)):
            count+=1
            minString = max(minString, d[s[i]][1])
            if i == minString :
                res.append(count)
                count = 0
        return res



