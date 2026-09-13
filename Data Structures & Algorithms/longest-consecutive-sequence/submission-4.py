class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        if len(nums) ==1 : 
            return 1 
        maxi = 0
        for i in nums :
            if i-1 in s :
                continue
            curr= 1
            maxi = max(curr,maxi)
            while i+1 in s:
                curr+=1
                maxi = max(curr,maxi)
                i+=1
        return maxi
