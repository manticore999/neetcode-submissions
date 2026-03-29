"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [intervals[i].start for i in range(len(intervals)) ]
        end = [intervals[i].end for i in range(len(intervals)) ]
        start.sort()
        end.sort()

        l,r = 0,0
        cur = 0
        days = 0
        while r<len(intervals) and l < len(intervals):
            if start[r] < end[l]:
                r+=1
                cur+=1
                days = max(days,cur)
            else : 
                cur-=1
                l+=1
        return days
            


