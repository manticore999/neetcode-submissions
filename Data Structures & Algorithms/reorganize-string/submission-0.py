class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = defaultdict(int)
        for c in s:
            counter[c]+=1
        maxh = [[counter[c],c] for c in counter ]
        heapq.heapify_max(maxh)
        res = ""
        while maxh:
            a ,a_char= heapq.heappop_max(maxh)
            if a==1: 
                if res and res[len(res)-1] == a_char:  return ""
                res+=a_char
                continue
            if a>1 and not maxh: return ''
            b,b_char = heapq.heappop_max(maxh)
            if res and res[-1] == a_char : return ''
            res+=a_char
            heapq.heappush_max(maxh,[a-1,a_char])
            res+=b_char
            if b-1 > 0:
                heapq.heappush_max(maxh,[b-1,b_char])
        return res
