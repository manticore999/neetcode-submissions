class TimeMap:

    def __init__(self):
        self.h = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.h[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if not self.h[key] : 
            return  ""
        values = self.h[key] 
        l,r = 0, len(values)-1
        
        res = ""
        while (l<=r):
            m = (l+r)//2
            if values[m][0] == timestamp : return  values[m][1]
            if values[r][0] == timestamp : return  values[r][1]
            if values[l][0] == timestamp : return  values[l][1]
            
            if values[m][0] < timestamp :
                res = values[m][1]
                l = m+1
            else: 
                r = m-1
        return  res



