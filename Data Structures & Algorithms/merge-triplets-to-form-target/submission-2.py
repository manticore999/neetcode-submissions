class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a,b,c = False, False, False
        for i,j,k in triplets : 
            if i> target[0] or j> target[1] or k>target[2] : 
                continue
            if i == target[0] : a = True
            if j == target[1] : b = True
            if k == target[2] : c = True
        return a and b and c



