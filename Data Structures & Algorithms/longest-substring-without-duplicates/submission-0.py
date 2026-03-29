class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        se = set()
        l = 0
        m = 0
        for r in range(len(s)):
            while s[r] in se : 
                se.remove(s[l])
                l+=1
            se.add(s[r])
            m = max(m,len(se))
        return m


        


