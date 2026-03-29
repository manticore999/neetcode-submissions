class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        current = intervals[0]
        for i in range(1,len(intervals)):
            if intervals[i][0] >= current[1] : 
                current = intervals[i]
                continue
            else : 
                current = [min(intervals[i][0],current[0]),min(intervals[i][1],current[1])]
                res+=1
        return res