class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        b= prices[0]
        for i in range(1,len(prices)):
            p = max(p,prices[i]-b)
            b = min(b,prices[i])
        return max(0,p)




        