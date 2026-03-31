class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0 
        res = nums[0]
        for i in range(len(nums)):
            s+= nums[i]
            res = max(res,s)
            if s< 0:
                s = 0
        return res