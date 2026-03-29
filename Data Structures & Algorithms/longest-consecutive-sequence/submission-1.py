class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        m= 0
        for i in s :
            if i-1 not in s :
                l= 1
                while (i+l) in s :
                    l+=1
                m = max(m,l)
        return m



        