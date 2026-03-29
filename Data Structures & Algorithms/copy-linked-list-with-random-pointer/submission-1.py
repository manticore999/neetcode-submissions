"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #begin by doing a normal copy
        if not head :
            return None
        copy = Node(head.val,None,None)
        d = copy
        i = head.next
        h = {}
        h[head] = copy
        while i :
            temp = Node(i.val,None,None)
            h[i] = temp
            d.next = temp 
            d = temp
            i = i.next
        
        a,b = head , copy
        while a and b:
            if a.random != None:
                b.random = h[a.random]
            a = a.next 
            b = b.next
            
        return copy
        
        