class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cmag= Counter(magazine)
        cransom = Counter(ransomNote)
        for i in cransom :
            if i not in cmag or cmag[i]<cransom[i]:
                return False
        return True 

        