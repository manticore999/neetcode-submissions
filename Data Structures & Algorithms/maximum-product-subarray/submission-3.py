class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        mini,maxi = 1,1
        
        for i in nums:
            if i == 0 :
                mini,maxi = 1,1
                continue
            temp = mini*i
            mini = min(mini*i,maxi*i,i)
            maxi = max(temp,maxi*i,i)
            res = max(res,maxi)
        return res
            