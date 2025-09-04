from collections import defaultdict, deque

def coureSchedule(n: int, course: list):
    graph = defaultdict(list)
    visited = set()
    que = deque()

    for s, e in course:
        graph[s].append(e)

    for s, e in course:
        visited.add(s)
        que.append(s)

    def dfs(v):
        if v in visited:
            return False
        
        visited.add(v)
        for w in graph[v]:
            if not dfs(w):
                return False

        return True
    
    return dfs(course[0][0])
"""    
print(False, coureSchedule(2, [[1,0], [0,1]]))
print(True, coureSchedule(2, [[1,0]]))
print(False, coureSchedule(2, [[1,2], [2,3], [3,1]]))
print(True, coureSchedule(2, [[1,2], [1,3], [2,3]]))
print(False, coureSchedule(2, [[1,2], [2,3], [3,4], [3,5], [5,6], [6,7], [7,3]]))
print(True, coureSchedule(2, [[1,2], [2,3], [3,4], [5,6], [6,7], [7,5]]))
"""

def is_finish(course: list) -> bool:
    graph = defaultdict(list)
    traced = set()
    visited = set()
    
    for s,e in course:
        graph[s].append(e)

    def dfs(v):
        if v in traced:
            return False
        
        if v in visited:
            return True
        
        traced.add(v)
        for w in graph[v]:
            if not dfs(w):
                return False
        traced.remove(v)
        visited.add(v)

        return True
    
    for x in list(graph):
        if not dfs(x):
            return False
    
    return True


print(is_finish([[1,0]]))