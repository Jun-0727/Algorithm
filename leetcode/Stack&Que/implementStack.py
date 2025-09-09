# LinkedList를 이용한 Stack ADT 구현

class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = Node(item, self.top)
        self.top = new_node

    def pop(self):
        item = self.top.item
        self.top = self.top.next
        
        return item