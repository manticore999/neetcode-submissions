# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge(self,a,b):
        n = d = ListNode()
        while a and b : 
            if a.val < b.val :
                n.next = a
                a = a.next
                n = n.next 
            else :
                n.next = b
                b = b.next
                n = n.next
        n.next = a or b
        return d.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k == 0: return None
        if k == 1 : return lists[0]
        for i in range(1,k):
            lists[i] = self.merge(lists[i],lists[i-1])
        return lists[-1]

        





        