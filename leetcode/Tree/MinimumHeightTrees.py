from collections import deque, defaultdict

# n = 4
# edges = [[1,0], [1,2], [1,3]]
n = 6
edges = [[0,3], [1,3],[2,3],[4,3],[5,4]]
graph = defaultdict(list)

for a,b in edges:
    graph[a].append(b)
    graph[b].append(a)


def bfs(root):
    height = -1
    visit = [False] * (n)
    que = deque()

    visit[root] = True
    que.append(root)

    while que:
        for _ in range(len(que)):
            node = que.popleft()

            for w in graph[node]:
                if not visit[w]:
                    visit[w] = True
                    que.append(w)
        height += 1
    
    return height

heigts = []                   

for i in range(n):
    heigts.append(bfs(i))

print(heigts)