class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = {i: [] for i in range(numCourses)}
        for a,b in prerequisites:
            pre[a].append(b)
        visited ,cycle= set(),set()
        res = []

        def dfs(i):
            if i in cycle :
                return False
            if i in visited :
                return True
            cycle.add(i)
            for j in pre[i]:
                if dfs(j) == False :
                    return False
            cycle.remove(i)
            visited.add(i)
            res.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
    
        return res
            




