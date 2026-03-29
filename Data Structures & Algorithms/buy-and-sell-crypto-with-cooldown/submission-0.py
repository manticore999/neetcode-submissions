class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i,buy):
            if i>=len(prices):
                return 0
            if (i,buy) in dp:
                return dp[(i,buy)]
            if buy : 
                profit = dfs(i+1,not buy) -prices[i]
                cooldown = dfs(i+1,buy)
                dp[(i,buy)] = max(profit,cooldown)
            else :
                sell = dfs(i+2,not buy)+prices[i]
                cooldown = dfs(i+1,buy)
                dp[(i,buy)] = max(sell,cooldown)
            return dp[(i,buy)]
        return dfs(0,True)

