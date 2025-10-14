from heapq import heappush, heappop

def queueReconstructionByHeight(people: list):
    heap = []
    result = []

    while people:
        print(heappop(people))
    """
    for height, front_x in people:
        heappush(heap, (-height, front_x))
        print(heap)

    while heap:
        height, front_x = heappop(heap)
        result.insert(front_x, [-height, front_x])

    """
    return result

print(queueReconstructionByHeight([[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]))