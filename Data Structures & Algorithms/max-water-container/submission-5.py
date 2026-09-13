class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        res = 0
        while (l<r):
            res = max(res, min(heights[r],heights[l])*(r-l) )
            if heights[l]<heights[r] : 
                temp = heights[l]
                l+=1
                while l<r and heights[l]< temp:
                    l+=1
            else : 
                temp = heights[r]
                r-=1
                while l<r and heights[r]< temp:
                    r-=1
        return res