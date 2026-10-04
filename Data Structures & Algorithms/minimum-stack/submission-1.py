class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min:
            self.min.append(val)
        else:
            self.min.append(min(val,self.min[len(self.min)-1]))
        

    def pop(self) -> None:
        # print(self.stack, self.min)
        self.stack.pop(len(self.stack)-1)
        self.min.pop(len(self.min)-1)
        # print(self.stack, self.min)?

    def top(self) -> int:
        return self.stack[len(self.stack)-1]
        

    def getMin(self) -> int:
        return self.min[len(self.min)-1]


        
