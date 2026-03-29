class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        current = nums[0]
        for i in nums:
            if i == current :
                count+=1
            if i != current :
                if count == 0:
                    current = i
                    count = 1
                else:
                    count-=1
        
            
        return current   