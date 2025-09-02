import itertools

# 직접구현
def combine_implement(n, k):
    results = []
    path = []
    
    def dfs(start: int, k: int):
        if k == 0:
            results.append(path[:])

        for i in range(start, n+1):
            path.append(i)
            dfs(i+1, k-1)
            path.pop()

    dfs(1, k)

    return results

# 딸깍
def combine(n: int, k: int) -> list:
    return list(itertools.combinations(range(1, n+1), k))

print(combine(4,2))