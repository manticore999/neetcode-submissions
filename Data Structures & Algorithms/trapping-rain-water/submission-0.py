class Solution:
    def trap(self, height: List[int]) -> int:
        maxl = height[0]
        maxr = height[-1]
        l,r = 0, len(height)-1
        res= 0
        while (l<r):
            if maxl > maxr : 
                r = r-1
                maxr = max(maxr,height[r]) 
                res += abs(maxr-height[r])
            elif maxl < maxr :
                
                l = l+1
                maxl = max(maxl,height[l])
                res += abs(maxl-height[l])
            else : 
                r = r-1
                maxr = max(maxr,height[r]) 
                res += abs(maxr-height[r])
        return res 






        