class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList) or (beginWord == endWord):
            return 0

        wordList.append(beginWord)
        
        h = {}
        for word in wordList:
            for i in range(len(word)):
                subword = word[:i] +"*"+word[i+1:]
                if subword not in h :
                    h[subword] = []
                h[subword].append(word)
        
        visited = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q: 
            for i in range(len(q)):
                curr = q.popleft()
                if curr == endWord:
                    return res
                for i in range(len(curr)):
                    pattern = curr[:i]+"*"+curr[i+1:]
                    for word in h[pattern]:
                        if word not in visited:
                            visited.add(word)
                            q.append(word)
                            
            res+=1
        return 0

            


        
