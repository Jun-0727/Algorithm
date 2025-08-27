class ListNode:
    val: int
    next: "ListNode"

    def __init__(self, val: int = 0, next: "ListNode" = None):
        self.val = val
        self.next = next


def swapPairNodes(head: ListNode) -> ListNode:
    prev = root = ListNode()
    node1, node2 = head, head.next
    while node1 and node2:
        prev.next = node2
        node1.next = node2.next
        node2.next = node1

        prev = node2
        node1 = node1.next
        node2 = node2.next

    return root.next


# 재귀를 이용한 아름다운 풀이
def swapPairNode2(self, head: ListNode) -> ListNode:
    if head and head.next:
        p_node = head.next
        head.next = self.swapPairNode2(p_node.next)
        p_node.next = head

        return p_node

    return head