# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root : return 0
        t = [0] # [maximum until that node , result]
        def dfs(root,maxi):
            if not root : return
            if root.val >= maxi: 
                t[0]+=1
                maxi = root.val
            dfs(root.left,maxi)
            dfs(root.right,maxi)
        dfs(root,root.val)
        return t[0]
