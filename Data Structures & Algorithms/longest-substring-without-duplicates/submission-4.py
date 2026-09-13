class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        temp = set()
        result = 0
        for r in range(len(s)) : 
            while s[r] in temp :
                temp.remove(s[l])
                l+=1
            temp.add(s[r])
            result = max(result,r-l+1)
        
        return result

