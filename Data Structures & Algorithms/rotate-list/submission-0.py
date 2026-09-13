# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head : return head
        tail = head 
        length = 1

        while tail.next: 
            tail = tail.next
            length +=1 
        k = k%length 

        if k == 0 : return head 

        steps = length - k -1
        temp = head
            #finding the first portion
        for i in range(steps):
            temp = temp.next
            #going to the end of the second portion
        new_head = temp.next
        temp.next = None
        tail.next = head
        head = new_head
        return head


        