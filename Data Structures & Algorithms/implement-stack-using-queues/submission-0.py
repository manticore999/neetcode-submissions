class MyStack:

    def __init__(self):
        self.a = []
        self.b = []

    def push(self, x: int) -> None:
        if not self.a and not self.b:
            self.a.append(x)
        elif self.a :
            self.b.append(x)
            while self.a :
                self.b.append(self.a.pop(0))
        elif self.b :
            self.a.append(x)
            while self.b :
                self.a.append(self.b.pop(0))
        

    def pop(self) -> int:
        if not self.a and not self.b :
            return 
        elif self.a :
            return self.a.pop(0)
        else:
             return self.b.pop(0)

    def top(self) -> int:
        if not self.a and not self.b :
            return 
        elif self.a :
            return self.a[0]
        else:
             return self.b[0]

    def empty(self) -> bool:
        if not self.a and not self.b :
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()