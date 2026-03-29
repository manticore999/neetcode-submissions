class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return nums[0]
        
        a,b = 0,0
        for i in range(1,len(nums)):
            temp = max(a+nums[i],b)
            a = b
            b = temp
        
        res = b
        a,b =0,0
        for i in range(len(nums)-1):
            temp = max(a+nums[i],b)
            a = b
            b = temp
        return max(res,b)