# 시작 index를 고려하지 않은 dfs
# 조합에 중복이 생긴다 ex) [2,2,3], [2,3,2], [3,2,2]
def combinationSum(nums: list, target: int):
    results = []
    
    def dfs(sum: int, path: list):
        if sum == target:
            results.append(path[:])
            return
        
        if sum > target:
            return
        
        for n in nums:
            path.append(n)
            dfs(sum+n, path)
            path.pop()
    
    for n in nums:
        dfs(n, [n])
    
    return results

# Best 답변
def combinationSum(candidates: list, target: int):
    result = []

    def dfs(csum, index, path):
        if csum == 0:
            result.append(path)
            return
        
        if csum < 0:
            return
        
        for i in range(index, len(candidates)):
            v = candidates[i]
            dfs(csum - v, i, path+[v])

    dfs(target, 0, [])

    return result

# My Algorithm
# target -> 0 으로 줄여나기기 보단
# 0 -> target 으로 더하면서 찾아가는게 편함
def combinationSum(candidates: list, target: int):
    results = []

    def dfs(sum: int, start: int, path: list):
        if sum == target:
            results.append(path[:])
            return
        
        if sum > target:
            return

        for i in range(start, len(candidates)):
            v = candidates[i]
            path.append(v)
            dfs(sum+v, i, path)
            path.pop()

    dfs(0, 0, [])

    return results

print(combinationSum([2,3,6,7], 7))