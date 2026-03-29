class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = [0,0]
        for b in bills :
            if b == 5:
                change[0]+=1
            elif b == 10:
                if change[0] == 0:
                    return False
                change[0]-=1
                change[1]+=1
            elif b == 20:
                if change[0] == 0:
                    return False
                elif change[1]>0 :
                    change[1]-=1
                    change[0]-=1
                elif change[0]>2:
                    change[0]-=3
                else :
                    return False
        return True