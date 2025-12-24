from collections import deque

def solution(B):
    # 경로 찾기 - BFS
    def bfs(x,y):
        que = deque([(x,y)])
        visited = [[False] * m for _ in range(n)]
        visited[x][y] = True

        while que:
            x, y = que.popleft()
            if (x, y) == (n-1, m-1):
                return True
            
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and moveable[nx][ny]:
                    visited[nx][ny] = True
                    que.append((nx, ny))

        return False
    
    n, m = len(B), len(B[0])
    moveable = [[True] * m for _ in range(n)]       # moveable: assassin이 이동 가능한 위치 좌표
    
    for i in range(n):
        for j in range(m):
            if B[i][j] in ('X', '>', '<', '^', 'v') :
                moveable[i][j] = False
            
    for i in range(n):
        for j in range(m):
            if B[i][j] == '>':
                ni, nj = i, j + 1
                while nj < m:
                    moveable[ni][nj] = False
                    nj += 1
                    if B[i][j] == 'X':
                        break

            elif B[i][j] == '<':
                ni, nj = i, j - 1
                while nj >= 0:
                    moveable[ni][nj] = False
                    nj -= 1
                    if B[i][j] == 'X':
                        break

            elif B[i][j] == '^':
                ni, nj = i - 1, j
                while ni >= 0:
                    moveable[ni][nj] = False
                    ni -= 1
                    if B[i][j] == 'X':
                        break
                    

            elif B[i][j] == 'v':
                ni, nj = i + 1, j
                while ni < n:
                    moveable[ni][nj] = False
                    ni += 1
                    if B[i][j] == 'X':
                        break

    # 도착 지점이 False인 경우
    if not moveable[n-1][m-1]:
        return False

    # 시작점 찾기
    for i in range(n):
        for j in range(m):
            if B[i][j] == 'A':
                sx, sy = i, j               # sx: 시작점 x좌표 / sy: 시작점 y좌표
                break
    
    return bfs(sx, sy)
