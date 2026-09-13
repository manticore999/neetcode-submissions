class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        left = 1
        right = max(piles)
        res = right
        while(left<=right):
            m = (left+right)//2
            hours = 0
            for p in piles : 
                hours+= math.ceil(p/m)
            
            if hours <= h : 
                res = min(res,m)
                right = m-1
            else : 
                left = m+1

        return res
        


