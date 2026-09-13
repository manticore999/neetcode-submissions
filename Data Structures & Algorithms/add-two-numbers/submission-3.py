# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = ListNode()
        a,b = l1,l2
        
        while a and b : 
            preva,prevb = a,b
            a.val += b.val+ carry.val
            if a.val > 9 : 
                a.val = a.val % 10
                carry.val = 1
            else : 
                carry.val = 0
            a = a.next 
            b = b.next 
        
        a,b = preva,prevb

        if b.next :
            a.next = b.next 
        if a.next :
            a = a.next 
            while a and a.next and carry.val == 1 : 
                a.val+=1
                if a.val > 9: 
                    a.val = a.val % 10
                    carry.val = 1
                    a = a.next
                else : carry.val = 0
        
            if carry.val == 1 :
                a.val+=1
                if a.val > 9: 
                    a.val = a.val % 10
                    a.next = ListNode(1)
        elif carry.val == 1 : 
            a.next = carry 
        return l1




        







