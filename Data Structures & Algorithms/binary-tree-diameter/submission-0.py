# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dlen(root):
            nonlocal res
            if not root :
                return 0
            maxl = dlen(root.left)
            maxr = dlen(root.right)
            res = max(res,maxl+maxr)
            return 1+ max(maxl,maxr)
        dlen(root)
        return res
        
            
            
        
        

        