class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        h = defaultdict(list)
        for ticket in tickets:
            h[ticket[0]].append(ticket[1])
        for tab in h: 
            h[tab].sort()
        res = ["JFK"]
        def dfs(string):
            nonlocal res
            if len(res) == len(tickets)+1:
                return True
            
            temp = h[string]
            for i,v in enumerate(temp):
                h[string].pop(i)
                res.append(v)
                if dfs(v): return True
                h[string].insert(i,v)
                res.pop()
            return False
        dfs("JFK")
        return res