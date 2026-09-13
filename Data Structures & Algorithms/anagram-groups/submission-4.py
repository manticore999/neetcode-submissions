class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        htable = defaultdict(list)
        for s in strs :
            count = [0]*26
            for c in s :
                    count[ord(c)-ord("a")]+=1
            
            htable[tuple(count)].append(s)
        
        return list (htable.values())

        