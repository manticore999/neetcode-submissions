class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        if "0000" in deadends:
            return -1
        
        
        def children(lock):
            children = []
            for i in range(4):
                d = str((int(lock[i])+1)%10)
                children.append( lock[:i]+d+lock[i+1:] )
                d = str((int(lock[i])+9)%10)
                children.append( lock[:i]+d+lock[i+1:] )
            return children
        
        #test a special case 
        dead = children(target)
        if dead in deadends:
            return -1
        
        
        q = deque()
        visit = set(deadends)
        q.append(["0000",0])
        while q:
            l,t = q.popleft()
            if l == target :
                return t
            child = children(l)
            for c in child:
                if c not in visit:
                    visit.add(c)
                    q.append([c,t+1])
        return -1
            
