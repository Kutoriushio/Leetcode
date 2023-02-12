class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                add = num1 + num2
                stack.append(add)
            elif token == '-':
                num1 = stack.pop()
                num2 = stack.pop()
                minus = num2 - num1
                stack.append(minus)
            elif token == '*':
                num1 = stack.pop()
                num2 = stack.pop()
                mul = num1 * num2
                stack.append(mul)
            elif token == '/':
                num1 = stack.pop()
                num2 = stack.pop()
                divide = int(num2 / num1)
                stack.append(divide)
            else:
                stack.append(int(token))

        return stack.pop()