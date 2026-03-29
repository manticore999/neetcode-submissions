class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        hand = list(count.keys())
        heapq.heapify(hand)
        while hand :
            first = hand[0]
            for i in range(first,first+groupSize):
                if i not in count  :
                    return False
                count[i]-=1
                if count[i]==0:
                    if i!=hand[0]:
                        return False
                    heapq.heappop(hand)
        return True
            
            




