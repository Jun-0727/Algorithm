with open("input.txt", "r") as f:
    lines = f.read().splitlines()

input = lines[0]


class LinkedList:
    def __init__(self, value: int = 0, next: "LinkedList" = None):
        self.value = value
        self.next = next

def build_linked_list(path: str) -> LinkedList:
    nums = list(map(int, path.split("->")))
    
    head = LinkedList(nums[0])
    current = head
    
    for num in nums[1:]:
        current.next = LinkedList(num)
        current = current.next

    return head

def linked_list_path(head: LinkedList) -> str:
    values = []
    current = head
    while current:
        values.append(str(current.value))
        current = current.next
    return  "->".join(values)

def merge_two_lists(l1: LinkedList, l2: LinkedList): 
    if (not l1) or (l2 and l1.value > l2.value):    # l1의 헤드를 가장 작은 노드로 세팅
        l1, l2 = l2, l1
    
    if l1:                                          # l1에 노드가 남아있다면
        l1.next = merge_two_lists(l1.next, l2)      # l1.next를 재귀를 이용하여 구함
    
    return l1

str1, str2 = map(str, input.split(','))

l1 = build_linked_list(str1)
l2 = build_linked_list(str2)

result = merge_two_lists(l1, l2)
print(linked_list_path(result))