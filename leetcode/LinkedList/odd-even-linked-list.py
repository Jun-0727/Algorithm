class ListNode:
    val: int
    next: "ListNode"
    
    def __init__(self, val: int = 0, next: "ListNode" = None):
        self.val = val
        self.next = next


def odd_even_linked_list(head: ListNode) -> ListNode:
    if head is None:
        return None
    
    odd = head
    even = head.next
    even_head = head.next

    while even and even.next:
        odd.next = odd.next.next
        odd = odd.next
        even.next = even.next.next
        even = even.next
    
    odd.next = even_head
    
    return head

"""
    반복문 탈출 조건이 떠오르지 않을 때
    
    1. 특수 상황 예외 처리
    2. 상황별 입력 데이터 분석 ex) n=1, n=2, n=3 ...
"""
