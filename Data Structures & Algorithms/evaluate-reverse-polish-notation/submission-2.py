class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens : 
            if i in ["+","-","*","/"] and s:
                x = s.pop()
                y = s.pop()
                if i =="+":
                    s.append(x+y)
                if i =="-":
                    s.append(y-x)
                if i =="/":
                    s.append(int(float(y)/x))
                if i =="*":
                    s.append(x*y)
            else :
                s.append(int(i))
        return s[-1]
                

        