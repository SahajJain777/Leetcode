class MinStack(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, value):
        self.stack1.append(value)

        if len(self.stack2) == 0 or value <= self.stack2[-1]:
            self.stack2.append(value)

    def pop(self):
        if len(self.stack1) == 0:
            return None

        element = self.stack1.pop()

        if element == self.stack2[-1]:
            self.stack2.pop()

        return element

    def top(self):
        if len(self.stack1) == 0:
            return None

        return self.stack1[-1]

    def getMin(self):
        if len(self.stack2) == 0:
            return None

        return self.stack2[-1]