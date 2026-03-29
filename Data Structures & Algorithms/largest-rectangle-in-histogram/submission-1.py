class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        s = []
        
        for i,h in enumerate(heights):
            ref = i
            while s and s[-1][1] > h :
                res = max(res,s[-1][1]*(i-s[-1][0]))
                ref = s[-1][0]
                s.pop()
            s.append((ref,h))
        
        for i,h in s:
            res = max(res,h*(len(heights)-i))


        return res