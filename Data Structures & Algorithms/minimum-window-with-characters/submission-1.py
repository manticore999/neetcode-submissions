from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ref = Counter(t)
        current = Counter()
        l= 0
        res = ""
        mini = float("inf")
        for r in range(len(s)):
            current[s[r]]+=1
            while current >= ref :
                if r-l+1 < mini :
                    res = s[l:r+1]
                    mini = r-l+1
                current[s[l]]-=1
                l+=1
        return  str(res)


        