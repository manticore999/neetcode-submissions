class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        mini,maxi=0,0
        maxig,minig = nums[0],nums[0]
        total = 0
        for i in nums:
            total+=i
            maxi = max(i,maxi+i)
            maxig = max(maxig,maxi)
            mini = min(i,mini+i)
            minig = min(mini,minig)
        return max(maxig,total-minig) if maxig > 0 else maxig
