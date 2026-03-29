class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a = [0]*len(nums)
        for i in nums :
            if a[i-1] >0 : 
                return i
            a[i-1]+=1
         

        