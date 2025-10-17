#-- 숨바꼭질 3 --#

import sys
from heapq import heappush, heappop
input = sys.stdin.readline
MAX_POINT = 100000

n, k = map(int, input().split())

def bfs(start, goal):
    que = []
    heappush(que, (0, start))
    visit = [False] * 100001

    visit[start] = True

    while que:
        time, x = heappop(que)
        
        if x == goal:
            return time
        
        nx = x - 1
        if nx >= 0:
            if not visit[nx]:
                visit[nx] = True
                heappush(que, (time+1, x-1)) 

        nx = x * 2
        if nx <= MAX_POINT:
            if not visit[nx]:
                visit[nx] = True
                heappush(que, (time, nx))

        nx = x + 1
        if nx <= MAX_POINT:
            if not visit[nx]:
                visit[nx] = True
                heappush(que, (time+1, nx))
            
print(bfs(n,k))
