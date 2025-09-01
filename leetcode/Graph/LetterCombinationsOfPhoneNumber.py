
def solution(digits):
    result = []

    def dfs(idx, path):
        if len(path) == len(digits):
            result.append(path)
            return
        
        for i in range(idx, len(digits)):
            for c in dic[digits[i]]:
                dfs(i+1, path+c)


    path = ""
    dic = {
        "2": "abc", "3": "def", "4": "ghi",
        "5": "jkl", "6": "mno", "7": "pqrs",
        "8": "tuv", "9": "wxyz"
    }

    dfs(0,path)
    print(result)

solution("23456")