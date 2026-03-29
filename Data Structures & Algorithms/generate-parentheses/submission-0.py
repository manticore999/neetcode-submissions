class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(nleft,nright,sub):
            if nleft == 0 and nright ==0:
                res.append(sub)
            
            if nleft > 0 :
                dfs(nleft-1,nright,sub+"(")
        
            if nleft < nright :
                dfs(nleft,nright-1,sub+")")
        dfs(n,n,"")
        return res
        