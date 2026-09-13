class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0 
        curr = prices[-1]
        for i in range(len(prices)-1,-1,-1): 
            maxi = max(maxi,curr-prices[i])
            curr = max(curr,prices[i])
        return maxi 
