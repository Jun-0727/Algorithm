class ListNode:
    val: int
    next: "ListNode"

    def __init__(self, val: int = 0, next: "ListNode" = None):
        self.val = val
        self.next = next


def reverseLinkedList(self, head: ListNode, m: int, n: int) -> ListNode:
    if head is None or m == n:
        return head
    
    root = ListNode()
    root.next = head
    start = root

    for _ in range(m - 1):
        start = start.next
    end = start.next

    for _ in range(n - m):
        tmp = start.next
        start.next = end.next
        end.next = end.next.next
        start.next.next = tmp

    return root.next

"""
    Linked List를 마치면서.
    
    - LinkedList는 노드 사이의 관계에 주목해라
    - head를 가리키는 root
    - 상대적인 노드와 절대적인 노드
        - 상대적 : 위치를 표현하는 노드     ex)tmp, head
        - 절대적 : 노드 자체를 표현하는 노드 ex)root, start, end
"""