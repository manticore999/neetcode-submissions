# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not  root : return []
        queue = [root]
        result = []
        n = len(queue)
        while len(queue) > 0 : 
            node = queue.pop(0)
            n-=1
            if node.left : 
                queue.append(node.left)
            if node.right : 
                queue.append(node.right)
            if n == 0 :
                result.append(node.val)
                n = len(queue)
        return result



        