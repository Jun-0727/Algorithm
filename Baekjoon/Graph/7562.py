import sys
from collections import deque
input = sys.stdin.readline

answers = []
test_case = int(input())
for _ in range(test_case):
    l = int(input())                                    # 체스판 한 변의 길이
    start_x, start_y = map(int, input().split())        # 시작점
    goal_x ,goal_y = map(int, input().split())          # 도착점
    
    def bfs(x,y):
        visited = [[False] * (l) for _ in range(l)]     # 방문 기록 초기화
        que = deque()                                   # 큐 생성

        que.append((x, y, 0))                           # 시작 노드(좌표) push
        visited[x][y] = True                            # 방문 기록 체크

        while que:
            x, y, move = que.popleft()                 # 좌표(x,y) & 
            if x == goal_x and y == goal_y:            # 목표 지점에 도달하면
                return move                            # 현재까지 이동 수 반환
            
            for dx, dy in [[1,2], [1,-2], [-1,2], [-1,-2], [2,1], [2,-1], [-2,1], [-2,-1]]:
                nx, ny = x + dx, y + dy

                if (0 <= nx < l) and (0 <= ny < l) and (not visited[nx][ny]):   # 좌표(nx, ny)에 대한 체스판 범위 & 방문여부 체크
                    visited[nx][ny] = True
                    que.append((nx, ny, move+1))

        return -1
    
    answers.append(bfs(start_x, start_y))                # 도착점까지 최소 이동 수

for answer in answers:
    print(answer)



# --------------------
# 재귀 연습용 코드
# --------------------
result = []
visited = [[0] * (l) for _ in range(l)]     # 방문 기록 초기화

def dfs(x, y, count):
    if x == goal_x and y == goal_y:
        result.append(count)
        return

    if (x < 0 or x >= l) or (y < 0 or y >= l):
        return
    
    if visited[x][y] > 0 and visited[x][y] < count:
        return
    
    
    visited[x][y] = count
    
    for dx, dy in [[1,2], [1,-2], [-1,2], [-1,-2], [2,1], [2,-1], [-2,1], [-2,-1]]:
        nx, ny = x + dx, y + dy
        
        dfs(nx, ny, count+1)