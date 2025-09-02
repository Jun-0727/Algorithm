import itertools

# dfs의 인자로 정점(v)를 넣을 때
def permute_param_v(nums: list) -> list:
    result, path = [], []
    graph = {i: [x for x in nums if x != i] for i in nums}  # dict로 단순화
    def dfs(v):    
        path.append(v)
        
        if len(path) == len(nums):
            result.append(path[:])
            path.pop()
            return
        
        for w in graph[v]:
            if not w in path:
                dfs(w)
        path.pop()
    
    for v in nums:
        dfs(v)

    return result


# dfs의 인자로 nums: list를 넣을 때
def permute_param_list(nums: list) -> list:
    results = []
    path = []

    def dfs(elements):
        if not elements:
            results.append(path[:])
            return

        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            path.append(e)
            dfs(next_elements)
            path.pop()
    
    dfs(nums)
    return results

# itertools
def permute(nums: list) -> list:
    return list(itertools.permutations(nums))
    
print(permute([1,2,3,4]))