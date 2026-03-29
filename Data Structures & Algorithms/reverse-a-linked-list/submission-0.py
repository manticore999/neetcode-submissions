# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr , temp = None , head , head 
        while temp and temp.next : 
            temp = temp.next 
            curr.next = prev 
            prev = curr 
            curr = temp 
        if curr : curr.next = prev
        return curr

        