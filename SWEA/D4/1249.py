## 보급로 ##

from heapq import heappush, heappop
MAXSIZE = 100000

def bfs(n: int, loads: list):
    heap = []
    visit = [[MAXSIZE] * n for _ in range(n)]       # 최단 시간 방문 기록
    
    heappush(heap, (0, 0, 0))                       # (걸린시간, x좌표, y좌표)
    
    while heap:
        hour, x, y = heappop(heap)

        if x == n-1 and y == n-1:                   # 목표 지점 도착
            return hour

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:                 # 도로 범위 체크
                if hour+loads[nx][ny] < visit[nx][ny]:      # nx,ny 도착까지 걸린 시간 체크
                    visit[nx][ny] = hour + loads[nx][ny]
                    heappush(heap, (hour+loads[nx][ny], nx, ny))


T = int(input())            # 테스트 케이스

for t in range(T):
    n = int(input())        # 지도의 크기
    
    loads = []              # 지도 초기화
    for _ in range(n):
        loads.append(list(map(int, input())))

    print(f'#{t+1} {bfs(n, loads)}')