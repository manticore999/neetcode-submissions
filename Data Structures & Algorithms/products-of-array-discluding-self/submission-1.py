class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix ,suffix= [1]*len(nums) , [1]*len(nums)
        #calculate prefix 
        
        prev = nums[0]
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1]*prev
            prev = nums[i]
        
        #calculate suffix 
        prev = nums[-1]
        for j in range(len(nums)-2,-1,-1):
            suffix[j] = suffix[j+1]*prev
            prev = nums[j]

        for i in range(len(nums)):
            nums[i] = prefix[i]*suffix[i]
        
        return nums




