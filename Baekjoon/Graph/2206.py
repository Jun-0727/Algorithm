#-- 벽 부수고 이동하기 --#

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

grid = []                                                   # 맵 초기화
for _ in range(n):
    grid.append(list(map(str, input())))

def bfs(x,y):                                               # BFS 탐색
    que = deque()                                           # 큐 생성
    visit = [[False] * m for _ in range(n)]                 # 방문 여부
    visit_with_hammer = [[False] * m for _ in range(n)]     # 핵심: 벽을 부술 해머를 가진채 방문 여부

    que.append((x, y, 1, True))
    visit[0][0] = 1

    while que:
        x, y, move, has_hammer = que.popleft()              # x, y: 좌표 / move: 이동거리 / has_hammer: 해머 존재 여부(해머로 벽을 부술 수 있음)

        if x == n-1 and y == m-1:
            return move

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x + dx, y + dy                                 # nx, ny: 다음 탐색 좌표
            
            if 0 <= nx < n and 0 <= ny < m:                         # 좌표 범위 
                if not visit[nx][ny]:                               # 방문 확인
                    if grid[nx][ny] == '1' and has_hammer:
                        visit[nx][ny] = True
                        que.append((nx, ny, move+1, False))         # has_hammer = False

                    if grid[nx][ny] == '0':
                        visit[nx][ny] = True
                        que.append((nx, ny, move+1, has_hammer))
                        
                        if has_hammer:                              # 방문 w/ hammer 확인
                            visit_with_hammer[nx][ny] = True
                
                # -----------------------------------------------------------------------------------------------
                # 방문한적 있는 경로여도 벽을 부술 기회가 남아있는 채로 방문한 것과 아닌 것의 차이를 구분 -> visit / visit_with_hammer
                # -----------------------------------------------------------------------------------------------
                else:
                    if grid[nx][ny] == '0' and has_hammer and not visit_with_hammer[nx][ny]:    # 통로이고 & 해머를 가지고 있고 & 해머를 가진채 방문한 적이 없는 좌표면
                        visit_with_hammer[nx][ny] = True
                        que.append((nx, ny, move+1, has_hammer))    

    return -1

print(bfs(0,0))