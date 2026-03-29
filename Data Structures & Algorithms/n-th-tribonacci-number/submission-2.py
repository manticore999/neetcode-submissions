class Solution:
    def tribonacci(self, n: int) -> int:
        a,b,c = 0,1,1
        res = 0
        if n == 0:
            return 0
        if n ==1 or n ==2 :
            return 1
        
        for i in range(3,n+1):
            res = a+b+c
            temp = c
            c = res
            temp,b = b,temp
            a = temp
        return res

