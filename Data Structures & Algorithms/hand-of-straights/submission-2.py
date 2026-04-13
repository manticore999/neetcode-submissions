class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0 : 
            return False
        hand.sort()
        count = Counter(hand)
        for i in hand : 
            if count[i] == 0 : 
                continue
            j = i
            k = 0
            while count[j]>0 and k < groupSize:
                count[j]-=1
                j+=1
                k+=1 
        return k == groupSize

            
            
            




