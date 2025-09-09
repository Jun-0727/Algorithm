class MyCircularQueue:
    def __init__(self, n: int):
        self.n = n
        self.que = [None] * n
        self.front = 0
        self.rear = 0

    def enQueue(self, item):
        if self.que[self.rear] is None:
            self.que[self.rear] = item
            self.rear = (self.rear + 1) % self.n
            return True
        else:
            return False
        
    def deQueue(self):
        if self.que[self.front] is None:
            return False
        else:
            self.que[self.front] = None
            self.front = (self.front + 1) % self.n
            return True
        
    def Front(self):
        return self.que[self.front]
    
    def Rear(self):
        return self.que[(self.rear - 1) % self.n]
    
    def isFull(self):
        return len(self.que) == self.n
    
    def getQue(self):
        return self.que
    
circularQueue = MyCircularQueue(5)
print(circularQueue.enQueue(10))
print(circularQueue.enQueue(20))
print(circularQueue.enQueue(30))
print(circularQueue.enQueue(40))
print(circularQueue.Rear())
print(circularQueue.isFull())
print(circularQueue.deQueue())
print(circularQueue.deQueue())
print(circularQueue.enQueue(50))
print(circularQueue.enQueue(60))
print(circularQueue.Rear())
print(circularQueue.Front())
