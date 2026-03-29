class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stck = []
        res = []
        for i in asteroids : 
            if i > 0:
                stck.append(i)
            else:
                while stck and stck[-1] <= abs(i):
                    temp = stck.pop()
                    if abs(i) == temp:
                        i = 0
                        break
                if not stck and i!=0:
                    res.append(i)
        return res+stck
