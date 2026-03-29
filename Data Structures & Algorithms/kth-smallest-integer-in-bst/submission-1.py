# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        glob = [k]
        def dfs(node):
            if not node : return 
            dfs(node.left)
            
            if glob[0] == 1: 
                glob.append(node.val)
                return
            glob[0]-=1
            dfs(node.right)
        dfs(root)
        return glob[1]
