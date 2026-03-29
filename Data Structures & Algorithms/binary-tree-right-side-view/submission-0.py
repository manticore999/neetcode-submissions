# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        cur = root
        if not root: return []
        q = [cur]
        res = []
        while q :
            n = len(q)
            while n>= 1 :
                if n == 1 : 
                    res.append(q[0].val)
                if q[0].left : q.append(q[0].left)
                if q[0].right : q.append(q[0].right)
                q.pop(0)
                n-=1 
        return res


        