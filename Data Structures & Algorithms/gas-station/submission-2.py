class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1 
        tot = 0
        res = 0
        for i in range(len(gas)):
            if res == -1 :
                res = i 
            tot+=gas[i]-cost[i]
            if tot <0 : 
                res = -1
                tot = 0
        return res





        