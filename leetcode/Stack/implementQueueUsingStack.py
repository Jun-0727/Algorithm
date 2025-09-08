class MyQue:
    def __init__(self):
        self.stack = []
        self.buffer = []

    def push(self, x):
        while self.stack:
            self.buffer.append(self.stack.pop())
        self.stack.append(x)
        while self.buffer:
            self.stack.append(self.buffer.pop())

    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def empty(self):
        return len(self.stack)
    
que = MyQue()
