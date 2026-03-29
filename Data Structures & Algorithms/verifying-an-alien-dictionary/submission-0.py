class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        tartib = { c:i for i,c in enumerate(order) }
        for i in range (len(words)-1):
            a = words[i]
            b = words[i+1]
            
            for j in range (len(a)):
                if j == len(b):
                    return False
                if a[j]!=b[j]:
                    if tartib[a[j]]>tartib[b[j]]:
                        return False
                    break
        return True
            