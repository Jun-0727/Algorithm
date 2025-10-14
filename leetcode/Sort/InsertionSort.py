def insertion_sort(li: list) -> list:
    for i in range(len(li)):
        for j in range(0, i):
            if li[i] < li[j]:
                x = li.pop(i)
                li.insert(j, x)
                break
    
    return li


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insertion_sort(head: ListNode) -> ListNode:
    root = prev_node = ListNode()
    root.next = cur_node = unsorted_node = head

    while True:
        if unsorted_node.val < cur_node.val:
            cur_node.next = unsorted_node.next
            unsorted_node.next = cur_node
            prev_node.next = unsorted_node


    unsorted_node = unsorted_node.next