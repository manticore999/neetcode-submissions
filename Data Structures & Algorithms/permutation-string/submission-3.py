class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) >len(s2) : 
            return False
        a,b = [0]*26, [0]*26
        for i in range(len(s1)):
            a[ord(s1[i])-97] += 1
            b[ord(s2[i])-97] +=1
        if a == b :
            return True
        m = 0
        for i in range(26):
            if a[i] == b[i]:
                m+=1

        l = 0
        for r in range(len(s1),len(s2)):
            if m ==26: return True

            i = ord(s2[r])-97
            b[i]+=1
            if b[i]== a[i]:
                m+=1
            elif a[i]+1 == b[i]:
                m-=1
            
            i = ord(s2[l])-97
            b[i]-=1
            if b[i]== a[i]:
                m+=1
            elif a[i]-1 == b[i]:
                m-=1
            l+=1
        return m ==26

            
            
            
            


        