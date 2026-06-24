class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        token = []
        for i in tokens:
            if i not in ('+', '-', '*', '/'):
                token.append(int(i))
            else:
                a = token.pop()
                b = token.pop()
                if i == '+':
                    result = a + b
                elif i == '-':
                    result = b - a
                elif i == '*':
                    result = a * b
                else:
                    result = int((b) / a)
                token.append(result)
        return token[0]