class Node:
    def __init__(self,key=0,val=0,prev=None,next=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.key = key

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.h = dict()
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self,node) : 
        nxt = self.left.next
        node.prev, node.next = self.left, nxt
        self.left.next = node
        nxt.prev = node 
    
    def remove(self,node):
        node.next.prev ,node.prev.next = node.prev , node.next 

    def get(self, key: int) -> int:
        if key not in self.h :
            return -1
        node = self.h[key]
        self.remove(node)
        self.insert(node) 
        return node.val
    
    def put(self, key: int, value: int) -> None:
        if key in self.h : 
            node = self.h[key]
            node.val = value
            self.remove(node)
            self.insert(node)
            return 
         
        new = Node(key=key,val=value)
        self.insert(new)
        self.h[key] = new
        if self.capacity < len(self.h) :
            lru = self.right.prev
            self.remove(lru)
            del self.h[lru.key]
        return 
        

       
            




        
