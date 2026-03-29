class Trie:
    def __init__(self):
        self.children = {}
        self.end = False
    def add(self,word):
        cur = self
        for c in word :
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows , cols = len(board), len(board[0])
        t = Trie()
        for w in words : 
            t.add(w)
        visit ,res = set(),set()
        def dfs(r,c,word,node):
            if (r >= rows or c >= cols or
             r<0 or c < 0 or (r,c) in visit or board[r][c] not in node.children):
                return

            word+=board[r][c]
            node = node.children[board[r][c]]
            if node.end :
                res.add(word)
            visit.add((r,c))
            
            dfs(r+1,c,word,node)
            dfs(r-1,c,word,node)
            dfs(r,c+1,word,node)
            dfs(r,c-1,word,node)
            visit.remove((r,c))
        for i in range(rows):
            for j in range(cols):
                dfs(i,j,'',t)
        return list(res)
            






        