class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        curr = 0
        for i in nums :
            if curr < 0:
                curr = 0
            curr+=i
            maxi = max(curr,maxi)
        return maxi

