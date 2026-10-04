class Solution:
    def sol(self, a,b,i):
        if i == '+':
            return a+b
        elif i == '-':
            return a-b
        elif i == '*':
            return a * b
        elif i == '/':
            return int(a/b)
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', "/"]
        for i in tokens:
            if i in operators:
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(self.sol (b,a,i))
            else:
                stack.append(int(i))
                print(i)
        print(len(stack),stack[0])
        return stack[0]
        