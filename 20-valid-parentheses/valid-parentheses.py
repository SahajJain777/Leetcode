class Solution(object):
    def isValid(self, s):

        stack = []

        # CHANGED: removed "last = len(stack) - 1"
        # because the top of the stack changes as we push/pop

        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)

            if c == ')':

                # CHANGED: check if stack is empty first
                if len(stack) == 0:
                    return False

                # CHANGED: use stack[-1] instead of stack[last]
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False

            elif c == '}':

                # CHANGED: check if stack is empty first
                if len(stack) == 0:
                    return False

                # CHANGED: use stack[-1]
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False

            elif c == ']':

                # CHANGED: check if stack is empty first
                if len(stack) == 0:
                    return False

                # CHANGED: use stack[-1]
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False