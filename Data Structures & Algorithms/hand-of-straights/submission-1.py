class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        count = Counter(hand)
        for i in hand:
            if count[i]:
                for first in range(i,i+groupSize):
                    if first not in count or not count[first]:
                        return False
                    count[first]-=1
        return True 
            
            




