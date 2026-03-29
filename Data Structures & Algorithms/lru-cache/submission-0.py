class Node:
    def __init__(self, key,val):
        self.key,self.val = key,val
        self.prev = self.next = None
    


class LRUCache:

    def __init__(self, capacity: int):
        self.c = capacity
        self.cache = {}
        self.l , self.r = Node(0,0), Node(0,0)
        self.l.next = self.r
        self.r.prev = self.l
    
    def insert(self,node):
        node.prev = self.r.prev 
        node.next = self.r
        self.r.prev.next = node
        self.r.prev = node
    
    def remove(self,node):
        node.prev.next = node.next 
        node.next.prev = node.prev


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        else:
            self.cache[key] = Node(key,value)
            self.insert(self.cache[key])
        if self.c < len(self.cache):
            lru = self.l.next
            self.remove(lru)
            del self.cache[lru.key]




        
