class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        def freq(s):
            a = [0]*26
            for i in s:
                a[ord(i)-97]+=1
            return a

        a = freq(s1)
        b = freq(s2)
        
        l,r = 0, len(s1)       
        while(l<len(s2)-r+1):
            if a == freq(s2[l:l+r]):
                return True
            l+=1
        return False 



        