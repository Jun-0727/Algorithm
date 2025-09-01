from collections import deque

def numberOfIslands(map: list) -> int:
    que = deque()
    answer = 0
    for x in range(len(map)):
        for y in range(len(map[0])):
            if map[x][y] == 1:
                que.append((x,y))
                while que:
                    x, y = que.pop()
                    map[x][y] = 0
                    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                        nx, ny = x + dx, y + dy

                        if nx >= 0 and nx < len(map) and ny >=0 and ny <len(map[0]) and map[nx][ny] == 1:
                            que.append((nx,ny))

                answer += 1

    return answer

# map = [[1,1,1,1,0], [1,1,0,1,0], [1,1,0,0,0], [0,0,0,0,0]]
map = [[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]


# 재귀를 이용한 문제풀이
def countIslands(grid, x, y):
    grid[x][y] = 0
    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        nx, ny = x + dx, y + dy
        if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]):
            if grid[nx][ny] == 1:
                countIslands(grid, nx, ny)

    return grid

answer = 0
for x in range(len(map)):
    for y in range(len(map[0])):
        if map[x][y] == 1:
            countIslands(map, x, y)
            answer += 1

print(answer)