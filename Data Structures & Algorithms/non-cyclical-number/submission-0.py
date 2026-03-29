class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n!=1 and n not in s:
            s.add(n) 
            so =0
            while n>0:
                so+= (n%10)**2
                n = n//10
            n = so
        return n==1 