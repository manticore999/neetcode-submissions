# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
        d = ListNode(0,head)
        prevg = d

        while True :
            kth = self.getknode(prevg,k)
            if not kth : 
                break
            nextgrp = kth.next
            prev, curr = kth.next ,prevg.next 
            
            while curr !=nextgrp: 
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            tmp = prevg.next
            prevg.next = kth
            prevg = tmp
            
        return d.next
    def getknode(self,node,k):
            while node and k>0:
                node = node.next
                k-=1
            return node





        











        