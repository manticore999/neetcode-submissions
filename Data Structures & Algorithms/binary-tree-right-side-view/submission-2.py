# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root : 
            return []
        curr = root 
        res = []
        q = [root]
        while q :
            res.append(q[-1].val)
            n = len(q)
            i = 0
            while (i<n):
                node = q.pop(0)
                if node.left :
                    q.append(node.left)
                if node.right : 
                    q.append(node.right)
                i+=1
        return res



        