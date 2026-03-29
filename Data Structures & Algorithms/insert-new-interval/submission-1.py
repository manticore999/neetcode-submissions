class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new = newInterval
        res = []
        for i in range(len(intervals)) :
            if intervals[i][0] > new[1]:
                res.append(new)
                return res +intervals[i:]
            if intervals[i][1]< new[0]:
                res.append(intervals[i])
            else : 
                new = [min(new[0],intervals[i][0]),max(new[1],intervals[i][1])]
        res.append(new)
        return res


        