from collections import Counter

def jewelsCounter(J: str, S: str):
    answer = 0

    stones = Counter(S)
    print(stones)
    
    for j in J:
        answer += stones[j]

    return answer

print(jewelsCounter('aA', 'aAAbbbb'))