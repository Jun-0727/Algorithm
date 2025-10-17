#-- 경로 찾기 --#

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())                                # n: 정점의 개수

matrix = []                                     # 그래프의 인접 행렬
for _ in range(n):
    matrix.append(list(map(int, input().split())))

graph = [[] for _ in range(n)]                  # 방향 그래프
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 1:
            graph[i].append(j)

answer = [[0] * n for _ in range(n)]

def dfs(start, goal):                           # DFS 경로 탐색
    stack = [start]
    visit = [False] * n                         # 노드 체크
    count = 0                                   # 노드간 이동 횟수
    
    while stack:
        v = stack.pop()

        if v == goal and count > 0:             # 노드(v) 방문여부 체크 & goal = start인 경우 체크
            answer[start][goal] = 1
            return
        
        if not visit[v]:                        # 방문 체크
            if count > 0:
                visit[v] = True
            
            for w in graph[v]:                  # 노드(v)의 인접노드(w)에 대하여
                if answer[w][goal] == 1:        # 시간단축: 도착 노드까지 가는 경로를 이미 탐색한 경우
                    answer[start][goal] = 1
                    return
                stack.append(w)
        count += 1 
   
    return

for i in range(n):
    for j in range(n):
        dfs(i,j)

for ans in answer:
    print(' '.join(str(c) for c in ans))


"""

def bfs(start, goal):                       # BFS 경로 탐색
    que = deque([start])
    visit = [0] * n                         # 노드 체크
    count = 0                               # 노드간 이동 횟수
    
    while que:
        v = que.popleft()

        if v == goal and count > 0:         # 노드(v) 방문여부 체크 & goal = start인 경우 체크
            answer[start][goal] = 1
            return
        
        for w in graph[v]:                  # 노드(v)의 인접노드(w)에 대하여
            if answer[w][goal] == 1:        # 도착 노드까지 가는 경로를 이미 탐색한 경우
                answer[start][goal] = 1
                return
            if not visit[w]:                # 방문 체크
                visit[w] = 1
                que.append(w)
                
        count += 1 


"""


def dfs(start, goal):                           # DFS 경로 탐색
    stack = [start]
    visit = [False] * n                         # 노드 체크
    count = 0                                   # 노드간 이동 횟수
    
    while stack:
        v = stack.pop()

        if v == goal and count > 0:             # 노드(v) 방문여부 체크 & goal = start인 경우 체크
            answer[start][goal] = 1
            return

        for w in graph[v]:                      # 노드(v)의 인접노드(w)에 대하여
            if answer[w][goal] == 1:            # 시간단축: 도착 노드까지 가는 경로를 이미 탐색한 경우
                answer[start][goal] = 1
                return
            if not visit[w]:
                stack.append(w)
                visit[w] = True

        count += 1 
    
    return