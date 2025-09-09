from heapq import heappush, heappop

def mergeKLists(lists: list) -> list:
    answer = []
    heap = []
    
    for list in lists:
        for x in list:
            heappush(heap, x)
    
    while heap:
        answer.append(str(heappop(heap)))

    return '->'.join(answer)

print(mergeKLists([[1,4,5], [1,3,4], [2,6]]))