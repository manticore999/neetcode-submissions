class Solution:
    def compress(self, chars: List[str]) -> int:
        k = i =  0
        
        while (i<len(chars)):
            chars[k]= chars[i]
            k+=1
            j = i+1
            while j<len(chars) and chars[i] ==chars[j]:
                j+=1
            
            if j - i > 1:
                temp = str(j-i)
                for n in temp:
                    chars[k] = n
                    k+=1
            i = j
        return k 



        






            
        