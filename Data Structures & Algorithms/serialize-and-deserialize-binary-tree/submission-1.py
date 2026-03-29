# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "n"
        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                res.append("n")
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return ",".join(res)   

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data[0] == "n":
            return None
        data = data.split(",")
        root = TreeNode(int(data[0]))
        q = deque([root])
        index = 1
        while q:
            node = q.popleft()
            if data[index]!="n":
                node.left = TreeNode(int(data[index]))
                q.append(node.left)
            index+=1
            if data[index]!="n":
                node.right = TreeNode(int(data[index]))
                q.append(node.right)
            index+=1
        return root

