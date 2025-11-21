### [백준 / 9663번] N-Queen ###

# 백트래킹 - DFS

n = int(input())
rows = [0] * n
answer = 0

### 1. 일단 놓고 확인하기 ###
# Queen을 0번 행 부터 n-1번 행 까지 차례대로 배치

# 1. x,y에 "퀸을 놓은 뒤"
# 2. 그 자리(x,y)가 놓을 수 있는 자리인지 확인하는 방법  

def promising(x, y):                            # x번째 행에 Queen을 놓아도 되는지 확인
    for i in range(x):                          # i: x 좌표 / rows[i]: y 좌표   
        if y == rows[i]:                  # 같은 열에 Queen이 존재하는 경우
            return False
        if abs(y - rows[i]) == x - i:     # 대각선에 Queen이 존재하는 경우
            return False     
    
    return True


def n_queens(x):                    # x번 행에 Queen을 놓는 함수
    global answer

    if x == n:                      # Queen을 n번째 놓는 경우라면
        answer += 1
        return
    else:
        for y in range(n):
            rows[x] = y             # x,y에 Queen을 놓고
            if promising(x):        # x번째 행에 퀸을 놓아도 되는 지 확인
                n_queens(x+1)       # x+1 번째 Queen 배치



### 2. 놓기 전에 확인하기 ###

# Queen을 0번 행 부터 n-1번 행 까지 차례대로 배치

# x,y에 "퀸을 놓기 전에"
# 그 자리(x,y)가 놓을 수 있는 자리인지 확인하고
# 놓을 수 있다면 Continue

def n_queens(x: int):               # x번 행에 Queen을 놓는 함수
    global answer

    if x == n:                      # Queen을 n번째 놓는 경우라면
        answer += 1
        return
    else:
        for y in range(n):
            if promising(x, y):     # x,y에 퀸을 놓아도 되는 지 확인
                rows[x] = y         # x,y에 Queen을 놓고
                n_queens(x+1)       # x+1 번째 Queen 배치

# n_queens(0)
# print(answer)



### 내 방식 ###
# 백트래킹
# 체스판을 1차원 배열로 표시하려니까 헷갈림 -> 2차원 배열로 표시

# Queen을 놓을 수 있는 좌표를 줄여 나가자

def n_queens(x: int, y: int, points: list, count: int) -> int:  # x,y: 퀸을 놓을 좌표 / points: Queen을 놓을 수 있는 좌표 / count: 더 놓아야 할 Queen의 개수
    if count == 0:
        return len(points)                                      # return 1 : 가능한 경우가 한가지 밖에 없다

    if not points:                                              # Queen을 놓을 수 있는 좌표가 존재하지 않는 경우
        return 0
    
    remain_points = []                                          # (x, y)에 Queen을 배치한 후 / 다른 Queen을 놓을 수 있는 좌표 리스트
    for nx, ny in points:
        if x != nx and y != ny and abs(x-nx) != abs(y-ny):      # 행/열/대각선 체크
            remain_points.append((nx, ny))

    next_points = []                                            # 다음 퀸을 놓을 좌표 리스트: n번 행에 Queen을 놓았다면 n+1번째 행 탐색
    for nx, ny in remain_points:
        if nx == x+1:
            next_points.append((nx, ny))
    
    total = 0
    for nx, ny in next_points:
        total += n_queens(nx, ny, remain_points, count-1)

    return total

points = []                              # 체스판 좌표 리스트 초기화
for i in range(n):
    for j in range(n):
        points.append((i,j))

answer = 0
for i in range(n):
    answer += n_queens(0, i, points, n-1)

print(answer)