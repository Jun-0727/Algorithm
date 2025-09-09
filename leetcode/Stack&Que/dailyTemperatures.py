T = [73,74,75,71,69,72,76,73]
result = [0] * len(T)

# 시간복잡도 O(n^2)
for i in range(len(T)):
    for j in range(i+1, len(T)):
        if T[i] < T[j]:
            result[i] = j-i
            break


# 시간복잡도 O(n)
def dailyTemperatures(T: list) -> list:
    stack = []
    result = [0] * len(T)
    
    for idx, cur_temp in enumerate(T):
        while stack and cur_temp > T[stack[-1]]:
            top = stack.pop()
            result[top] = idx - top
        
        stack.append(idx)

    return result

print(dailyTemperatures(T))

"""
    스택에 '값'이 아니라 '인덱스'를 넣는 아이디어

    Why? -> 결국 result에 들어갈 값은 인덱스끼리의 차이니까!
"""