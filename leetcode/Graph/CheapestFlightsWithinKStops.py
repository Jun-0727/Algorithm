from collections import defaultdict
from heapq import heappush, heappop

# 다익스트라 
def dijkstraK(n: int, edges: list, src: int, dst: int, K: int) -> int:
    graph = defaultdict(list)
    for start, end, price in edges:
        graph[start].append((price, end))
    
    Q = [(0, src, 0)]

    while Q:
        price, node, k = heappop(Q)

        if node == dst:
            return price
        
        if k <= K:
            for p, v in graph[node]:
                heappush(Q, (price+p, v, k+1))
        
    return -1
    
print(dijkstraK(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0))