class Solution:
    def simplifyPath(self, path: str) -> str:
        stck = []
        i = 0
        while i < len(path) : 
            if path[i] == "/" : 
                i+=1
                continue
            j = i+1
            current = path[i]
            while j<len(path) and path[j]!="/" : 
                current+=path[j]
                j+=1
            if current == ".":
                i = j
                continue
            if current == ".." :
                if stck :  
                    stck.pop()
                i = j 
                continue
                
            else : 
                stck.append(current)
                i = j 
        
        return "/" +"/".join(stck)


        