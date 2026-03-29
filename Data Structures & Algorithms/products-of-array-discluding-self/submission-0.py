class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        s= 1
        p = 1
        for i in range(len(nums)):
            prefix[i] = p
            p = p*nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            suffix[i] = s
            s = s*nums[i]
        for j in range(len(nums)):
            prefix[j] = prefix[j]*suffix[j]
        return prefix

            



        