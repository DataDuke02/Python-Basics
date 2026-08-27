class Solution:
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(int(token))

        return stack[0]


Input:
tokens = ["2", "1", "+", "3", "*"]

Output:
9

2 + 1 = 3
3 × 3 = 9

Input:
tokens = ["4", "13", "5", "/", "+"]

Output:
6

13 / 5 = 2
4 + 2 = 6
