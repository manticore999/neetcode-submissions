class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if target in triplets :
            return True
        test = [False,False,False] 
        for i in triplets :
            if i[0] == target[0]:
                test[0] = True
            if i[1] == target[1]:
                test[1] = True
            if i[2] == target[2]:
                test[2] = True
        if not test[1] or not test[2] or not test[0]:
            return False

        current = []
        for i in triplets :
            if i[0] > target[0] or i[1] > target[1] or i[2] > target[2]:
                continue 
            if i[0]== target[0] or i[1]== target[1] or i[2]== target[2]:
                if not current : 
                    current = i
                current = [max(i[0],current[0]),max(i[1],current[1]),max(i[2],current[2])]
        return current == target






