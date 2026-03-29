# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #split the linked list first 
        s,f = head,head.next
        while f and f.next:
            f = f.next.next
            s = s.next
        #reverse the second list 
        temp = s
        p = None
        while s:
            temp = temp.next
            s.next = p
            p = s
            s = temp
        #merge the two linked lists p and head
        s = p
        a,b ,c, d= head,head,s,s
        while a and d : 
            a = a.next
            b.next = c
            d = d.next
            c.next = a
            b = a
            c = d
        




        



        