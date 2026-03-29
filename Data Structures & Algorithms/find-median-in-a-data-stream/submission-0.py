class MedianFinder:

    def __init__(self):
        self.minh = []
        self.maxh = []

    def addNum(self, num: int) -> None:
        if self.minh and num > self.minh[0] : 
            heapq.heappush(self.minh,num)
        else :
            heapq.heappush_max(self.maxh,num)
        if len(self.minh) > len(self.maxh)+1 :
            heapq.heappush_max(self.maxh,heapq.heappop(self.minh))
        if len(self.maxh) > len(self.minh)+1 : 
            heapq.heappush(self.minh,heapq.heappop_max(self.maxh))
        
    def findMedian(self) -> float:
        if len(self.minh) > len(self.maxh) :
            return self.minh[0]
        elif len(self.minh) < len(self.maxh):
            return self.maxh[0]
        return (self.maxh[0]+self.minh[0])/2.0 
        
        
        