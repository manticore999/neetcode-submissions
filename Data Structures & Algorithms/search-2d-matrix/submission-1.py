class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for t in matrix : 
            l = 0
            r = len(t)-1
            if t[l] == target or t[r] == target : 
                return True
            if target < t[l] or (target > t[r] and t == matrix[-1]) :
                return False
            elif  target > t[r]:
                continue
            else :
                while (l<=r):
                    m = (l+r) // 2
                    if t[m] == target :
                        return True
                    elif t[m] < target : 
                        l = m+1 
                    else : 
                        r = m-1
                return False 
        
                



        