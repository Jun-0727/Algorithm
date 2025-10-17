#-- 효율적인 해킹 --#

import sys
input = sys.stdin.readline

N, M = map(int, input().split())        # N: 컴퓨터 수, M: 신뢰 관계 수

graph = [[] for _ in range(N+1)]        # 인접 리스트 초기화
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)             

def dfs(x):
    visit = [0] * (N+1)                 # visit[x] : x 노드 방문 여부
    stack = [x]                         # 스택 초기화
    visit[x] = 1                        # 노드 x 방문 체크

    while stack:
        v = stack.pop()
        for w in graph[v]:
            if not visit[w]:            # 성능을 고려한 DFS - 스택에 넣기 전 방문 체크
                stack.append(w)
                visit[w] = 1            # 노드 w 방문 체크

    return sum(visit)

answer = []
result = [0] * (N+1)                    # 각 노드별 해킹 가능한 컴퓨터 개수 저장

for i in range(1,N+1):                  # 각 노드별 DFS 실행
    result[i] = dfs(i)

max_num = max(result)                   # max_num : 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터 수
for i in range(1, N+1):
    if result[i] == max_num:
        answer.append(i)
    
print(*answer)
