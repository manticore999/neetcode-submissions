class Node:
    def __init__(self,val=0,n=None,pre=None):
        self.val = val
        self.n = n
        self.pre = pre

class MyHashSet:

    def __init__(self):
        self.root = Node()
        self.end = None
    
    def add(self, key: int) -> None:
        if self.contains(key):
            return
        node = Node(val=key)
        if self.end :
            self.end.n = node
            node.pre = self.end
            self.end = node
        else:
            self.root.n = node
            node.pre = self.root
            self.end = node 
        

    def remove(self, key: int) -> None:
        curr = self.root.n
        while curr :
            if curr.val == key:
                curr.pre.n = curr.n
                if curr == self.end :
                    self.end = self.end.pre
                if curr.n :
                    curr.n.pre = curr.pre
                break
            curr = curr.n
        

    def contains(self, key: int) -> bool:
        curr = self.root.n
        while curr:
            if curr.val == key :
                return True
            curr = curr.n
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)