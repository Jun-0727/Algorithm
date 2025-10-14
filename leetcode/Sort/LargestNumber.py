from itertools import permutations
from collections import defaultdict

li = [9, 5, 3, 30, 34]

def largest_number(li: list) -> str:
    result = 0
    for nums in permutations(li):
        tmp = ''
        for num in nums:
            tmp += str(num)
        
        result = max(result, int(tmp))
    
    return str(result)

# print(largest_number(li))


def largest_number(li: list) -> int:
    li.sort(reverse=True)
    while len(li) > 1:
        a = str(li.pop())
        b = str(li.pop())
        
        if int(a+b) > int(b+a):
            li.append(int(a+b))
        else:
            li.append(int(b+a))
        
    return li[0]

print(largest_number(li))
