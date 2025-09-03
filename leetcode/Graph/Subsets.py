# 와, 책이랑 똑같이 풀었다..!
def subset(nums: list) -> list:
    result = []

    def dfs(start, path):
        result.append(path)

        for i in range(start, len(nums)):
            dfs(i+1, path+[nums[i]])

    dfs(0, [])

    return result

print(subset([1,2,3]))
