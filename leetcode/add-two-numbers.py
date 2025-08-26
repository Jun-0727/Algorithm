class ListNode:
    val: int
    next: "ListNode"
    
    def __init__(self, val: int = 0, next: "ListNode" = None):
        self.val = val
        self.next = next

# LinkedList 뒤집기
def reverseLinkedList(head: ListNode) -> ListNode:
    node, prev = head, None

    while node:
        node.next = prev
        prev = node
        node = node.next

    head = prev
    
    return head    

# LinkedList를 List로 변환
def toList(head: ListNode) -> list:
    values: list = []

    node = head
    while node:
        values.append(node.val)
        node = node.next

    return values

# List를 LinkedList로 변환
def toLinkedList(values: list) -> ListNode:
    prev = None

    for x in values:
        node = ListNode(x)
        node.next = prev
        prev = node

    head = prev     

    return head

# 전가산기 개념을 도입한 두 LinkedList 더하기
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    prev = None
    carry = 0
    
    while l1 or l2 or carry:
        sum = 0

        if l1:
            sum += l1.val
            l1 = l1.next

        if l2:
            sum += l2.val
            l2 = l2.next
        
        carry, val = divmod(sum+carry, 10)
        node = ListNode(val)
        node.next = prev
        prev = node