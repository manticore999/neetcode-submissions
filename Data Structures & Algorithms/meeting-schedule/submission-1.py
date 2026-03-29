"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key  = lambda interval : interval.start)
        previous = intervals[0] if intervals else None
        for i in range(1,len(intervals)):
            if intervals[i].start < previous.end :
                return False
            previous = intervals[i]
        return True

