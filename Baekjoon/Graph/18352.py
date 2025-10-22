#-- 특정 거리의 도시 찾기 --#

import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())      # n: 도시 수, m: 도로 수, k: 거리, x: 출발 도시

graph = defaultdict(list)                   # 간선 정보 초기화
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(x, depth):                          # 도시 거리 BFS 탐색
    result = []                             
    visit = [False] * (n+1)                 # 방문 정보
    que = deque()                           # 큐 세팅
    que.append((x,depth))                   # x: 출발 도시, depth: 이동 거리

    while que:
        v, depth = que.popleft()            # v: 출발 도시, depth: 이동 거리
        
        if not visit[v]:
            visit[v] = True
            
            if depth == k:                  # k번째 이동 후 처음 도착한 도시 v
                result.append(v)

            if depth < k:                   # <k 번째 이동 후 처음 도착한 도시 w
                for w in graph[v]:
                    que.append((w, depth+1))

    return result

cities = bfs(x, 0)

if not cities:
    print(-1)
else:
    cities.sort()
    for city in cities:
        print(city)


"""
def bfs(x, dist):
    result = []

    visit = [False] * (n+1)
    que = deque()

    visit[x] = True
    que.append((x,dist))

    while que:
        v, dist = que.popleft()

        for w in graph[v]:
            if not visit[w]:
                if dist == (k-1):
                    visit[w] = True
                    result.append(w)
                
                if dist < k-1:
                    visit[w] = True
                    que.append((w, dist+1))
    
    return result    
"""