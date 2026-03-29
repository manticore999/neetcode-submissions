class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i ,t in enumerate(tasks):
            t.append(i)
        tasks.sort()
        minh = []
        t = 1
        res = []
        n = len(tasks)
        while len(res)<n:
            while tasks and tasks[0][0] <= t:
                temp = tasks.pop(0)
                heapq.heappush(minh, [temp[1],temp[2]])
            if not minh:
                t+=1
                continue
            current = heapq.heappop(minh)
            res.append(current[1])
            t+=current[0]
        return res




