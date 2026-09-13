class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        while(l<r) : 
            m = (l+r)//2
            if m ==l or m == r : 
                if nums[l]<nums[r]:
                    return nums[l]
                return nums[r]
            if nums[m]<nums[r] :
                r = m
            else : 
                l = m
        return nums[r] 
                

            



        

        



