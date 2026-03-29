class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = [0,0,0]
        for i in nums:
            temp[i]+=1
        index = 0
        for i in range(3):
            while temp[i]>0 :
                nums[index] = i
                temp[i]-=1
                index+=1
                
        


        