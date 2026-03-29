class Solution:
    def findMin(self, nums: List[int]) -> int:
        m = max(nums)
        for i in range(len(nums)):
            if nums[i] == m :
                return nums[(i+1)%len(nums)]

        