# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        #determine the length of the list 
        length = 0
        cur = head 
        while cur : 
            cur = cur.next
            length+=1
        #use a stack approach , stack the first part of the list and
        # start counting at the other half
        stck = []
        cur = head 
        length = length / 2 
        
        while length > 0 : 
            length-=1
            stck.append(cur.val)
            cur = cur.next
        
        result = 0
        
        while cur :
            twin = stck.pop() 
            result = max(cur.val+twin, result)
            cur = cur.next
        return result 




        