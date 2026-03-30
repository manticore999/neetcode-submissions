class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # the graph approach is easy to spot, the key thing here is to remember how  to build the adj list
        if endWord not in wordList : return 0
        
        adj = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList: 
            for c in range(len(word)): 
                pattern = word[:c]+"$" +word[c+1:]
                adj[pattern].append(word)
        
        visited = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q : 
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord : 
                    return res
                for c in range(len(word)): 
                    pattern = word[:c]+"$" +word[c+1:]
                    for nei in adj[pattern]:
                        if nei not in visited : 
                            q.append(nei) 
                            visited.add(nei)  
            res+=1
        return 0 



        