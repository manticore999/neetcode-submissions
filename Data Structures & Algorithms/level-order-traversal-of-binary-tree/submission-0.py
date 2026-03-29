# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root : return [] 
        q = [root]
        while q :
            level = []
            n = len(q)
            while n>0 : 
                cur = q[0]
                if cur.left :
                    q.append(cur.left)
                if cur.right :
                    q.append(cur.right)
                level.append(cur.val)
                q.pop(0)
                n-=1
            res.append(level)
        return res 
            


         
        