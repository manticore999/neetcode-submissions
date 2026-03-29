class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        q = []
        output = [0]*len(temperatures)
        for j,t in enumerate(temperatures) : 
            while q and q[-1][0] <t :
                c,i = q.pop()
                output[i] = j-i
            q.append([t,j])
        return output