class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        current = intervals[0]
        for i in range(1,len(intervals)):
            if intervals[i][0] > current[1] : 
                res.append(current)
                current = intervals[i]
            else : 
                current = [min(current[0],intervals[i][0]),max(current[1],intervals[i][1])]
        res.append(current)
        return res
