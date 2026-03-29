# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        n = 0
        def helper(node,cur_max):
            nonlocal n
            if not node : return
            if node.val >= cur_max :
                n+=1
            
            helper(node.left,max(node.val,cur_max))
            helper(node.right,max(node.val,cur_max))
        helper(root,float("-inf"))
        return n 



        