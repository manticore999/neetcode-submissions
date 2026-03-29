"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        h = {}

        def dfs(node):
            if not node : 
                return 
            clone = Node(node.val,[])
            h[node] = clone 
            for n in node.neighbors :
                if n not in h:
                    dfs(n)
                clone.neighbors.append(h[n])
            return clone 

        if not node :
            return 
        clone = dfs(node)
        return clone



