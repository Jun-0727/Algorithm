from collections import deque

class MyStack:
    def __init__(self):
        self.que = deque()

    def push(self, item):
        self.que.append(item)

        for _ in range(len(self.que) - 1):
            self.que.append(self.que.popleft())


    def pop(self):
        return self.que.popleft()
    
    def top(self):
        return self.que[0]
    
    def empty(self):
        return len(self.que) == 0
    

stack = MyStack()

stack.push(1)
stack.push(2)
print(stack.top())
print(stack.pop())
print(stack.empty())
