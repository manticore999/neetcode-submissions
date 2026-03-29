from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ref = Counter(t)
        c = Counter()
        l = 0
        lres, rres = 0,0
        haves = 0
        mini = float("inf")
        for r in range(len(s)):
            if ref[s[r]] > 0:
                c[s[r]]+=1
                if c[s[r]] == ref[s[r]]:
                    haves+=1

            while (haves == len(ref.keys())):
                if r-l+1 <mini :
                    lres, rres = l,r
                    mini = r-l+1
                if c[s[l]] > 0 :
                    c[s[l]]-=1
                    if c[s[l]] < ref[s[l]]:
                        haves-=1
                l+=1
        return s[lres:rres+1] if mini <float("inf") else ""


        