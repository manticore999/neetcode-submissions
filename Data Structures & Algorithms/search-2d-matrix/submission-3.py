class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix : return False
        

        for row in matrix : 
            if target > row[-1]:
                continue
            if target < row[0] : return False

            left = 0
            right = len(row)-1
            if target == row[left] or target == row[right] :
                return True 
            while (left<right) : 
                m = (left+right)//2
                val = row[m]
                if target in [row[m],row[left],row[right]] : 
                    return True
                if target > val :
                    left = m+1
                else:
                    right = m-1
        return False
        
                



        