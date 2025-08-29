with open("input.txt", "r") as f:
    lines = f.read().splitlines()

input = lines[0]

class LinkedList:
    def __init__(self, val: int = 0, next: "LinkedList" = None):
        self.val: int = val
        self.next: LinkedList = next

def is_palindrome(head: LinkedList) -> bool:
    values = []
     
    while head:
        values.append(head.val)

        head = head.next

    if values == values[::-1]:
        return True
    else:
        return False
    
# 연결 리스트 초기화
nodes = list(map(int, input.split('->')))
start_node = LinkedList(nodes[0], None)
prev_node = start_node
for node in nodes[1:]:
    curr_node = LinkedList(node, None)
    prev_node.next = curr_node
    prev_node = curr_node

print(is_palindrome(start_node))


"""
1. Python 에도 생성자가 있다.
2. 생성자는 객체 생성 시점에 값을 세팅하는 역할을 한다.
3. 연결리스트 클래스 정의
"""
