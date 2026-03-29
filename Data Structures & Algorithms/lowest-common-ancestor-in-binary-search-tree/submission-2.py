# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root 
        mini = min(p.val,q.val)
        maxi = max(p.val,q.val)

        while curr : 
            if curr.val < mini:
                curr = curr.right
            elif curr.val>maxi : 
                curr = curr.left 
            else:
                return curr
             