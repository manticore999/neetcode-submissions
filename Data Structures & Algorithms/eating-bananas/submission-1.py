class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h ==len(piles):
            return max(piles)
        u = max(piles)
        l = 1
        res = u
        while (l<=u):
            med = (u+l)//2
            s=0
            for i in piles : 
                s += math.ceil(float(i) /med)
            if (s<=h):
                res = med
                u = med-1
            else : 
                l = med+1
        return res
