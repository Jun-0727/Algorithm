# -----------
# 효율적인 해킹
# -----------

import sys
from collections import deque
input = sys.stdin.readline              # 빠른 입력

N, M = map(int, input().split())        # N: 컴퓨터 수, M: 신뢰 관계 수

graph = [[] for _ in range(N+1)]        # 인접 리스트 초기화
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)              

answer = []
result = [0] * (N+1)                    # 각 노드별 해킹 가능한 컴퓨터 개수 저장

def bfs(v):
    visited = [False] * (N+1)           # 방문 여부 배열
    que = deque([v])                    # 큐 초기화
    visited[v] = True
    count = 0                           # 현재 노드에서 해킹할 수 있는 컴퓨터 수

    while que:
        if count == N:                  # 모든 노드 방문 시 중단(무한 순환 방지)
            break

        v = que.popleft()               # BFS 탐색
        for w in graph[v]:
            if not visited[w]:
                que.append(w)
                visited[w] = True
                count += 1

    return count

for i in range(1,N+1):                  # 각 노드별 BFS 실행
    result[i] = bfs(i)

max_num = max(result)                   # 가장 많은 컴퓨터를 해킹할 수 있는 경우 찾기
for i in range(1, N+1):
    if result[i] == max_num:
        answer.append(i)
    
print(*answer)



# ------------------------------------------------------
# 한개의 노드에서 두개의 간선이 나가는 경우를 고려하지 못한 DFS 
# ------------------------------------------------------
def solution_dfs_error(graph):                    
    answer = []
    computer = []                                       # i번 컴퓨터 해킹시 해킹 가능한 컴퓨터 개수
    
    def dfs(v, count):
        if (not graph[v]) or (count == N):              # 재귀 탈출 조건 & 순환 구조 체크
            return count
        
        for w in graph[v]:                              # 가장 많은 컴퓨터를 해킹할 수 있는 개수 찾기
            return max(computer[v], dfs(w, count+1))
  
    for i in range(1, N+1):
        computer[i] = dfs(i,1)

    for i in range(1, N+1):
        if computer[i] == max(computer):
            answer.append(i)

    return answer


# ------------------------------------------------------
# DFS 탐색 - 시간초과
# ------------------------------------------------------
def solution_dfs_runtime_error(v):
    stack = [v]
    visited = [0] * (N+1)
    count = 0

    while stack:
        v = stack.pop()
        visited[v] = 1
        count += 1
        for w in graph[v]:
            if not visited[w]:
                stack.append(w)
        
    return count


for i in range(1, N+1):
    result[i] = solution_dfs_runtime_error(i)

max_num = max(result)
for i in range(1, N+1):
    if result[i] == max_num:
        answer.append(i)

print(*answer)
