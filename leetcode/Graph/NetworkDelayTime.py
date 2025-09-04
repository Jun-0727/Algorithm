from collections import defaultdict
from heapq import heappush, heappop

def networkDelayTime(times: list, N: int, K: int) -> int:
    graph = defaultdict(list)
    dist = defaultdict(int)
    Q = [(0,K)]

    for s, e, t in times:
        graph[s].append((t,e))

    while Q:
        time, node = heappop(Q)
        if node not in dist:
            dist[node] = time
            for t, v in graph[node]:
                heappush(Q, (time+t, v))

    if len(dist) == N:
        return max(dist.values())
    
    return -1

print(networkDelayTime([[2,1,1], [2,3,1], [3,4,1]], 4, 2))
    