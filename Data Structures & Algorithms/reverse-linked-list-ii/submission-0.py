# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head : return 
        if left == right : return head

        #we need to isolate the portion we're going to 
        dummy = ListNode()
        dummy.next = head
        lp,curr = dummy,head

        for i in range(left-1) : 
            lp,curr = curr,curr.next
        
        p =None
        
        for i in range(right-left+1) : 
            temp = curr.next 
            curr.next = p
            p = curr
            curr = temp 
        
        lp.next.next = curr
        lp.next = p
        return dummy.next 
        
