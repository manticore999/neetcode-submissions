class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            cur = strs[0][i]
            for s in range(len(strs)):
                if  i ==len(strs[s]) or strs[s][i]!=cur :
                    return res
            res+=cur
        return res