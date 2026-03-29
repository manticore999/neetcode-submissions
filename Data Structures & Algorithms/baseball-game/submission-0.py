class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stck = []
        for i in operations:
            if i =='+':
                stck.append(stck[-1]+stck[-2])
            elif i == 'D':
                stck.append(stck[-1]*2)
            elif i == 'C':
                stck.pop()
            else:
                stck.append(int(i))
        
        return sum(stck)
        